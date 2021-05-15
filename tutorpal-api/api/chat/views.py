from .models import Room, Message
from .serializers import StudentRoomSerializer, TutorRoomSerializer, MessageSerializer, RoomSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action

# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # filter to rooms they own
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated, DRYPermissions]

    def get_queryset(self):
        if self.request.user.has_student:
            return Room.objects.filter(student_pk=self.request.user.student_pk)
        elif self.request.user.has_tutor:
            return Room.objects.filter(tutor_pk=self.request.user.tutor_pk)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You are not authenticated")

    def get_serializer_class(self):
        if self.request.user.has_student:
            return StudentRoomSerializer
        elif self.request.user.has_tutor:
            return TutorRoomSerializer
        return RoomSerializer

    @action(detail=True)
    def messages(self, request, pk):
        room = Room.objects.get(pk=pk)
        if self.request.user.has_student and self.request.user.student_pk == room.student_pk:
            queryset = Message.objects.filter(room=room)
        elif self.request.user.has_tutor and self.request.user.tutor_pk == room.tutor_pk:
            queryset = Message.objects.filter(room=room)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view these messages")

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer_class = MessageSerializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = MessageSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def perform_create(self, serializer):
        serializer.save(tutor_pk=int(self.request.data.get(
            'tutor')), student_pk=self.request.user.student_pk)
