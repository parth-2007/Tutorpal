from .models import Session, Seminar
from rest_framework import serializers
from register.serializers import StudentViewingSerializer, TutorViewingSerializer, NestedTutorSerializer

import random

# one for not in the seminar as a student


class StudentSeminarSerializer(serializers.ModelSerializer):
    tutor = NestedTutorSerializer(read_only=True)

    class Meta:
        model = Seminar
        fields = [
            'id', 'tutor',
            'times', 'duration',
            'description', 'subjects',
            'price', 'free',
            'student_number', 'active', 'sessions_completed'
        ]
        read_only_fields = fields


class TutorSeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar
        fields = [
            'id', 'call_url',
            'times', 'duration',
            'description', 'subjects',
            'price', 'free',
            'student_number', 'active',
            'payouts', 'sessions_completed'
        ]
        read_only_fields = ['tutor',
                            'payouts', 'sessions_completed']

    def create(self, validated_data):
        request = self.context['request']
        data = request.data
        tutor = request.user.tutor

        # making url
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        call_url = ''.join(random.choice(letters) for i in range(30))

        # checking for prices
        if data.get('free', False):
            price = 0
            free = True
        else:
            price = data.get('price')
            free = False
        if data.get('price', 0) == 0:
            free = True

        validated_data['tutor'] = tutor
        validated_data['tutor_pk'] = tutor.pk
        validated_data['free'] = free
        validated_data['price'] = price
        validated_data['call_url'] = call_url
        return super().create(validated_data)

    def save(self, **kwargs):
        return super().save(**kwargs)


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
