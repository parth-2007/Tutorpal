from .models import Session
from rest_framework import serializers, status
from django_restql.mixins import DynamicFieldsMixin


class SessionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'id', 'student', 'tutor',
            'date', 'time_start', 'time_end', 'duration',
            'price', 'free', 'description', 'call_url',
            'accepted', 'rejected', 'started', 'finished', 'accessable', 'canceled',
            'student_paid', 'tutor_paid',
            'refund_requested', 'refund_available', 'refunded',
            'tutor_emailed', 'student_emailed', 'parent_emailed',
        ]

    # def update(self, instance, validated_data):
    #     instance.canceled = validated_data.get('canceled', instance.canceled)
    #     instance.save()
    #     return instance


class ReservedSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'tutor', 'date', 'time_start', 'time_end', 'id'
        ]
