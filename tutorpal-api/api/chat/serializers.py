from .models import Room, Message
from rest_framework import serializers
from register.serializers import StudentViewingSerializer, TutorViewingSerializer


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = [
            'id', 'tutor_pk', 'student_pk'
        ]


class StudentRoomSerializer(serializers.ModelSerializer):
    tutor = TutorViewingSerializer(read_only=True)

    class Meta:
        model = Room
        fields = [
            'id', 'tutor_pk', 'student_pk', 'tutor'
        ]


class TutorRoomSerializer(serializers.ModelSerializer):
    student = StudentViewingSerializer(read_only=True)

    class Meta:
        model = Room
        fields = [
            'id', 'tutor_pk', 'student_pk', 'student'
        ]


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'id', 'author', 'message', 'timestamp'
        ]
        # extra_kwargs = {'room': {'write_only': True}, 'author': {
        #     'write_only': True}, 'message': {'write_only': True}}
