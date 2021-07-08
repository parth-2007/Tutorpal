import re

from django.core import exceptions
from .models import Session
from .serializers import TutorSessionSerializer, StudentSessionSerializer, ReservedSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from django.db.models.query import QuerySet
from register.models import Tutor, Student
from datetime import datetime, time, timedelta
from django.utils import timezone
import random
from chat.models import Room
# from django.db.models import F, ExpressionWrapper, DateTimeField
from .payments import send_payout, refund_order, capture_order
# email
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_protect


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
        if self.action in ["retrieve", "update", "partial_update", "pay_tutor"]:
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
        # all the sessions of a user
        student_queryset = Session.objects.filter(
            student__user=request.user).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def pending_on_tutor(self, request):
        # tutor didn't reject/accept yet
        student_queryset = Session.objects.filter(
            student__user=request.user, accepted=False, rejected=False, canceled=False).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, accepted=False, rejected=False, canceled=False).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def pending_on_student_payment(self, request):
        # student didn't pay
        student_queryset = Session.objects.filter(
            student__user=request.user, student_paid=False, canceled=False, accepted=True, free=False).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, student_paid=False, canceled=False, accepted=True, free=False).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def upcoming(self, request):
        # class accepted and paid for by student but not started
        student_queryset = Session.objects.filter(
            student__user=request.user, accepted=True, student_paid=True, canceled=False, started=False).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, accepted=True, student_paid=True, canceled=False, started=False).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def past_sessions(self, request):
        # sessions where tutor was paid
        student_queryset = Session.objects.filter(
            student__user=request.user, finished=True, tutor_paid=True).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, finished=True, tutor_paid=True).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    # @action(detail=False, permission_classes=[IsAuthenticated])
    # def finished_sessions(self, request):
    #     student_queryset = Session.objects.filter(
    #         student__user=request.user, finished=True).select_related('tutor', 'tutor__user')
    #     tutor_queryset = Session.objects.filter(
    #         tutor__user=request.user, finished=True).select_related('student', 'student__user')
    #     return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def canceled_sessions(self, request):
        # sessions that were cancelled
        student_queryset = Session.objects.filter(
            student__user=request.user, canceled=True).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, canceled=True).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def started_sessions(self, request):
        # started sessions
        student_queryset = Session.objects.filter(
            student__user=request.user, started=True, finished=False).select_related('tutor', 'tutor__user')
        tutor_queryset = Session.objects.filter(
            tutor__user=request.user, started=True, finished=False).select_related('student', 'student__user')
        return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=True, permission_classes=[IsAuthenticated])
    def pay_tutor(self, request, pk):
        self.get_object()
        if not self.session.tutor_paid and not self.session.free and not self.session.canceled and self.session.finished:
            tutor = self.session.tutor
            payout = send_payout(email=tutor.paypal_email if len(tutor.paypal_email) >
                                 0 else tutor.user.email, price=self.session.price, session_id=self.session.id)
            if payout == 'success':
                self.session.tutor_paid = True
                self.session.save()
                return Response(data={'Success': 'Sent payout'}, status=status.HTTP_200_OK)
            else:
                return Response(data={'Error': 'There has been an error sending a payout'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(data={'Error': 'Cannot send payout for session'}, status=status.HTTP_403_FORBIDDEN)

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
        else:
            price = data.get('price')
        serializer.save(student=student, student_pk=self.request.user.student_pk,
                        tutor=tutor, tutor_pk=int(data.get('tutor')),
                        duration=duration, call_url=result_str, price=price)  # 2 query
        email = tutor.user.email
        current_site = get_current_site(self.request)
        subject = 'You have a class request'
        message = render_to_string('session/emails/requested.html', {
            'user': tutor.user,
            'domain': current_site.domain,
            'student': student
        })
        send_mail(subject, message, None, [email])

    def perform_update(self, serializer):
        if self.request.data.get('accepted', False):
            tutor = self.request.user.tutor
            tutor_pk = self.request.user.tutor_pk
            student = self.session.student
            student_pk = self.session.student_pk
            Room.objects.get_or_create(
                tutor=tutor, tutor_pk=tutor_pk, student=student, student_pk=student_pk)
            if self.session.free:
                return serializer.save(student_paid=True, tutor_paid=True, accepted=True)
        if self.request.data.get('canceled', False):
            # current_site = get_current_site(self.request)
            subject = 'Your tutoring session has been canceled'
            student_message = render_to_string('session/emails/canceled_student.html', {
                'user': self.session.student.user,
                'tutor': self.session.tutor
                # 'domain': current_site.domain,
            })
            student_mail = (subject, student_message, None, [
                            self.session.student.user.email, self.session.student.parent_email])
            tutor_message = render_to_string('session/emails/canceled_tutor.html', {
                'user': self.session.tutor.user,
                'student': self.session.student
                # 'domain': current_site.domain,
            })
            tutor_mail = (subject, tutor_message, None, [
                          self.session.tutor.user.email])
            send_mass_mail((student_mail, tutor_mail))
            if self.session.student_paid and not self.session.started and not self.session.free and len(self.session.payment_id) > 0:
                refund_order(self.session.payment_id, self.session.price)
                # return super().perform_update(serializer)
        return super().perform_update(serializer)


@csrf_protect
@api_view(('POST',))
def api_capture_order(request, id):
    try:
        order_id = request.data.get('order_id', None)
        if not order_id:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'order id not given'})
        session = Session.objects.get(id=id)
        response = capture_order(order_id)
        if int(response.status_code) == 201:
            session.student_paid = True
            print(response.result.purchase_units[0].payments.captures[0].id)
            session.payment_id = response.result.purchase_units[0].payments.captures[0].id
            session.save()
            return Response(status=status.HTTP_200_OK, data={'success': 'successfully processed payment'})
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'session does not exist'})


@csrf_protect
@api_view()
def finish_session(request, id):
    try:
        session = Session.objects.get(id=id)  # fetch the object
    except exceptions.ObjectDoesNotExist:
        return Response(data={'Error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.user.has_tutor and not session.finished and not session.canceled and request.user.is_authenticated and session.tutor_pk == request.user.tutor_pk:  # you need to be able to end it
        if session.student_joined:  # if student joins they have to wait until 5 mins before the class_end time
            if session.time_end < timezone.now() - timezone.timedelta(minutes=5):
                return Response(status=status.HTTP_403_FORBIDDEN, data={'Error': 'Ending session too early'})
        # if they didn't join they need to wait 20 mins, then they can end
        elif datetime.combine(session.date, session.time_start) + timezone.timedelta(minutes=20) > timezone.make_naive(timezone.now()):
            return Response(status=status.HTTP_403_FORBIDDEN, data={'Error': 'Ending session too early'})
        if not session.tutor_paid and not session.free:  # the session was paid
            tutor = session.tutor
            payout_price = session.price * 0.9651 - 0.49  # paypal fees
            payout = send_payout(email=tutor.paypal_email if len(tutor.paypal_email) >
                                 0 else tutor.user.email, price=payout_price, session_id=session.id)
            if payout == 'success':  # payout was successful
                session.tutor_paid = True
                session.finished = True
                session.save()
                return Response(data={'Success': 'Sent payout and ended session'}, status=status.HTTP_200_OK)
            else:
                session.finished = True
                session.save()
                return Response(data={'Error': 'There has been an error sending a payout, but the session was ended'}, status=status.HTTP_403_FORBIDDEN)
        else:  # session was free
            session.finished = True
            session.save()
            return Response(data={'Success': 'Ended Session'}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(data={'Error': 'You cannot end this session'}, status=status.HTTP_403_FORBIDDEN)
