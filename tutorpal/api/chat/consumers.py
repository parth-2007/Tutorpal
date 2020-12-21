import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from register.models import User, Student, Tutor
from .models import Room, Message
from channels import exceptions
from django.utils import timezone
from asgiref.sync import sync_to_async
import datetime
import pytz
import json


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Connected', event)

        other_user = self.scope['url_route']['kwargs']['user_id']
        me = self.scope['user']
        self.me_user_obj = await self.get_user(email=me)
        room_obj = await self.get_room(other_user=other_user, email=me)
        self.room_obj = room_obj
        chat_room = f"room_{room_obj.id}"
        self.chat_room = chat_room
        self.last_ts = await self.get_last_ts()
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept"
        })

        await self.connect_save_user()

    async def websocket_receive(self, event):
        print('Received', event)
        front_text = event.get("text", None)
        front_dict = json.loads(front_text)
        message = front_dict.get("message")
        tzname = front_dict.get("tzname")
        if len(message.replace(" ", "")) > 0:
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get('message')
            timestamp = self.last_ts
            user_email = self.scope['user']
            me_user_obj = self.me_user_obj
            diff = timezone.now() - timestamp
            if diff.seconds >= 1:
                if tzname != "None":
                    tzone = pytz.timezone(tzname)
                    local_time = timezone.now().astimezone(tzone)
                else:
                    local_time = timezone.now()
                myResponse = {
                    'message': msg,
                    'full_name': me_user_obj.first_name + " " + me_user_obj.last_name,
                    'year': local_time.year,
                    'month': local_time.month,
                    'day': local_time.day,
                    'hour': local_time.hour,
                    'minute': local_time.minute,
                    'cooldown': False,
                    'student': me_user_obj.is_student,
                    'tutor': me_user_obj.is_tutor,
                }
                await self.create_chat_message(msg)
                #other_user_obj = User.objects.get(id=self.scope['url_route']['kwargs']['user_id'])
                room = self.room_obj
                # self.last_msg = created_msg

                await self.channel_layer.group_send(
                    self.chat_room,
                    {
                        "type": "chat_message",
                        "text": json.dumps(myResponse)
                    }
                )
                self.last_ts = await self.get_last_ts()
            else:
                myResponse = {
                    'message': msg,
                    'full_name': me_user_obj.first_name + " " + me_user_obj.last_name,
                    'year': timezone.now().year,
                    'month': timezone.now().month,
                    'day': timezone.now().day,
                    'hour': timezone.now().hour,
                    'minute': timezone.now().minute,
                    'cooldown': True,
                    'student': me_user_obj.is_student,
                    'tutor': me_user_obj.is_tutor,
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
        await self.disconnect_save_user()
        print('Disconnected', event)
        raise exceptions.StopConsumer()

    @database_sync_to_async
    def get_room(self, other_user, email):
        me = User.objects.get(email=email)
        if me.is_tutor:
            me_obj = Tutor.objects.get(user=me)
            other_user_obj = Student.objects.get(id=other_user)
            return Room.objects.get(student=other_user_obj, tutor=me_obj)
        elif me.is_student:
            me_obj = Student.objects.get(user=me)
            other_user_obj = Tutor.objects.get(id=other_user)
            return Room.objects.get(tutor=other_user_obj, student=me_obj)

    @database_sync_to_async
    def get_user(self, email):
        user_obj = User.objects.get(email=email)
        return user_obj

    @database_sync_to_async
    def create_chat_message(self, msg):
        room_obj = Room.objects.get(id=self.room_obj.id)
        me_user_obj = self.me_user_obj
        tutor_unread_msgs = room_obj.tutor_unread_msgs
        student_unread_msgs = room_obj.student_unread_msgs
        print("Tutor connection: ", room_obj.tutor_connected)
        print("Student connection: ", room_obj.student_connected)
        if me_user_obj.is_student:
            print("Student sending...")
            if room_obj.tutor_connected:
                read = True
                print("Message read!")
            else:
                read = False
                tutor_unread_msgs += 1
                room_obj.tutor_unread_msgs = tutor_unread_msgs
                room_obj.save()
        if me_user_obj.is_tutor:
            print("Tutor sending...")
            if room_obj.student_connected:
                read = True
                print("Message read!")
            else:
                read = False
                student_unread_msgs += 1
                room_obj.student_unread_msgs = student_unread_msgs
                room_obj.save()
        return Message.objects.create(author=me_user_obj, room=room_obj, message=msg, read=read)

    @database_sync_to_async
    def get_last_ts(self):
        room_obj = self.room_obj
        try:
            msg = Message.objects.filter(room=room_obj).order_by('-id')[0]
            ts = msg.timestamp
        except:
            ts = datetime.datetime.now() - datetime.timedelta(minutes=1)
            ts = timezone.utc.localize(ts)
        return ts

    @database_sync_to_async
    def connect_save_user(self):
        room_obj = Room.objects.get(id=self.room_obj.id)
        user_obj = self.me_user_obj
        print("connected: ", user_obj, " in ", room_obj)
        if user_obj.is_student:
            room_obj.student_connected = True
            print("student connected")
            for unread_msg in Message.objects.filter(read=False):
                if unread_msg.author.is_tutor:
                    print("read unreead messages!")
                    unread_msg.read = True
                    unread_msg.save()
            room_obj.student_unread_msgs = 0
        elif user_obj.is_tutor:
            room_obj.tutor_connected = True
            print("tutor connected")
            for unread_msg in Message.objects.filter(read=False):
                if unread_msg.author.is_student:
                    print("read unread messages!")
                    unread_msg.read = True
                    unread_msg.save()
            room_obj.tutor_unread_msgs = 0
        room_obj.save()

    @database_sync_to_async
    def disconnect_save_user(self):
        room_obj = Room.objects.get(id=self.room_obj.id)
        user_obj = self.me_user_obj
        print("disconnected: ", user_obj, " in ", room_obj)
        if user_obj.is_student:
            print("disconnected student!")
            room_obj.student_connected = False
            room_obj.save()
        elif user_obj.is_tutor:
            print("disconnected tutor!")
            room_obj.tutor_connected = False
            room_obj.save()
