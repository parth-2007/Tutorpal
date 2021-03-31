from ..models import Review
from ..serializers import ReviewSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ReviewList(APIView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get(self, request, format=None):
        reviews = Review.objects.all().select_related(
            'student', 'student__user', 'tutor')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        tutor = request.data.get('tutor')
        # 1 query
        if not Review.objects.filter(student__user=request.user, tutor=tutor).exists():
            if serializer.is_valid():
                serializer.save(student__user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="Cannot make review", status=status.HTTP_403_FORBIDDEN)


class ReviewDetail(APIView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        from django.db import connection
        print('# of Queries: {}'.format(len(connection.queries)))
        return response

    def get_object(self, pk=None):
        try:
            return Review.objects.select_related('student', 'student__user', 'tutor').get(pk=pk)
        except Review.DoesNotExist:
            raise Http404
        # return super().get_object()

    def get(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
        # return self.update(request, *args, **kwargs)

    def put(self, request, pk, format=None):
        review = self.get_object(pk)
        student = review.student
        if request.user.has_student and student == request.user.student:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data="You cannot edit this review")

    # def patch(self, request, *args, **kwargs):
        # return self.partial_update(request, *args, **kwargs)

    def patch(self, request, pk, format=None):
        review = self.get_object(pk)
        student = review.student
        if request.user.has_student and student == request.user.student:
            serializer = ReviewSerializer(
                review, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data="You cannot edit this review")

    # def delete(self, request, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)

    # def delete(self, request, pk, format=None):
    #     review = self.get_object(pk)
    #     student = review.student
    #     if request.user.has_student and student == request.user.student:
    #         review.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     return Response(data="You cannot delete this student", status=status.HTTP_403_FORBIDDEN)
