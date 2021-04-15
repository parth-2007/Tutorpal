from .models import Room
from .serializers import RoomSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from dry_rest_permissions.generics import DRYPermissions

# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # filter to rooms they own
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated, DRYPermissions]

    def get_queryset(self):
        if self.request.user.has_student:
            return Room.objects.filter(student__id=self.request.user.student_pk)
        elif self.request.user.has_tutor:
            return Room.objects.filter(tutor__id=self.request.user.tutor_pk)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You are not authenticated")

    # @action(detail=False)
    # def inbox(self, request):
    #     if self.request.user.has_student:
    #         room_queryset = Room.objects.filter(
    #             student=request.user.student)
    #     elif self.request.user.has_tutor:
    #         room_queryset = Room.objects.filter(tutor=request.user.tutor)
    #     else:
    #         return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your rooms")

    #     page = self.paginate_queryset(room_queryset)
    #     if page is not None:
    #         serializer_class = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer_class.data)

    #     serializer_class = self.get_serializer(room_queryset, many=True)
    #     return Response(serializer_class.data)

    def perform_create(self, serializer):
        serializer.save(tutor_pk=int(self.request.data.get('tutor')), student_pk=self.request.user.student_pk)