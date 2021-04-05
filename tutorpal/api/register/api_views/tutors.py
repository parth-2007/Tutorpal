from ..models import Tutor, User
from ..serializers import UserOwnerSerializer, UserViewingSerializer, TutorOwnerSerializer, TutorViewingSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
from django.contrib.postgres.search import SearchVector
from rest_framework.pagination import PageNumberPagination
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page


class TutorList(APIView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get(self, request, format=None):
        tutors = Tutor.objects.all().select_related('user')
        serializer = TutorViewingSerializer(tutors, many=True)
        return Response(serializer.data)


class TutorDetail(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Tutor.objects.all()
    serializer_class = TutorOwnerSerializer
    # permission_classes = (DRYPermissions,)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get_object(self, pk=None):
        if self.request.user.is_authenticated and pk == "me" and self.request.user.has_tutor:
            return self.request.user.tutor
        elif pk == "me" and not self.request.user.is_authenticated:
            raise Http404
        try:
            return Tutor.objects.select_related('user').get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        # return super().get_object()

    def get(self, request, pk, format=None):
        tutor = self.get_object(pk)
        if request.user.is_authenticated and pk == request.user.tutor_pk:
            serializer = TutorOwnerSerializer(tutor)
        else:
            serializer = TutorViewingSerializer(tutor)
        return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
        # return self.update(request, *args, **kwargs)

    def put(self, request, pk, format=None):
        tutor = self.get_object(pk)
        if tutor == request.user.tutor:
            serializer = TutorOwnerSerializer(tutor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data="You cannot edit this tutor")

    # def patch(self, request, *args, **kwargs):
        # return self.partial_update(request, *args, **kwargs)

    def patch(self, request, pk, format=None):
        tutor = self.get_object(pk)
        if tutor == request.user.tutor:
            serializer = TutorOwnerSerializer(
                tutor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data="You cannot edit this tutor", status=status.HTTP_403_FORBIDDEN)

    # def delete(self, request, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)

    def delete(self, request, pk, format=None):
        tutor = self.get_object(pk)
        if tutor == request.user.tutor:
            tutor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data="You cannot delete this tutor", status=status.HTTP_403_FORBIDDEN)


@api_view()
def user(request, pk):
    from django.db import connection
    if pk == "me":
        serializer = UserOwnerSerializer(request.user)
    else:
        user = User.objects.get(tutor_pk=pk)
        serializer = UserViewingSerializer(user)
    print('# of Queries: {}'.format(len(connection.queries)))
    return Response(data=serializer.data)


# @api_view()
# def search(self, request):
#     query = request.GET.get('q')
#     tutor_query = Tutor.objects.annotate(
#         search=SearchVector('user__first_name', 'user__last_name', 'occupation',
#                             'rates', 'qualifications', 'subjects', 'what_you_teach', 'education')
#     ).filter(search=query)
#     page = PageNumberPagination.paginate_queryset(tutor_query)
#     if page is not None:
#         serializer_class = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer_class.data)

#     serializer_class = self.get_serializer(tutor_query, many=True)
#     return Response(serializer_class.data)


# @api_view()
# def trending(self, request):
#     tutor_query = Tutor.objects.order_by('num_classes', 'average_reviews')
#     page = self.paginate_queryset(tutor_query)
#     if page is not None:
#         serializer_class = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer_class.data)

#     serializer_class = self.get_serializer(tutor_query, many=True)
#     return Response(serializer_class.data)


# @api_view()
# def reviews(self, request, pk):
#     review_query = Review.objects.filter(tutor=pk)
#     page = self.paginate_queryset(review_query)
#     if page is not None:
#         serializer_class = ReviewSerializer(page, many=True)
#         return self.get_paginated_response(serializer_class.data)

#     serializer_class = ReviewSerializer(review_query, many=True)
#     return Response(serializer_class.data)
