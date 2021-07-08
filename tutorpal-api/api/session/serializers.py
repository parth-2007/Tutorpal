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
            'student_paid', 'payment_id', 'student_joined'
        ]
        read_only_fields = ['student_paid', 'finished', 'call_url',
                            'accepted', 'rejected', 'started', 'finished']
        extra_kwargs = {'payment_id': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.student_joined = validated_data.get(
            'student_joined', instance.student_joined)
        instance.save()
        return super().update(instance, validated_data)


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
        ]
        read_only_fields = [
            'id', 'student', 'tutor_pk',
            'date', 'time_start', 'time_end', 'duration',
            'price', 'free', 'description', 'call_url', 'subjects',
            'student_paid', 'tutor_paid', 'student_joined'
        ]


class ReservedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'tutor_pk', 'date', 'time_start', 'time_end', 'id'
        ]
        read_only_fields = fields
