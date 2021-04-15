from .models import Room, Message
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id', 'tutor_pk', 'student_pk'
        ]


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'id', 'author', 'message', 'timestamp'
        ]
        # extra_kwargs = {'room': {'write_only': True}, 'author': {
        #     'write_only': True}, 'message': {'write_only': True}}
