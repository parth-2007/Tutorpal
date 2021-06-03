from .models import Session
from .serializers import TutorSessionSerializer, StudentSessionSerializer, ReservedSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db.models.query import QuerySet
from register.models import Tutor, Student
from datetime import datetime
import random
from chat.models import Room


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    permission_classes = [DRYPermissions]

    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #     from django.db import connection
    #     for query in connection.queries:
    #         print("\n", query.get("sql"))
    #     print('\n# of Queries: {}\n'.format(len(connection.queries)))
    #     return response

    def get_serializer_class(self):
        if self.action in ["retrieve", "update", "partial_update"]:
            pk = self.kwargs.get('pk')
            # checks if self.session exists, if not it will call it from the db
            if not hasattr(self, 'session') and self.request.user.has_student:
                self.session = Session.objects.select_related(
                    'tutor', 'tutor__user').get(pk=pk)
            elif not hasattr(self, 'session') and self.request.user.has_tutor:
                self.session = Session.objects.select_related(
                    'student', 'student__user').get(pk=pk)
            if self.session.tutor_pk == self.request.user.tutor_pk:
                return TutorSessionSerializer
            elif self.session.student_pk == self.request.user.student_pk:
                return StudentSessionSerializer
        if self.action == "create":
            return StudentSessionSerializer
        return ReservedSerializer

    def get_object(self):
        if self.action in ["retrieve", "update", "partial_update"]:
            pk = self.kwargs.get('pk')
            # checks if self.session exists, if not it will call it from the db
            if not hasattr(self, 'session') and self.request.user.has_student:
                self.session = Session.objects.select_related(
                    'tutor', 'tutor__user').get(pk=pk)
            elif not hasattr(self, 'session') and self.request.user.has_tutor:
                self.session = Session.objects.select_related(
                    'student', 'student__user').get(pk=pk)
            return self.session
        else:
            return super().get_object()

    def session_view(self, request: HttpRequest, student_queryset: QuerySet, tutor_queryset: QuerySet) -> Response:
        if request.user.has_student:
            session_queryset = student_queryset
        elif request.user.has_tutor:
            session_queryset = tutor_queryset
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="You cannot view your sessions")

        page = self.paginate_queryset(session_queryset)
        if page is not None:
            if request.user.has_student:
                serializer_class = StudentSessionSerializer(page, many=True)
            elif request.user.has_tutor:
                serializer_class = TutorSessionSerializer(page, many=True)
            else:
                serializer_class = ReservedSerializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        if request.user.has_student:
            serializer_class = StudentSessionSerializer(
                session_queryset, many=True)
        elif request.user.has_tutor:
            serializer_class = TutorSessionSerializer(
                session_queryset, many=True)
        else:
            serializer_class = ReservedSerializer(session_queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False)
    def my_sessions(self, request):
        student_queryset = Session.objects.filter(
            student__user=request.user).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def pending_on_tutor(self, request):
        student_queryset = Session.objects.filter(
            student__user=request.user, accepted=False, rejected=False, canceled=False).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, accepted=False, rejected=False, canceled=False).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def pending_on_student_payment(self, request):
        student_queryset = Session.objects.filter(
            student__user=request.user, student_paid=False, canceled=False, accepted=True, free=False).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, student_paid=False, canceled=False, accepted=True, free=False).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def upcoming(self, request):
        student_queryset = Session.objects.filter(
            student__user=request.user, accepted=True, student_paid=True, canceled=False, started=False).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, accepted=True, student_paid=True, canceled=False, started=False).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def tutor_not_paid(self, request):
        student_queryset = Session.objects.filter(
            student__user=request.user, canceled=False, finished=True, tutor_paid=False).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, canceled=False, finished=True, tutor_paid=False).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def past_sessions(self, request):
        student_queryset = Session.objects.filter(
            student__user=request.user, finished=True, tutor_paid=True).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, finished=True, tutor_paid=True).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def finished_sessions(self, request):
        student_queryset = Session.objects.filter(
            student__user=request.user, finished=True).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, finished=True).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def canceled_sessions(self, request):
        student_queryset = Session.objects.filter(
            student__user=request.user, canceled=True).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, canceled=True).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def started_sessions(self, request):
        student_queryset = Session.objects.filter(
            student__user=request.user, started=True, finished=False).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, started=True, finished=False).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    def perform_create(self, serializer):
        data = self.request.data
        tutor = Tutor.objects.select_related("user").get(
            id=int(data.get('tutor')))  # 1 query
        student = Student(id=self.request.user.student_pk,
                          user=self.request.user)
        start = datetime.strptime(data.get("time_start"), "%H:%M")
        end = datetime.strptime(data.get("time_end"), "%H:%M")
        duration = end - start
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        result_str = ''.join(random.choice(letters) for i in range(30))
        if data.get('free', False):
            price = 0
        serializer.save(student=student, student_pk=self.request.user.student_pk,
                        tutor=tutor, tutor_pk=int(data.get('tutor')),
                        duration=duration, call_url=result_str, price=price)  # 2 query

    def perform_update(self, serializer):
        if self.request.data.get('accepted', None):
            tutor = self.request.user.tutor
            tutor_pk = self.request.user.tutor_pk
            student = self.session.student
            student_pk = self.session.student_pk
            Room.objects.get_or_create(
                tutor=tutor, tutor_pk=tutor_pk, student=student, student_pk=student_pk)
            if self.session.free:
                return serializer.save(student_paid=True, tutor_paid=True)
        return serializer.save()
