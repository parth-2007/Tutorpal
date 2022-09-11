import os
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail, send_mass_mail
from .payments import send_payout, refund_order, capture_order
from chat.models import Room
from register.permissions import IsStudent, IsTutor
import math
import random
from django.utils import timezone
from datetime import datetime, timedelta
from register.models import Tutor, Student
from django.db.models.query import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import TutorSessionSerializer, StudentSessionSerializer, ReservedSerializer, StudentSeminarSerializer, TutorSeminarSerializer
from .models import Session, Seminar, StudentSeminar
from django.core import exceptions
# from django.db.models import F, ExpressionWrapper, DateTimeFielde


class SeminarViewSet(viewsets.ModelViewSet):
    queryset = Seminar.objects.all()
    permission_classes = [DRYPermissions]

    def get_serializer_class(self):
        if self.action == "list":
            return StudentSeminarSerializer
        if self.request.user.is_authenticated and self.request.user.has_tutor:
            return TutorSeminarSerializer
        return StudentSeminarSerializer

    @action(detail=False, permission_classes=[IsAuthenticated])
    def my_seminars(self, request):
        if request.user.has_tutor:
            queryset = Seminar.objects.filter(
                tutor_pk=self.request.user.tutor_pk)
        else:
            queryset = Seminar.objects.filter(
                studentseminar__student=request.user.student)
        page = self.paginate_queryset(queryset)
        if page is not None:
            if request.user.has_tutor:
                serializer_class = TutorSeminarSerializer(page, many=True)
            else:
                serializer_class = StudentSeminarSerializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        if request.user.has_tutor:
            serializer_class = TutorSeminarSerializer(page, many=True)
        else:
            serializer_class = StudentSeminarSerializer(page, many=True)
        return Response(serializer_class.data)

    @action(detail=False, permission_classes=[IsStudent])
    def discover_seminars(self, request):
        queryset = Seminar.objects.exclude(
            studentseminar__student=request.user.student)
        page = self.paginate_queryset(queryset)
        if page is not None:
            if request.user.has_tutor:
                serializer_class = TutorSeminarSerializer(page, many=True)
            else:
                serializer_class = StudentSeminarSerializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        if request.user.has_tutor:
            serializer_class = TutorSeminarSerializer(page, many=True)
        else:
            serializer_class = StudentSeminarSerializer(page, many=True)
        return Response(serializer_class.data)

    @action(methods=['POST'], detail=True, permission_classes=[IsStudent])
    def register(self, request, pk):
        seminar = Seminar.objects.get(pk=pk)
        if seminar.sessions_completed == len(seminar.times):
            return Response(data={'error': 'too late to register'}, status=status.HTTP_403_FORBIDDEN)
        try:
            StudentSeminar.objects.get(
                student__pk=request.user.student_pk, seminar=seminar)
            return Response(data={'error': 'already registered'}, status=status.HTTP_403_FORBIDDEN)
        except StudentSeminar.DoesNotExist:
            if seminar.free:
                StudentSeminar.objects.create(
                    student=request.user.student, seminar=seminar)
                seminar.student_number = seminar.student_number + 1
                seminar.save()
                return Response(data={'success': 'added student'}, status=status.HTTP_200_OK)
            else:
                order_id = request.data.get('order_id', None)
                if not order_id:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'order id not given'})
                seminar = Seminar.objects.get(pk=pk)
                response = capture_order(order_id)
                if int(response.status_code) == 201:
                    # print(response.result.purchase_units[0].payments.captures[0].id)
                    payment_id = response.result.purchase_units[0].payments.captures[0].id
                    StudentSeminar.objects.create(
                        student=request.user.student, seminar=seminar, payment_id=payment_id)
                    seminar.student_number = seminar.student_number + 1
                    seminar.save()
                    return Response(status=status.HTTP_200_OK, data={'success': 'successfully processed payment and added student'})
                else:
                    return Response(status=status.HTTP_200_OK, data={'error': 'payment did not process correctly'})

    @action(methods=['POST'], detail=True, permission_classes=[IsStudent])
    def unregister(self, request, pk):
        seminar = Seminar.objects.get(pk=pk)
        student_seminar = StudentSeminar.objects.get(
            student=request.user.student, seminar=seminar)
        if seminar.payouts > 1 or seminar.sessions_completed == len(seminar.times):
            return Response(data={'error': 'too late to unregister'}, status=status.HTTP_400_BAD_REQUEST)
        if not seminar.free and seminar.price > 0:
            payment_id = student_seminar.payment_id
            refund_order(payment_id, seminar.price)
        student_seminar.delete()
        seminar.student_number = seminar.student_number - 1
        seminar.save()
        return Response(data={'success': 'removed student'}, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True, permission_classes=[IsTutor])
    def start(self, request, pk):
        seminar = Seminar.objects.get(pk=pk)
        if seminar.tutor_pk == request.user.tutor_pk:
            seminar.active = True
            seminar.save()
            emails = StudentSeminar.objects.filter(
                seminar=seminar).values_list('student__user__email', flat=True)
            if os.environ.get('RUN_ENV', 'local') == 'aws_prod':
                domain = 'https://www.tutorpal.org/'
            elif os.environ.get('RUN_ENV', 'local') == 'aws_dev':
                domain = 'https://beta.tutorpal.org/'
            else:
                domain = get_current_site(self.request).domain
            subject = 'Your seminar has started'
            message = render_to_string('seminar/emails/started_seminar.html', {
                'tutor_user': seminar.tutor.user,
                'domain': domain,
                'seminar_id': seminar.id
            })
            send_mail(subject, message, settings.EMAIL_FROM, list(emails))
            return Response(data={'success': 'started seminar'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': 'invalid seminar'}, status=status.HTTP_403_FORBIDDEN)

    @action(methods=['POST'], detail=True, permission_classes=[IsTutor])
    def finish(self, request, pk):
        seminar = Seminar.objects.get(pk=pk)
        # check if able to end session
        if request.user.has_tutor and seminar.active and seminar.tutor_pk == request.user.tutor_pk:  # you need to be able to end it
            # the seminar was paid
            if not seminar.payouts == 2 and not seminar.free and (seminar.payouts == 0 or (seminar.payouts == 1 and seminar.sessions_completed == len(seminar.times) - 1)):
                payout_price = math.floor(
                    ((float(seminar.student_number * seminar.price / 2) * 0.9151) - 0.49) * 100) / 100  # paypal fee is 3.49% + $0.49, our fee is 5%
                tutor = seminar.tutor
                tutor.num_classes = tutor.num_classes + 1
                tutor.save()
                # paypal fees and round
                if payout_price > 0:
                    payout = send_payout(email=tutor.paypal_email if len(
                        tutor.paypal_email) > 0 else tutor.user.email, price=payout_price, session_id="seminar" + str(seminar.id))
                    if payout == 'success':  # payout was successful
                        seminar.payouts = seminar.payouts + 1
                        seminar.active = False
                        seminar.sessions_completed = seminar.sessions_completed + 1
                        seminar.save()
                        return Response(data={'Success': 'Sent payout and ended session'}, status=status.HTTP_200_OK)
                    else:
                        seminar.active = False
                        seminar.sessions_completed = seminar.sessions_completed + 1
                        seminar.save()
                        return Response(data={'Error': 'There has been an error sending a payout, but the session was ended'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    seminar.active = False
                    seminar.sessions_completed = seminar.sessions_completed + 1
                    seminar.save()
                    return Response(data={'Error': 'Session was ended, no payout was sent because paypal fees dropped it to $0 or there were no students'}, status=status.HTTP_200_OK)
            else:  # session was free
                tutor = seminar.tutor
                tutor.num_classes = tutor.num_classes + 1
                tutor.free_tutoring_given = tutor.free_tutoring_given + seminar.duration
                tutor.save()
                seminar.sessions_completed = seminar.sessions_completed + 1
                seminar.active = False
                seminar.save()
                return Response(data={'Success': 'Ended Session'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'Error': 'You cannot end this session'}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, permission_classes=[IsStudent])
    def join_seminar(self, request, pk):
        seminar = Seminar.objects.get(pk=pk)
        try:
            StudentSeminar.objects.get(
                student=request.user.student, seminar=seminar)
            return Response(data={'url': seminar.call_url}, status=status.HTTP_200_OK)
        except StudentSeminar.DoesNotExist:
            return Response(data={'error': 'you are not in this seminar'}, status=status.HTTP_403_FORBIDDEN)


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    permission_classes = [DRYPermissions]
    # permission_classes = []

    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #     from django.db import connection
    #     for query in connection.queries:
    #         print("\n", query.get("sql"))
    #     print('\n# of Queries: {}\n'.format(len(connection.queries)))
    #     return response

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
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
            elif self.action == "create":
                return StudentSessionSerializer
        return ReservedSerializer

    def get_object(self):
        if self.action in ["retrieve", "update", "partial_update", "pay_tutor"]:
            pk = self.kwargs.get('pk')
            # checks if self.session exists, if not it will call it from the db
            if self.request.user.is_authenticated:
                if not hasattr(self, 'session') and self.request.user.has_tutor:
                    self.session = Session.objects.select_related(
                        'student', 'student__user').get(pk=pk)
                elif not hasattr(self, 'session') and self.request.user.has_student:
                    self.session = Session.objects.select_related(
                        'tutor', 'tutor__user').get(pk=pk)
            else:
                if not hasattr(self, 'session'):
                    self.session = Session.objects.get(pk=pk)
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

    # @action(detail=True, permission_classes=[IsAuthenticated])
    # def pay_tutor(self, request, pk):
    #     self.get_object()
    #     if not self.session.tutor_paid and not self.session.free and not self.session.canceled and self.session.finished:
    #         tutor = self.session.tutor
    #         payout = send_payout(email=tutor.paypal_email if len(tutor.paypal_email) >
    #                              0 else tutor.user.email, price=self.session.price, session_id=self.session.id)
    #         if payout == 'success':
    #             self.session.tutor_paid = True
    #             self.session.save()
    #             return Response(data={'Success': 'Sent payout'}, status=status.HTTP_200_OK)
    #         else:
    #             return Response(data={'Error': 'There has been an error sending a payout'}, status=status.HTTP_403_FORBIDDEN)
    #     else:
    #         return Response(data={'Error': 'Cannot send payout for session'}, status=status.HTTP_403_FORBIDDEN)

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
            free = True
        else:
            price = data.get('price')
            free = False
        if data.get('price', 0) == 0:
            free = True
        serializer.save(student=student, student_pk=self.request.user.student_pk,
                        tutor=tutor, tutor_pk=int(data.get('tutor')),
                        duration=duration, call_url=result_str, price=price, free=free)  # 2 query
        email = tutor.user.email
        if os.environ.get('RUN_ENV', 'local') == 'aws_prod':
            domain = 'https://www.tutorpal.org/'
        elif os.environ.get('RUN_ENV', 'local') == 'aws_dev':
            domain = 'https://beta.tutorpal.org/'
        else:
            domain = get_current_site(self.request).domain
        subject = 'You have a class request'
        message = render_to_string('session/emails/requested.html', {
            'user': tutor.user,
            'domain': domain,
            'student': student
        })
        send_mail(subject, message, settings.EMAIL_FROM, [email])

    def perform_update(self, serializer):
        if self.request.data.get('accepted', False):
            if self.request.user.has_tutor:
                tutor = self.request.user.tutor
                tutor_pk = self.request.user.tutor_pk
                student = self.session.student
                student_pk = self.session.student_pk
                Room.objects.get_or_create(
                    tutor=tutor, tutor_pk=tutor_pk, student=student, student_pk=student_pk)
                email = student.user.email
                if os.environ.get('RUN_ENV', 'local') == 'aws_prod':
                    domain = 'https://www.tutorpal.org/'
                elif os.environ.get('RUN_ENV', 'local') == 'aws_dev':
                    domain = 'https://beta.tutorpal.org/'
                else:
                    domain = get_current_site(self.request).domain
                subject = 'Your class request has been accepted'
                message = render_to_string('session/emails/accepted.html', {
                    'tutor_user': tutor.user,
                    'domain': domain,
                    'student_user': student.user
                })
                send_mail(subject, message, settings.EMAIL_FROM, [email])
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
            student_mail = (subject, student_message, settings.EMAIL_FROM, [
                            self.session.student.user.email, self.session.student.parent_email])
            tutor_message = render_to_string('session/emails/canceled_tutor.html', {
                'user': self.session.tutor.user,
                'student': self.session.student
                # 'domain': current_site.domain,
            })
            tutor_mail = (subject, tutor_message, settings.EMAIL_FROM, [
                          self.session.tutor.user.email])
            send_mass_mail((student_mail, tutor_mail))
            if self.session.student_paid and not self.session.started and not self.session.free and len(self.session.payment_id) > 0:
                refund_order(self.session.payment_id, self.session.price)
                # return super().perform_update(serializer)
        return super().perform_update(serializer)


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
            # print(response.result.purchase_units[0].payments.captures[0].id)
            session.payment_id = response.result.purchase_units[0].payments.captures[0].id
            session.save()
            return Response(status=status.HTTP_200_OK, data={'success': 'successfully processed payment'})
        else:
            return Response(status=status.HTTP_200_OK, data={'error': 'payment did not process correctly'})
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'session does not exist'})


@api_view(('POST',))
def finish_session(request, id):
    try:
        session = Session.objects.get(id=id)  # fetch the object
    except exceptions.ObjectDoesNotExist:
        return Response(data={'Error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.user.has_tutor and not session.finished and not session.canceled and request.user.is_authenticated and session.tutor_pk == request.user.tutor_pk and session.started:  # you need to be able to end it
        if session.student_joined:  # if student joins they have to wait until 5 mins before the class_end time
            if datetime.combine(session.date, session.time_end) - timedelta(minutes=5) > timezone.make_naive(timezone.now()):
                return Response(status=status.HTTP_403_FORBIDDEN, data={'Error': 'Ending session too early'})
        # if they didn't join they need to wait 20 mins, then they can end
        elif datetime.combine(session.date, session.time_start) + timezone.timedelta(minutes=20) > timezone.make_naive(timezone.now()) or datetime.combine(session.date, session.time_end) - timedelta(minutes=5) > timezone.make_naive(timezone.now()):
            return Response(status=status.HTTP_403_FORBIDDEN, data={'Error': 'Ending session too early'})
        if not session.tutor_paid and not session.free:  # the session was paid
            tutor = session.tutor
            tutor.num_classes = tutor.num_classes + 1
            tutor.save()
            # paypal fees and round
            payout_price = math.floor(
                ((float(session.price) * 0.9151) - 0.49) * 100) / 100
            if payout_price > 0:
                payout = send_payout(email=tutor.paypal_email if len(
                    tutor.paypal_email) > 0 else tutor.user.email, price=payout_price, session_id=session.id)
                if payout == 'success':  # payout was successful
                    session.tutor_paid = True
                    session.finished = True
                    session.save()
                    return Response(data={'Success': 'Sent payout and ended session'}, status=status.HTTP_200_OK)
                else:
                    session.finished = True
                    session.save()
                    return Response(data={'Error': 'There has been an error sending a payout, but the session was ended'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                session.finished = True
                session.save()
                return Response(data={'Error': 'Session was ended, no payout was sent because paypal fees dropped it to $0'}, status=status.HTTP_200_OK)
        else:  # session was free
            tutor = session.tutor
            tutor.num_classes = tutor.num_classes + 1
            tutor.free_tutoring_given = tutor.free_tutoring_given + session.duration
            tutor.save()
            session.finished = True
            session.save()
            return Response(data={'Success': 'Ended Session'}, status=status.HTTP_200_OK)
    else:
        return Response(data={'Error': 'You cannot end this session'}, status=status.HTTP_403_FORBIDDEN)


# @api_view()
# def test_payout(request):
#     print('making the request')
#     payout_price = 1.59
#     payout = send_payout(
#         email="sb-ysvrf3397194@personal.example.com", price=payout_price, session_id='test1')
#     if payout == 'success':  # payout was successful
#         return Response(data={'Success': 'Sent payout'}, status=status.HTTP_200_OK)
#     else:
#         return Response(data={'Error': 'There has been an error sending a payout'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
