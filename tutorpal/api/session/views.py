from .models import Session
from .serializers import SessionSerializer, ReservedSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from dry_rest_permissions.generics import DRYPermissions
from django.core.exceptions import ObjectDoesNotExist
from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class SessionViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Session.objects.all()
    # serializer_class = SessionSerializer
    permission_classes = [DRYPermissions]

    def get_serializer_class(self):
        if self.action == "list":
            return ReservedSerializer
        elif self.action == "retrieve":
            pk = self.request.META.get("PATH_INFO")[10:-1]
            try:
                if Session.objects.get(pk=pk).tutor.user == self.request.user or Session.objects.get(pk=pk).student.user == self.request.user:
                    return SessionSerializer
            except ObjectDoesNotExist:
                return ReservedSerializer
            return ReservedSerializer
        return SessionSerializer

    @action(detail=False, permission_classes=[IsAuthenticated])
    def my_sessions(self, request):
        if hasattr(request.user, 'student'):
            my_sessions = Session.objects.filter(student=request.user.student)
        elif hasattr(request.user, 'tutor'):
            my_sessions = Session.objects.filter(tutor=request.user.tutor)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(my_sessions)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(my_sessions, many=True)
        return Response(serializer_class.data)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user.student)
