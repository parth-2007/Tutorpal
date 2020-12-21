from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from rest_framework import permissions, viewsets, status, mixins, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from dry_rest_permissions.generics import DRYPermissions
from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework.views import APIView

# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # filter to rooms they own
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated, DRYPermissions]

    def get_queryset(self):
        if hasattr(self.request.user, 'student'):
            return Room.objects.filter(student=self.request.user.student)
        elif hasattr(self.request.user, 'tutor'):
            return Room.objects.filter(tutor=self.request.user.tutor)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You are not authenticated")


# class MessageViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
#     queryset = Message.objects.all()  # filter to rooms they own
#     serializer_class = MessageSerializer
#     permission_classes = []


# class RoomSockets(mixins.UpdateModelMixin, generics.GenericAPIView):
#     # queryset = Room.objects.all()
#     # serializer_class = RoomSerializer

#     def get_serializer_class(self, request):
#         pass

#     def get_queryset(self):
#         if hasattr(self.request.user, 'student'):
#             return Room.objects.filter(student=self.request.user.student)
#         elif hasattr(self.request.user, 'tutor'):
#             return Room.objects.filter(tutor=self.request.user.tutor)
#         else:
#             return Response(status=status.HTTP_403_FORBIDDEN, data="You are not authenticated")

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
