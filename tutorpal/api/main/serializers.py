from .models import Bugs, Feedback
from rest_framework import serializers


class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bugs
        fields = ['bug', 'level']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['text']
