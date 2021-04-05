# from ..models import Session
# from ..serializers import SessionSerializer, ReservedSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class SessionList(APIView):
#     def dispatch(self, request, *args, **kwargs):
#         response = super().dispatch(request, *args, **kwargs)
#         from django.db import connection
#         print('# of Queries: {}'.format(len(connection.queries)))
#         return response
