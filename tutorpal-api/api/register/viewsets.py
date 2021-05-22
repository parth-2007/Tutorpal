from django.contrib.postgres.search import SearchVector
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import permissions, status, viewsets, mixins, filters
from rest_framework.response import Response
from .models import Review, Student, Tutor, User
from .permissions import CanMakeReview
from .serializers import (ReviewSerializer, StudentOwnerSerializer,
                          StudentViewingSerializer, TutorOwnerSerializer,
                          TutorViewingSerializer, UserOwnerSerializer,
                          UserViewingSerializer)
from rest_framework.decorators import action


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
            print("\nsql query: ", query.get("sql"))
        print('\n# of Queries: {}\n'.format(len(connection.queries)))
        return response

    def get_object(self):
        # print("# get_object() called")
        if self.action in ["retrieve", "update", "partial_update"]:
            pk = self.kwargs['pk']
            if pk == "me" and self.request.user.is_authenticated:
                return self.request.user
        return super().get_object()

    def get_serializer_class(self):
        # print("# get_serializer_class() called")
        if 'pk' in self.kwargs and self.kwargs['pk'] == 'me':
            return UserOwnerSerializer
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
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Tutor.objects.all().select_related('user')
    serializer_class = TutorViewingSerializer
    permission_classes = [DRYPermissions]

    filter_backends = (filters.OrderingFilter,)
    ordering = ('-average_reviews', '-num_reviews', '-num_classes')

    # @method_decorator(cache_page(60*15))  # may want to edit this
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        # for query in connection.queries:
        #     print("sql query: ", query.get("sql"))
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get_object(self):
        if self.action in ["retrieve", "update", "partial_update"]:
            pk = self.kwargs['pk']
            if self.request.user.is_authenticated and pk == "me" and self.request.user.has_tutor:
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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

    def rank(self, scope):
        rankings = {}
        for tutor in scope:
            conversions = {"High School": 1, "Bachelors Degree": 2,
                           "Masters Degree": 3, "Ph.D.": 4}
            education = conversions.get(tutor.education)
            if tutor.average_reviews < 1:
                average = 2.5
            else:
                average = tutor.average_reviews
            if tutor.num_classes < 1:
                num_classes = 1
            else:
                num_classes = tutor.num_classes
            rankings[tutor] = (average * 0.75) * \
                (education * 0.25) * (num_classes * 0.75)
            rankings = {k: v for k, v in sorted(
                rankings.items(), key=lambda item: item[1], reverse=True)}
        return rankings

    @action(detail=False)
    def trending(self, request):
        tutor_query = Tutor.objects.order_by(
            'num_classes', 'average_reviews', 'num_reviews').select_related('user')
        print(tutor_query)
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


class StudentViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Student.objects.all().select_related('user')
    # serializer_class = StudentViewingSerializer
    permission_classes = [DRYPermissions]

    # @method_decorator(cache_page(60*15))  # may want to edit this
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        # for query in connection.queries:
        #     print("sql query: ", query.get("sql"))
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get_object(self):
        if self.action in ["retrieve", "update", "partial_update"]:
            pk = self.kwargs['pk']
            if pk == "me" and self.request.user.has_student:
                return self.request.user.student
            else:
                return super().get_object()
        else:
            return super().get_object()

    def get_serializer_class(self):
        if 'pk' in self.kwargs and self.kwargs['pk'] == "me" and self.request.method == "GET":
            return StudentOwnerSerializer
        else:
            return StudentViewingSerializer

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
        for query in connection.queries:
            print("sql query: ", query.get("sql"))
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def create(self, request):
        description = request.data.get('description')
        stars = request.data.get('stars')
        tutor_id = request.data.get('tutor')
        try:
            review = Review.objects.get(
                student__user=request.user, tutor_id=tutor_id)  # 1 query
            return Response(status=status.HTTP_403_FORBIDDEN, data="This student has already made a review about the tutor.")
        except Review.DoesNotExist:
            # student = request.user.student
            student = Student(id=request.user.student_pk, user=request.user)
            tutor = Tutor.objects.get(pk=request.data.get('tutor'))  # 2 query
            review = Review.objects.create(
                tutor=tutor, student=student, stars=stars, description=description)  # 3 query
            tutor.average_reviews = (
                float(tutor.average_reviews) + float(stars)) / (float(tutor.num_reviews) + 1)
            tutor.save()  # 4 query
            return Response(status=status.HTTP_201_CREATED, data=self.serializer_class(review).data)
