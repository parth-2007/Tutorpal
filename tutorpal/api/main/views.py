from rest_framework import viewsets
from .serializers import BugSerializer, FeedbackSerializer
from .models import Bugs, Feedback


class BugViewSet(viewsets.ModelViewSet):
    queryset = Bugs.objects.all()
    serializer_class = BugSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
