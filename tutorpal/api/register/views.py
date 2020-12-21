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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserViewingSerializer
    # permission_classes = [CanMakeUser, IsUserOrReadOnly]
    permission_classes = [DRYPermissions]

    # Add change password method

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

    # def list(self, request):
    #     # disable later
    #     queryset = User.objects.all()
    #     serializer_class = UserViewingSerializer(queryset, many=True)
    #     permission_classes = [DRYPermissions]
    #     return Response(serializer_class.data)
    #     # return Response(data="Listing for users not available", status=status.HTTP_403_FORBIDDEN)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     permission_classes = [DRYPermissions]
    #     if request.user == user:
    #         serializer_class = UserOwnerSerializer(user)
    #         return Response(serializer_class.data)
    #     else:
    #         serializer_class = UserViewingSerializer(user)
    #         return Response(serializer_class.data)


class TutorViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorViewingSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, CanMakeObj]
    permission_classes = [DRYPermissions]

    # def list(self, request):
    #     # Keep for search
    #     queryset = Tutor.objects.all()
    #     serializer_class = TutorViewingSerializer(queryset, many=True)
    #     permission_classes = [DRYPermissions]
    #     return Response(serializer_class.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Tutor.objects.all()
    #     tutor = get_object_or_404(queryset, pk=pk)
    #     permission_classes = [DRYPermissions]
    #     if request.user == tutor.user:
    #         serializer_class = TutorOwnerSerializer(tutor)
    #         return Response(serializer_class.data)
    #     else:
    #         serializer_class = TutorViewingSerializer(tutor)
    #         return Response(serializer_class.data)

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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StudentViewSet(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentViewingSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, CanMakeObj]
    permission_classes = [DRYPermissions]

    # def list(self, request):
    #     # disable
    #     queryset = Student.objects.all()
    #     serializer_class = StudentViewingSerializer(queryset, many=True)
    #     permission_classes = [DRYPermissions]
    #     return Response(serializer_class.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Student.objects.all()
    #     student = get_object_or_404(queryset, pk=pk)
    #     permission_classes = [DRYPermissions]
    #     if request.user == student.user:
    #         serializer_class = StudentOwnerSerializer(student)
    #         return Response(serializer_class.data)
    #     else:
    #         serializer_class = StudentViewingSerializer(student)
    #         return Response(serializer_class.data)

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

    # def list(self, request):
    # return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data="Listing not available")

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

    # def perform_create(self, serializer):
    # 	student = self.request.user.student
    # 	serializer.save(student=self.request.user.student)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
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
