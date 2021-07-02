from .models import Room, Message
from rest_framework import serializers
from register.serializers import StudentViewingSerializer, TutorViewingSerializer
from django.db.models import Count, Q


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id']


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'tutor', 'student', 'tutor_pk', 'student_pk'
        ]


class StudentRoomSerializer(serializers.ModelSerializer):
    tutor = TutorViewingSerializer(read_only=True)
    unread = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = [
            'id', 'tutor_pk', 'student_pk', 'tutor', 'unread'
        ]

    def get_unread(self, obj):
        unread_count = Message.objects.filter(room=obj).exclude(author=obj.student.user).aggregate(
            unread=Count('pk', filter=Q(student_read=False))
        )
        return unread_count.get('unread')


class TutorRoomSerializer(serializers.ModelSerializer):
    student = StudentViewingSerializer(read_only=True)
    unread = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = [
            'id', 'tutor_pk', 'student_pk', 'student', 'unread'
        ]

    def get_unread(self, obj):
        unread_count = Message.objects.filter(room=obj).exclude(author=obj.tutor.user).aggregate(
            unread=Count('pk', filter=Q(tutor_read=False))
        )
        return unread_count.get('unread')


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'id', 'author', 'message', 'timestamp', 'tutor_read', 'student_read'
        ]
        # extra_kwargs = {'room': {'write_only': True}, 'author': {
        #     'write_only': True}, 'message': {'write_only': True}}
