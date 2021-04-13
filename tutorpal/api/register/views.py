from django.contrib.postgres.search import SearchVector
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.timezone import now
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import permissions, status, viewsets, mixins
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Review, Student, Tutor, User
from .permissions import CanMakeReview
from .serializers import (ReviewSerializer, StudentOwnerSerializer,
                          StudentViewingSerializer, TutorOwnerSerializer,
                          TutorViewingSerializer, UserOwnerSerializer,
                          UserViewingSerializer)
from .tokens import account_activation_token, password_reset_token
import json
from django.contrib.auth import authenticate, login


@api_view(('POST',))
def register_student(request):
    from django.db import connection
    print(request.data)
    try:
        pfp = request.FILES.get("profile_pic")
        data = request.data.get("data")
        user_data = data.get('user')
        password = user_data.pop('password')
        student_data = data.get('student')
        user = User(**user_data)
        user.set_password(password)
        if pfp:
            user.profile_pic = pfp
        student = Student(**student_data)
        user.save()
        student.user = user
        student.save()
        user.student_pk = student.pk
        user.save()
    except Exception as e:
        print("error: ", e)
        raise e

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
    # for query in connection.queries:
    #     print("sql query: ", query.get("sql"))
    # print('# of Queries: {}'.format(len(connection.queries)))
    return response


@api_view(('POST',))
def register_tutor(request):
    from django.db import connection
    try:
        pfp = request.FILES.get("profile_pic")
        data = request.data.get("data")
        user_data = data.get('user')
        password = user_data.pop('password')
        tutor_data = data.get('tutor')
        user = User(**user_data)
        user.set_password(password)
        if pfp:
            user.profile_pic = pfp
        tutor = Tutor(**tutor_data)
        user.save()
        tutor.user = user
        tutor.save()
        user.tutor_pk = tutor.pk
        user.save()
    except Exception as e:
        print("error: ", e)
        raise e

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
    # for query in connection.queries:
    #     print("sql query: ", query.get("sql"))
    # print('# of Queries: {}'.format(len(connection.queries)))
    return response


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

@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({"CSRF":"CSRF Cookie Set"})

@require_POST
def api_login(request):
    data = json.loads(request.body)
    email = data.get("email", None)
    password = data.get("password", None)
    if email is None or password is None:
        return JsonResponse({"errors": "Did not provide an email or password"}, status=400)

    user = authenticate(email=email, password=password)
    if user is None:
        return JsonResponse({"errors": "Invalid email or password"}, status=400)

    login(request, user)
    user_data = UserOwnerSerializer(user).data
    return JsonResponse(user_data)


class UserViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserViewingSerializer
    permission_classes = [DRYPermissions]

    # @method_decorator(cache_page(60*15))  # may want to edit this
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        for query in connection.queries:
            print("sql query: ", query.get("sql"))
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


class TutorViewSet(viewsets.GenericViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin):
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
        ).filter(search=query).select_related('user')
        page = self.paginate_queryset(tutor_query)
        if page is not None:
            serializer_class = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer_class.data)

        serializer_class = self.get_serializer(tutor_query, many=True)
        return Response(serializer_class.data)

    @action(detail=False)
    def trending(self, request):
        tutor_query = Tutor.objects.all().order_by('num_classes', 'average_reviews').select_related('user')
        page = self.paginate_queryset(tutor_query)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = TutorViewingSerializer(tutor_query, many=True)
        return Response(serializer.data)

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


class StudentViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin):
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


class ReviewViewSet(viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    queryset = Review.objects.all().select_related(
        'student', 'student__user', 'tutor')
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CanMakeReview]

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def create(self, request):
        description = request.data.get('description')
        stars = request.data.get('stars')
        try:
            review = Review.objects.get(student__user=request.user, tutor_id=request.data.get('tutor'))
            return Response(status=status.HTTP_403_FORBIDDEN, data="This student has already made a review about the tutor.")
        except ObjectDoesNotExist:
            student = request.user.student
            tutor = Tutor.objects.get(pk=request.data.get('tutor'))
            review = Review.objects.create(tutor=tutor, student=student, stars=stars, description=description)
            review.save()
            tutor.average_reviews = (
                float(tutor.average_reviews) + float(stars)) / (float(tutor.num_reviews) + 1)
            return Response(status=status.HTTP_201_CREATED, data=self.serializer_class(review).data)