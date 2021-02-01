from .models import Room, Message
from rest_framework import serializers
from django_restql.mixins import DynamicFieldsMixin


class RoomSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    # messages = serializers.SerializerMethodField('get_messages')

    # def get_messages(self, room):
    #     return MessageSerializer(instance=Message.objects.filter(room=room)[:50], many=True).data

    class Meta:
        model = Room
        fields = [
            'id', 'tutor', 'student', 'tutor_connected', 'student_connected',
            'tutor_unread_msgs', 'student_unread_msgs', 'messages',
        ]
        # extra_kwargs = {'tutor': {'read_only': True},
        #                 'student': {'read_only': True}}


class MessageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Message
        fields = [
            'id', 'room', 'author', 'message', 'timestamp', 'read',
        ]
        # extra_kwargs = {'room': {'write_only': True}, 'author': {
        #     'write_only': True}, 'message': {'write_only': True}}
