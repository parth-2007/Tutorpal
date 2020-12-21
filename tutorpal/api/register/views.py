from .models import User, Tutor, Student, Review
from .serializers import UserOwnerSerializer, UserViewingSerializer, TutorOwnerSerializer, TutorViewingSerializer, StudentOwnerSerializer, StudentViewingSerializer, ReviewSerializer, ChangePasswordSerializer
from rest_framework import permissions, viewsets, status, generics
from .permissions import IsOwnerOrReadOnly, CanMakeObj, CanMakeUser, CanMakeReview, IsUserOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from dry_rest_permissions.generics import DRYPermissions
from django_auto_prefetching import AutoPrefetchViewSetMixin
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.postgres.search import SearchVector


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserViewingSerializer
    permission_classes = [DRYPermissions]

    def get_serializer_class(self):
        if self.action == "list":
            return UserViewingSerializer
        elif self.action == "retrieve":
            pk = self.request.META.get("PATH_INFO")[7:-1]
            try:
                if User.objects.get(pk=pk) == self.request.user:
                    return UserOwnerSerializer
            except ObjectDoesNotExist:
                return UserViewingSerializer
            return UserViewingSerializer
        return UserOwnerSerializer


class TutorViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorViewingSerializer
    permission_classes = [DRYPermissions]

    def get_serializer_class(self):
        if self.action == "list":
            return TutorViewingSerializer
        elif self.action == "retrieve":
            pk = self.request.META.get("PATH_INFO")[8:-1]
            try:
                if Tutor.objects.get(pk=pk).user == self.request.user:
                    return TutorOwnerSerializer
            except ObjectDoesNotExist:
                return TutorViewingSerializer
            return TutorViewingSerializer
        return TutorOwnerSerializer

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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StudentViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentViewingSerializer
    permission_classes = [DRYPermissions]

    def get_serializer_class(self):
        if self.action == "list":
            return StudentViewingSerializer
        elif self.action == "retrieve":
            pk = self.request.META.get("PATH_INFO")[10:-1]
            try:
                if Student.objects.get(pk=pk).user == self.request.user:
                    return StudentOwnerSerializer
            except ObjectDoesNotExist:
                return StudentViewingSerializer
            return StudentViewingSerializer
        return StudentOwnerSerializer

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
            return Response(status=status.HTTP_201_CREATED, data=serializer_class(review).data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data="This student has already made a review about the tutor.")


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated, DRYPermissions)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
