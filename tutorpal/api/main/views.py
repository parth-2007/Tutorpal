from rest_framework import viewsets, mixins
from .serializers import BugSerializer, FeedbackSerializer
from .models import Bugs, Feedback


class BugViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Bugs.objects.all()
    serializer_class = BugSerializer


class FeedbackViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
