from .models import User, Tutor, Student, Review
from .serializers import UserOwnerSerializer, UserViewingSerializer, TutorOwnerSerializer, TutorViewingSerializer, StudentOwnerSerializer, StudentViewingSerializer, ReviewSerializer
from .permissions import CanMakeReview

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from dry_rest_permissions.generics import DRYPermissions
from django_auto_prefetching import AutoPrefetchViewSetMixin
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


@api_view(('POST',))
def register_student(request):
    if not request.user.is_authenticated:
        try:
            user_serializer = UserOwnerSerializer(
                data=request.data.get('user'))
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
            user.is_active = False
            user.save()
            student_serializer = StudentOwnerSerializer(
                data=request.data.get('student'))
            student_serializer.is_valid(raise_exception=True)
            student = student_serializer.save(user=user)
        except Exception:
            return Response(data="Invalid data given", status=status.HTTP_400_BAD_REQUEST)

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

        return Response(data=StudentOwnerSerializer(student).data, status=status.HTTP_201_CREATED)
    else:
        return Response(data="You cannot be authenticated while registering", status=status.HTTP_403_FORBIDDEN)


@api_view(('POST',))
def register_tutor(request):
    if not request.user.is_authenticated:
        try:
            user_serializer = UserOwnerSerializer(
                data=request.POST.get('user'))
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer
            user.is_active = False
            user.save()
            tutor_serializer = TutorOwnerSerializer(
                data=request.POST.get('tutor'))
            tutor_serializer.is_valid(raise_exception=True)
            tutor = tutor_serializer.save(user=user)
        except Exception:
            return Response(data="Invalid data given", status=status.HTTP_400_BAD_REQUEST)

        email = user.email
        current_site = get_current_site(request)
        subject = 'Confirm Your Email for TutorPal'
        message = render_to_string('register/emails/confirm-email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })
        send_mail(subject, message, None, [email])

        return Response(data=TutorOwnerSerializer(tutor).data, status=status.HTTP_201_CREATED)
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
    queryset = User.objects.all()
    serializer_class = UserViewingSerializer
    permission_classes = [DRYPermissions]

    @method_decorator(cache_page(60*15))  # may want to edit this
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        pk = self.kwargs['pk']
        if pk == "me" and self.request.user.is_authenticated:
            return self.request.user
        else:
            return super().get_object()

    def get_serializer_class(self):
        if 'pk' in self.kwargs and self.kwargs['pk'] == "me":
            return UserOwnerSerializer
        else:
            return UserViewingSerializer
        # elif self.action == "list":
        #     print("list called")
        #     return UserViewingSerializer
        # elif self.action == "retrieve":
        #     print("retrieve called")
        #     pk = self.request.META.get("PATH_INFO")[7:-1]
        #     try:
        #         if User.objects.get(pk=pk) == self.request.user:
        #             return UserOwnerSerializer
        #     except ObjectDoesNotExist:
        #         return UserViewingSerializer
        #     return UserViewingSerializer
        # return UserOwnerSerializer

    # @action(detail=False, methods=['get', 'patch', 'delete', 'put'])
    # def me(self, request):
    #     self.kwargs['pk'] = request.user.pk
    #     if request.user.is_authenticated:
    #         if request.method == "GET":
    #             return self.retrieve(request)
    #         elif request.method == "PATCH":
    #             return self.partial_update(request)
    #         elif request.method == "PUT":
    #             return self.perform_update(request)
    #         elif request.method == "DELETE":
    #             return self.perform_destroy(request)
    #     else:
    #         return Response(data="You must be authenticated to use this endpoint", status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # token_serializer = MyTokenObtainPairSerializer(
        #     data={'email': request.data.get('email'), 'password': request.data.get('password')})
        # token_serializer.is_valid(raise_exception=True)
        response = Response(data={
            "user": UserOwnerSerializer(user, context=self.get_serializer_context()).data,
            # "access": token_serializer.data.get('access'),
        })
        # response.set_cookie(
        #     'refresh', token_serializer.data.get('refresh'))
        return response

    # def perform_create(self, serilaizer):
    #     login(self.request, self.request.user)


class TutorViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorViewingSerializer
    permission_classes = [DRYPermissions]

    @method_decorator(cache_page(60*15))  # may want to edit this
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        pk = self.kwargs['pk']
        if pk == "me" and hasattr(self.request.user, 'tutor'):
            return self.request.user.tutor
        else:
            return super().get_object()

    def get_serializer_class(self):
        if 'pk' in self.kwargs and self.kwargs['pk'] == "me":
            return TutorOwnerSerializer
        else:
            return TutorViewingSerializer
        # if self.action == "list":
        #     return TutorViewingSerializer
        # elif self.action == "retrieve":
        #     pk = self.kwargs.get('pk')
        #     try:
        #         if Tutor.objects.get(pk=pk).user == self.request.user:
        #             return TutorOwnerSerializer
        #     except ObjectDoesNotExist:
        #         return TutorViewingSerializer
        #     return TutorViewingSerializer
        # return TutorOwnerSerializer

    @action(detail=False, methods=['get', 'patch', 'delete', 'put'])
    def me(self, request):
        self.kwargs['pk'] = request.user.pk
        if request.user.is_authenticated:
            if request.method == "GET":
                return self.retrieve(request)
            elif request.method == "PATCH":
                print("Got here")
                serializer = self.get_serializer(
                    request.user, data=request.data, partial=True)
                print(serializer)
                serializer.is_valid(raise_exception=True)
                return self.perform_update(serializer)
            elif request.method == "PUT":
                print("Got here")
                serializer = self.get_serializer(
                    request.user, data=request.data, partial=False)
                print("Got here")
                print(serializer)
                serializer.is_valid(raise_exception=True)
                print("Got here")
                return self.perform_update(serializer)
            elif request.method == "DELETE":
                return self.perform_destroy(request.user)
        else:
            return Response(data="You must be authenticated to use this endpoint", status=status.HTTP_400_BAD_REQUEST)

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


class StudentViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentViewingSerializer
    permission_classes = [DRYPermissions]

    @method_decorator(cache_page(60*15))  # may want to edit this
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        pk = self.kwargs['pk']
        if pk == "me" and hasattr(self.request.user, 'student'):
            return self.request.user.student
        else:
            return super().get_object()

    def get_serializer_class(self):
        if 'pk' in self.kwargs and self.kwargs['pk'] == "me":
            return StudentOwnerSerializer
        else:
            return StudentViewingSerializer
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


class ReviewViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Review.objects.all()
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
