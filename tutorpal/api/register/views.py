from .models import User, Tutor, Student, Review
from .serializers import UserOwnerSerializer, UserViewingSerializer, TutorOwnerSerializer, TutorViewingSerializer, StudentOwnerSerializer, StudentViewingSerializer, ReviewSerializer
from .permissions import CanMakeReview

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from dry_rest_permissions.generics import DRYPermissions
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action, api_view
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render
from django.utils.timezone import now
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token, password_reset_token
from django.utils.encoding import force_text
from django.core.mail import send_mail
# from django.http import HttpRequest
# import pytz


@api_view(('POST',))
def register_student(request):
    if not request.user.is_authenticated:
        try:
            user_serializer = UserOwnerSerializer(
                data=request.data.get('user'))
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
            user.is_active = False
            student_serializer = StudentOwnerSerializer(
                data=request.data.get('student'))
            student_serializer.is_valid(raise_exception=True)
            student = student_serializer.save(user=user)
            user.student_id = student.id
        except Exception as e:
            raise e
            # return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

        email = user.email
        current_site = get_current_site(request)
        subject = 'Confirm Your Email for TutorPal'
        message = render_to_string('register/emails/confirm_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })
        send_mail(subject, message, None, [email])

        response = Response(data=StudentOwnerSerializer(
            student).data, status=status.HTTP_201_CREATED)
        # tz_name = request.data.get('tz_name')
        # if tz_name in pytz.all_timezones:
        #     response.set_cookie('tz_name', tz_name)
        return response
    else:
        return Response(data="You cannot be authenticated while registering", status=status.HTTP_403_FORBIDDEN)


@api_view(('POST',))
def register_tutor(request):
    if not request.user.is_authenticated:
        req_data = request.data
        req_data['average_reviews'] = 0.0
        try:
            user_serializer = UserOwnerSerializer(
                data=req_data.get('user'))
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
            user.is_active = False
            tutor_serializer = TutorOwnerSerializer(
                data=req_data.get('tutor'))
            tutor_serializer.is_valid(raise_exception=True)
            tutor = tutor_serializer.save(user=user)
            user.tutor_id = tutor.id
        except Exception as e:
            raise e
            # return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

        email = user.email
        current_site = get_current_site(request)
        subject = 'Confirm Your Email for TutorPal'
        message = render_to_string('register/emails/confirm_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })
        send_mail(subject, message, None, [email])

        response = Response(data=TutorOwnerSerializer(
            tutor).data, status=status.HTTP_201_CREATED)
        # tz_name = request.data.get('tz_name')
        # if tz_name in pytz.all_timezones:
        #     response.set_cookie('tz_name', tz_name)
        return response
    else:
        return Response(data="You cannot be authenticated while registering", status=status.HTTP_403_FORBIDDEN)


@api_view()
def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return Response(data="Invalid credentials provided", status=status.HTTP_400_BAD_REQUEST)

    if account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response(data="Successfully activated account", status=status.HTTP_200_OK)
    else:
        return Response(data="Invalid credentials provided", status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
def reset_password(request):
    try:
        email = request.data.get("email")
        print(email)
        user = User.objects.get(email=email)
    except (AttributeError, User.DoesNotExist):
        return Response(data="Invalid email", status=status.HTTP_400_BAD_REQUEST)

    current_site = get_current_site(request)
    subject = 'Confirm Your Email for TutorPal'
    message = render_to_string('register/emails/reset_password.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': password_reset_token.make_token(user)
    })
    send_mail(subject, message, None, [email])

    return Response('Sent email', status.HTTP_200_OK)


@api_view(('POST',))
def password_reset(request, uidb64, token):
    try:
        password = request.data.get('password')
    except AttributeError:
        return Response(data="New password not provided", status=status.HTTP_400_BAD_REQUEST)

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return Response(data="Invalid credentials provided", status=status.HTTP_400_BAD_REQUEST)

    if user is not None and password_reset_token.check_token(user, token):
        user.set_password(password)
        user.last_reset = now()
        user.save()
        return Response(data="Successfully changed password", status=status.HTTP_200_OK)
    else:
        return Response(data="Invalid credentials provided", status=status.HTTP_400_BAD_REQUEST)


def test(request):
    return render(request, 'register/index.html')


def get_trending():
    tutors = Tutor.objects.order_by('num_classes', 'average_reviews')
    return tutors


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('student', 'tutor')
    serializer_class = UserViewingSerializer
    permission_classes = [DRYPermissions]

    # @method_decorator(cache_page(60*15))  # may want to edit this
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get_object(self):
        # print("# get_object() called")
        if self.action in ["retrieve", "update", "partial_update"]:
            pk = self.kwargs['pk']
            if pk == "me" and self.request.user.is_authenticated:
                return self.request.user
            else:
                return super().get_object()
        else:
            return super().get_object()

    def get_serializer_class(self):
        # print("# get_serializer_class() called")
        if 'pk' in self.kwargs and self.kwargs['pk'] == 'me':
            return UserOwnerSerializer
        else:
            return super().get_serializer_class()

    @action(detail=True)
    def student(self, request, pk):
        if self.request.user.has_student:
            if pk == self.request.user.pk:
                serializer = StudentOwnerSerializer(request.user.student)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                serializer = StudentViewingSerializer(request.user.student)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data="User has no Student", status=status.HTTP_404_NOT_FOUND)

    @action(detail=True)
    def tutor(self, request, pk):
        if self.request.user.has_tutor:
            if pk == "me":
                serializer = TutorOwnerSerializer(request.user.tutor)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                serializer = TutorViewingSerializer(request.user.tutor)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data="User has no Tutor", status=status.HTTP_404_NOT_FOUND)


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all().select_related('user')
    serializer_class = TutorViewingSerializer
    permission_classes = [DRYPermissions]

    # @method_decorator(cache_page(60*15))  # may want to edit this
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get_object(self):
        # print("# get_object() called")
        # pk = self.kwargs['pk']
        # if pk == "me" and hasattr(self.request.user, 'tutor'):
        #     return self.request.user.tutor
        # if self.action == "update" or self.action == "partial_update":
        #     if pk == "me" and hasattr(self.request.user, 'tutor'):
        #         return self.request.user.tutor
        # else:
        #     return super().get_object()
        if self.action in ["retrieve", "update", "partial_update"]:
            pk = self.kwargs['pk']
            if pk == "me" and self.request.user.has_tutor:
                return self.request.user.tutor
            else:
                return super().get_object()
        else:
            return super().get_object()

    def get_serializer_class(self):
        if 'pk' in self.kwargs and self.kwargs['pk'] == "me":
            return TutorOwnerSerializer
        else:
            return super().get_serializer_class()

    @action(detail=False)
    def search(self, request):
        query = request.GET.get('q')
        tutor_query = Tutor.objects.annotate(
            search=SearchVector('user__first_name', 'user__last_name', 'occupation',
                                'rates', 'qualifications', 'subjects', 'what_you_teach', 'education')
        ).filter(search=query)
        page = self.paginate_queryset(tutor_query)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(tutor_query, many=True)
        return Response(serializer_class.data)

    @action(detail=False)
    def trending(self, request):
        tutor_query = get_trending()
        page = self.paginate_queryset(tutor_query)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(tutor_query, many=True)
        return Response(serializer_class.data)

    @action(detail=True)
    def reviews(self, request, pk):
        review_query = Review.objects.filter(tutor=pk)
        page = self.paginate_queryset(review_query)
        if page is not None:
            serializer_class = ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = ReviewSerializer(review_query, many=True)
        return Response(serializer_class.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().select_related('user')
    serializer_class = StudentViewingSerializer
    permission_classes = [DRYPermissions]

    # @method_decorator(cache_page(60*15))  # may want to edit this
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get_object(self):
        # pk = self.kwargs['pk']
        # if pk == "me" and hasattr(self.request.user, 'student'):
        #     return self.request.user.student
        # else:
        #     return super().get_object()
        if self.action in ["retrieve", "update", "partial_update"]:
            pk = self.kwargs['pk']
            if pk == "me" and self.request.user.has_student:
                return self.request.user.student
            else:
                return super().get_object()
        else:
            return super().get_object()

    def get_serializer_class(self):
        if 'pk' in self.kwargs and self.kwargs['pk'] == "me":
            return StudentOwnerSerializer
        else:
            return super().get_serializer_class()
        # if self.action == "list":
        #     return StudentViewingSerializer
        # elif self.action == "retrieve":
        #     pk = self.request.META.get("PATH_INFO")[10:-1]
        #     try:
        #         if Student.objects.get(pk=pk).user == self.request.user:
        #             return StudentOwnerSerializer
        #     except ObjectDoesNotExist:
        #         return StudentViewingSerializer
        #     return StudentViewingSerializer
        # return StudentOwnerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().select_related(
        'student', 'student__user', 'tutor')
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CanMakeReview]

    def create(self, request):
        tutor = Tutor.objects.get(pk=request.data.get('tutor'))
        student = request.user.student
        description = request.data.get('description')
        stars = request.data.get('stars')
        if not Review.objects.filter(student=student, tutor=tutor).exists():
            review = Review(tutor=tutor, student=student,
                            stars=stars, description=description)
            review.save()
            tutor.average_reviews = (
                float(tutor.average_reviews) + float(stars)) / (float(tutor.num_reviews) + 1)
            return Response(status=status.HTTP_201_CREATED, data=self.serializer_class(review).data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="This student has already made a review about the tutor.")
