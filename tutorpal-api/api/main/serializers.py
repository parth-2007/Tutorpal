from .models import Bugs, Feedback
from rest_framework import serializers


class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bugs
        fields = ['bug', 'level']
    
    def validate(self, attrs):
        level = attrs.get('level', 0)
        if not 1 <= level <= 10:
            raise serializers.ValidationError('level must be in between 1 and 10')
        return super().validate(attrs)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['text']
