from .models import Bugs, Feedback
from rest_framework import serializers, status
from django_restql.mixins import DynamicFieldsMixin


class BugSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Bugs
        fields = ['bug', 'level']


class FeedbackSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['text']
