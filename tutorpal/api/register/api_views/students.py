from ..models import Student, User
from ..serializers import UserOwnerSerializer, UserViewingSerializer, StudentOwnerSerializer, StudentViewingSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page


class StudentList(APIView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get(self, request, format=None):
        students = Student.objects.all().select_related('user')
        serializer = StudentViewingSerializer(students, many=True)
        return Response(serializer.data)


class StudentDetail(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentOwnerSerializer
    # permission_classes = (DRYPermissions,)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get_object(self, pk=None):
        if self.request.user.is_authenticated and pk == "me" and self.request.user.has_student:
            return self.request.user.student
        elif pk == "me" and not self.request.user.is_authenticated:
            raise Http404
        try:
            return Student.objects.select_related('user').get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        # return super().get_object()

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        if request.user.is_authenticated and pk == request.user.student_id:
            serializer = StudentOwnerSerializer(student)
        else:
            serializer = StudentViewingSerializer(student)
        return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
        # return self.update(request, *args, **kwargs)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        if student == request.user.student:
            serializer = StudentOwnerSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data="You cannot edit this student")

    # def patch(self, request, *args, **kwargs):
        # return self.partial_update(request, *args, **kwargs)

    def patch(self, request, pk, format=None):
        student = self.get_object(pk)
        if student == request.user.student:
            serializer = StudentOwnerSerializer(
                student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data="You cannot edit this student", status=status.HTTP_403_FORBIDDEN)

    # def delete(self, request, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        if student == request.user.student:
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data="You cannot delete this student", status=status.HTTP_403_FORBIDDEN)


@api_view()
def user_(request, pk):
    from django.db import connection
    if pk == "me":
        serializer = UserOwnerSerializer(request.user)
    else:
        user = User.objects.get(student_id=pk)
        serializer = UserViewingSerializer(user)
    print('# of Queries: {}'.format(len(connection.queries)))
    return Response(data=serializer.data)
