from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from rest_framework import permissions, viewsets, status, mixins, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from dry_rest_permissions.generics import DRYPermissions
from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework.views import APIView
from rest_framework.decorators import action

# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # filter to rooms they own
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated, DRYPermissions]

    def get_queryset(self):
        if self.request.user.has_student:
            return Room.objects.filter(student=self.request.user.student)
        elif self.request.user.has_tutor:
            return Room.objects.filter(tutor=self.request.user.tutor)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You are not authenticated")

    @ action(detail=False)
    def inbox(self, request):
        if self.request.user.has_student:
            room_queryset = Room.objects.filter(
                student=request.user.student)
        elif self.request.user.has_tutor:
            room_queryset = Room.objects.filter(tutor=request.user.tutor)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your rooms")

        page = self.paginate_queryset(room_queryset)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(room_queryset, many=True)
        return Response(serializer_class.data)


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
