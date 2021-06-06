from .models import Session
from rest_framework import serializers
from register.serializers import StudentViewingSerializer, TutorViewingSerializer


class StudentSessionSerializer(serializers.ModelSerializer):
    tutor = TutorViewingSerializer(read_only=True)

    class Meta:
        model = Session
        fields = [
            'id', 'tutor', 'student_pk',
            'date', 'time_start', 'time_end', 'duration',
            'price', 'free', 'description', 'call_url', 'subjects',
            'accepted', 'rejected', 'started', 'finished', 'accessable', 'canceled',
            'student_paid', 'tutor_paid',
            'refund_requested', 'refund_available', 'refunded', 'refund_description',
            'tutor_emailed', 'student_emailed', 'parent_emailed',
        ]


class TutorSessionSerializer(serializers.ModelSerializer):
    student = StudentViewingSerializer(read_only=True)

    class Meta:
        model = Session
        fields = [
            'id', 'student', 'tutor_pk',
            'date', 'time_start', 'time_end', 'duration',
            'price', 'free', 'description', 'call_url', 'subjects',
            'accepted', 'rejected', 'started', 'finished', 'accessable', 'canceled',
            'student_paid', 'tutor_paid',
            'refund_requested', 'refund_available', 'refunded', 'refund_description',
            'tutor_emailed', 'student_emailed', 'parent_emailed',
        ]


class ReservedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'tutor_pk', 'date', 'time_start', 'time_end', 'id'
        ]
        read_only_fields = fields
