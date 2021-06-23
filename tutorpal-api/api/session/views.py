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
from paypalpayoutssdk.core import PayPalHttpClient, SandboxEnvironment
from paypalpayoutssdk.payouts import PayoutsPostRequest
from paypalhttp import HttpError
import os
# from django.db.models import F, ExpressionWrapper, DateTimeField


def send_payout(email, price, session_id):
    # Creating Access Token for Sandbox
    client_id = os.environ.get('PAYPAL_CLIENT_ID')
    client_secret = os.environ.get('PAYPAL_CLIENT_SECRET')

    # Creating an environment
    environment = SandboxEnvironment(
        client_id=client_id, client_secret=client_secret)
    client = PayPalHttpClient(environment)

    body = {
        "sender_batch_header": {
            "recipient_type": "EMAIL",
            "email_message": "Your TutorPal Payment",
            "note": "This is your Tutorpal payment",
                    "sender_batch_id": f"Payout_{session_id}",
                    "email_subject": "Your TutorPal Payment"
        },
        "items": [{
            "note": "Your Payout!",
            "amount": {
                "currency": "USD",
                "value": f"{price}"
            },
            "receiver": f"{email}",
            "sender_item_id": "Test_txn_1"
        }]
    }

    request = PayoutsPostRequest()
    request.request_body(body)

    try:
        # Call API with your client and get a response for your call
        response = client.execute(request)
        # If call returns body in response, you can get the deserialized version from the result attribute of the response
        batch_id = response.result.batch_header.payout_batch_id
        # print(batch_id)
        return 'success'
    except IOError as ioe:
        print(ioe)
        if isinstance(ioe, HttpError):
            # Something went wrong server-side
            print(ioe.status_code)
        return 'error'


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

    # @action(detail=False, permission_classes=[IsAuthenticated])
    # def tutor_payment_available(self, request):
    #     # tutor can claim money
    #     # 12 hours after a class ends
    #     date_time_expression = ExpressionWrapper(
    #         F('time_end') + F('date'), output_field=DateTimeField()
    #     )
    #     student_queryset = Session.objects.annotate(
    #         time_end_dt=date_time_expression).filter(
    #         student__user=request.user, canceled=False, finished=True, tutor_paid=False,
    #         free=False, refund_requested=False,
    #         time_end_dt__lt=datetime.now() - timedelta(hours=12)
    #     ).select_related('tutor', 'tutor__user')
    #     tutor_queryset = Session.objects.annotate(
    #         time_end_dt=date_time_expression).filter(
    #         tutor__user=request.user, canceled=False, finished=True, tutor_paid=False,
    #         free=False, refund_requested=False,
    #         time_end_dt__lt=datetime.now() - timedelta(hours=12)
    #     ).select_related('student', 'student__user')
    #     return self.session_view(request, student_queryset, tutor_queryset)

    # @action(detail=False, permission_classes=[IsAuthenticated])
    # def refund_available(self, request):
    #     # student can get a refund
    #     # only available before 12 hours after a class finished
    #     date_time_expression = ExpressionWrapper(
    #         F('time_end') + F('date'), output_field=DateTimeField()
    #     )
    #     student_queryset = Session.objects.annotate(
    #         time_end_dt=date_time_expression).filter(
    #         student__user=request.user, canceled=False, finished=True, tutor_paid=False,
    #         free=False, refund_requested=False,
    #         time_end_dt__gte=datetime.now() - timedelta(hours=12)
    #     ).select_related('tutor', 'tutor__user')
    #     tutor_queryset = Session.objects.annotate(
    #         time_end_dt=date_time_expression).filter(
    #         tutor__user=request.user, canceled=False, finished=True, tutor_paid=False,
    #         free=False, refund_requested=False,
    #         time_end_dt__gte=datetime.now() - timedelta(hours=12)
    #     ).select_related('student', 'student__user')
    #     return self.session_view(request, student_queryset, tutor_queryset)

    @action(detail=True, permission_classes=[IsAuthenticated])
    def pay_tutor(self, request, pk):
        self.get_object()
        if not self.session.tutor_paid and not self.session.free and not self.session.canceled and self.session.finished and not self.session.refund_requested:
            tutor = self.session.tutor
            payout = send_payout(email=tutor.paypal_email if len(tutor.paypal_email) >
                                 0 else tutor.user.email, price=self.session.price, session_id=self.session.id)
            if payout == 'success':
                self.session.tutor_paid = True
                self.session.save()
                return Response(data={'Success': 'Sent payout'}, status=status.HTTP_200_OK)
            else:
                return Response(data={'Error': 'Could not send payout for session'}, status=status.HTTP_403_FORBIDDEN)
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
