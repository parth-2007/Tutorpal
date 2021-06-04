from .models import Room, Message
from .serializers import StudentRoomSerializer, TutorRoomSerializer, MessageSerializer, RoomSerializer, CreateRoomSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action
from register.models import Tutor, Student

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
        if self.action == 'create':
            return CreateRoomSerializer
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

    def create(self, request, *args, **kwargs):
        serializer = CreateRoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        req_data = request.data
        req_data['tutor'] = Tutor.objects.get(pk=req_data.get('tutor_pk'))
        req_data['student'] = Student.objects.get(
            pk=req_data.get('student_pk'))
        room, created = Room.objects.get_or_create(**req_data)
        # if request.user.has_tutor:
        #     data = TutorRoomSerializer(room).data
        # elif request.user.has_student:
        #     data = StudentRoomSerializer(room).data
        # else:
        data = RoomSerializer(room).data
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK, headers=headers)
