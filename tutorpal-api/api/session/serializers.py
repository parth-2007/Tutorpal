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
            'accepted', 'rejected', 'started', 'finished', 'canceled',
            'student_paid', 'tutor_paid', 'payment_id', 'student_joined'
            # 'tutor_emailed', 'student_emailed', 'parent_emailed',
            # 'refund_requested', 'refund_available', 'refunded', 'refund_description',
        ]
        extra_kwargs = {'payment_id': {'write_only': True},
                        'student_paid': {'read_only': True},
                        'finished': {'read_only': True}}


class TutorSessionSerializer(serializers.ModelSerializer):
    student = StudentViewingSerializer(read_only=True)

    class Meta:
        model = Session
        fields = [
            'id', 'student', 'tutor_pk',
            'date', 'time_start', 'time_end', 'duration',
            'price', 'free', 'description', 'call_url', 'subjects',
            'accepted', 'rejected', 'started', 'finished', 'canceled',
            'student_paid', 'tutor_paid', 'student_joined'
            # 'tutor_emailed', 'student_emailed', 'parent_emailed',
            # 'refund_requested', 'refund_available', 'refunded', 'refund_description',
        ]
        extra_kwargs = {'student_paid': {'read_only': True}}


class ReservedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'tutor_pk', 'date', 'time_start', 'time_end', 'id'
        ]
        read_only_fields = fields
