from typing import Union
from ..models import User
from ..serializers import UserOwnerSerializer, UserViewingSerializer, TutorOwnerSerializer, TutorViewingSerializer, StudentOwnerSerializer, StudentViewingSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import mixins
from django.http import HttpRequest
from rest_framework.pagination import PageNumberPagination
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page


def get_object(request: HttpRequest, pk: Union[int, str]) -> Union[User, Http404]:
    if pk == "me" and request.user.is_authenticated:
        return request.user
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404


class UserList(generics.GenericAPIView):
    queryset = User.objects.all()
    pagination_class = PageNumberPagination

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get(self, request, format=None):
        queryset = User.objects.all()
        page = request.query_params.get('page')
        if page is not None:
            paginate_queryset = self.paginate_queryset(queryset)
            serializer = UserViewingSerializer(paginate_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = UserViewingSerializer(queryset, many=True)
        return Response(serializer.data)


class UserDetail(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    # queryset = User.objects.all()
    serializer_class = UserOwnerSerializer
    # permission_classes = (DRYPermissions,)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get_object(self, pk=None):
        return get_object(self.request, pk)
        # return super().get_object()

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        if user == request.user:
            serializer = UserOwnerSerializer(user)
        else:
            serializer = UserViewingSerializer(user)
        return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
        # return self.update(request, *args, **kwargs)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        if user == request.user:
            serializer = UserOwnerSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data="You cannot edit this user")

    # def patch(self, request, *args, **kwargs):
        # return self.partial_update(request, *args, **kwargs)

    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        if user == request.user:
            serializer = UserOwnerSerializer(
                user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data="You cannot edit this user", status=status.HTTP_403_FORBIDDEN)

    # def delete(self, request, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        if user == request.user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data="You cannot delete this user", status=status.HTTP_403_FORBIDDEN)


@api_view()
def student(request, pk):
    from django.db import connection
    user = get_object(request, pk)
    if user.has_student:
        student = user.student
        if user == request.user:
            serializer = StudentOwnerSerializer(student)
        else:
            serializer = StudentViewingSerializer(student)
        print('# of Queries: {}'.format(len(connection.queries)))
        return Response(data=serializer.data)
    return Response(data="User has no Student", status=status.HTTP_404_NOT_FOUND)


@api_view()
def tutor(request, pk):
    from django.db import connection
    user = get_object(request, pk)
    if user.has_tutor:
        tutor = user.tutor
        if user == request.user:
            serializer = TutorOwnerSerializer(tutor)
        else:
            serializer = TutorViewingSerializer(tutor)
        print('# of Queries: {}'.format(len(connection.queries)))
        return Response(data=serializer.data)
    return Response(data="User has no Tutor", status=status.HTTP_404_NOT_FOUND)
