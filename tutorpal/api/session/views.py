from .models import Session
from .serializers import SessionSerializer, ReservedSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
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
            pk = self.kwargs.get('pk')
            try:
                if Session.objects.get(pk=pk).tutor.user == self.request.user or Session.objects.get(pk=pk).student.user == self.request.user:
                    return SessionSerializer
            except ObjectDoesNotExist:
                return ReservedSerializer
            return ReservedSerializer
        # elif self.action in ["my_sessions", "pending_on_tutor", "pending_on_student_payment", "upcoming", "tutor_not_paid", "finished_sessions", "canceled_sessions", "started_sessions"]:
        #     return SessionSerializer
        return SessionSerializer

    @action(detail=False, permission_classes=[IsAuthenticated])
    def my_sessions(self, request):
        if hasattr(request.user, 'student'):
            session_queryset = Session.objects.filter(
                student=request.user.student)
        elif hasattr(request.user, 'tutor'):
            session_queryset = Session.objects.filter(tutor=request.user.tutor)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(session_queryset)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(session_queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def pending_on_tutor(self, request):
        if hasattr(request.user, 'student'):
            session_queryset = Session.objects.filter(
                student=request.user.student, accepted=False, rejected=False, canceled=False)
        elif hasattr(request.user, 'tutor'):
            session_queryset = Session.objects.filter(
                tutor=request.user.tutor, accepted=False, rejected=False, canceled=False)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(session_queryset)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(session_queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def pending_on_student_payment(self, request):
        if hasattr(request.user, 'student'):
            my_sessions = Session.objects.filter(
                student=request.user.student, student_paid=False, canceled=False, accepted=True)
        elif hasattr(request.user, 'tutor'):
            my_sessions = Session.objects.filter(
                tutor=request.user.tutor, student_paid=False, canceled=False, accepted=True)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(my_sessions)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(my_sessions, many=True)
        return Response(serializer_class.data)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def upcoming(self, request):
        if hasattr(request.user, 'student'):
            session_queryset = Session.objects.filter(
                student=request.user.student, accepted=True, student_paid=True, canceled=False)
        elif hasattr(request.user, 'tutor'):
            session_queryset = Session.objects.filter(
                tutor=request.user.tutor, accepted=True, student_paid=True, canceled=False)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(session_queryset)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(session_queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def tutor_not_paid(self, request):
        if hasattr(request.user, 'student'):
            session_queryset = Session.objects.filter(
                student=request.user.student, canceled=False, finished=True, tutor_paid=False)
        elif hasattr(request.user, 'tutor'):
            session_queryset = Session.objects.filter(
                tutor=request.user.tutor, canceled=False, finished=True, tutor_paid=False)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(session_queryset)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(session_queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def finished_sessions(self, request):
        if hasattr(request.user, 'student'):
            session_queryset = Session.objects.filter(
                student=request.user.student, finished=True, tutor_paid=True)
        elif hasattr(request.user, 'tutor'):
            session_queryset = Session.objects.filter(
                tutor=request.user.tutor, finished=True, tutor_paid=True)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(session_queryset)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(session_queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def canceled_sessions(self, request):
        if hasattr(request.user, 'student'):
            session_queryset = Session.objects.filter(
                student=request.user.student, canceled=True)
        elif hasattr(request.user, 'tutor'):
            session_queryset = Session.objects.filter(
                tutor=request.user.tutor, canceled=True)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(session_queryset)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(session_queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def started_sessions(self, request):
        if hasattr(request.user, 'student'):
            session_queryset = Session.objects.filter(
                student=request.user.student, started=True)
        elif hasattr(request.user, 'tutor'):
            session_queryset = Session.objects.filter(
                tutor=request.user.tutor, started=True)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(session_queryset)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(session_queryset, many=True)
        return Response(serializer_class.data)

    # @action(detail=True)
    # def pay_tutor(self, request):
    #     if hasattr(request.user, 'tutor'):

    def perform_create(self, serializer):
        serializer.save(student=self.request.user.student)
