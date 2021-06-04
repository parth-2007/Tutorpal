import json
# from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from register.models import User  # , Student, Tutor
from .models import Room, Message
from channels import exceptions
from django.utils import timezone
import pytz
# from asgiref.sync import sync_to_async


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        # print('Connected', event)
        # get my user obj and room obj
        room_id = self.scope['url_route']['kwargs']['room_id']
        room_obj = await self.get_room(room_id)
        self.room_obj = room_obj
        self.me_user_obj = self.scope['user']
        self.chat_room = f"room_{room_id}"
        await self.send({
            "type": "websocket.accept"
        })
        await self.channel_layer.group_add(
            self.chat_room,
            self.channel_name
        )

    async def websocket_receive(self, event):
        # print('Received', event)
        message = event.get("text", None)
        # front_dict = json.loads(front_text)
        # message = front_dict.get("message")
        tzname = self.scope['cookies'].get("tz_name")
        if message is not None and len(message.replace(" ", "")) > 0:
            # loaded_dict_data = json.loads(front_text)
            # msg = loaded_dict_data.get('message')
            me_user_obj = self.me_user_obj
            room_obj = self.room_obj
            if self.check_user_in_room(me_user_obj, room_obj):
                if tzname != "None" and tzname is not None:
                    tzone = pytz.timezone(tzname)
                    local_time = timezone.now().astimezone(tzone)
                else:
                    local_time = timezone.now()
                message_obj = await self.create_chat_message(message)
                myResponse = {
                    'message': message,
                    'author': me_user_obj.id,
                    'timestamp': str(local_time),
                    'id': message_obj.id,
                }
                await self.channel_layer.group_send(
                    self.chat_room,
                    {
                        "type": "chat_message",
                        "text": json.dumps(myResponse)
                    }
                )
            else:
                myResponse = {
                    'error': 'user is not in room'
                }
                await self.channel_layer.group_send(
                    self.chat_room,
                    {
                        "type": "chat_message",
                        "text": json.dumps(myResponse)
                    }
                )

    async def chat_message(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        # print('Disconnected', event)
        try:
            for group in self.groups:
                await self.channel_layer.group_discard(group, self.channel_name)
        except AttributeError:
            raise exceptions.InvalidChannelLayerError(
                "BACKEND is unconfigured or doesn't support groups"
            )
        await self.disconnect(event["code"])
        raise exceptions.StopConsumer()

    @database_sync_to_async
    def get_room(self, id):
        return Room.objects.get(id=id)

    @database_sync_to_async
    def create_chat_message(self, msg):
        room_obj = self.room_obj
        me_user_obj = self.me_user_obj
        message = Message.objects.create(
            author=me_user_obj, room=room_obj, message=msg)
        return message

    @database_sync_to_async
    def check_user_in_room(self, user: User, room: Room) -> bool:
        if room.student.user == user or room.tutor.user == user:
            return True
        return False
