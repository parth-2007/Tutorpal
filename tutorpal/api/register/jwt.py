# Back to JWT lol
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenViewBase
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import Token, RefreshToken
from django.conf import settings
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from .models import User
from django.utils.timezone import now, make_aware, localtime
import json
from rest_framework import serializers
from datetime import datetime
from django.conf import settings


def get_token_data_from_token(token):
    validated_token = RefreshToken(token)
    print(validated_token)
    user_id = validated_token['user_id']
    issued = validated_token['issued']
    issued = datetime.strptime(issued, "%Y-%m-%d %H:%M:%S.%f%z")
    print(issued)
    print(user_id)
    return user_id, issued


def check_token_invalid(token):
    token = RefreshToken(token)
    user_id, issued = get_user_from_token(token)
    user = User.objects.get(pk=user_id)
    if user.last_reset >= issued:
        token.blacklist()


def create_tokens_from_user(user):
    refresh = RefreshToken.for_user(user)
    tokens = {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }
    return tokens


# class Timezone:
#     def __init__(self):
#         self.timezone = timezone.now()


# class TimezoneSerializer(serializers.Serializer):
#     timezone = serializers.DateTimeField()


# def serializetimezone():
#     # if TimezoneSerializer(data=Timezone).is_valid():
#     return TimezoneSerializer(data=Timezone).is_valid()


class MyTokenViewBase(TokenViewBase):
    # def get(self, request, *args, **kwargs):
    #     print("hi")
    #     # refreshing for tokens stored in cookie
    #     refresh_token = request.COOKIES.get('refresh_token')
    #     print(refresh_token)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        try:
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
        except TokenError as e:
            raise InvalidToken(e.args[0])
        print("\nrequest data: ", data)
        if "error" in data:
            response = Response(data=data, status=status.HTTP_403_FORBIDDEN)
            return response
        elif "refresh" and "access" in data:
            response = Response(data=data, status=status.HTTP_200_OK)
            response.set_cookie('refresh', data.get('refresh'))
            return response
        else:
            response = Response(data=data, status=status.HTTP_200_OK)
            return response


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['issued'] = str(now())
        return token


class MyTokenObtainPairView(MyTokenViewBase):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        validated_token = RefreshToken(attrs['refresh'])
        # print("\nValidated token: ", validated_token)
        user_id = validated_token['user_id']
        issued = validated_token['issued']
        issued = datetime.strptime(issued, "%Y-%m-%d %H:%M:%S.%f%z")
        # print("\nIssued date and time: ", issued)
        # print("\nUser id:", user_id)
        user = User.objects.get(pk=user_id)
        if issued >= user.last_reset:
            # print("\nValid token\n")
            data = super().validate(attrs)
        else:
            # print("\nInvalid token\n")
            validated_token.blacklist()
            data = {'error': 'this refresh token is no longer valid'}
        return data


class MyTokenRefreshView(TokenViewBase):
    serializer_class = MyTokenRefreshSerializer


@api_view()
def refresh_token_from_cookie(request):
    refresh_token = request.COOKIES.get('refresh')
    serializer = MyTokenRefreshSerializer(data={"refresh": refresh_token})
    try:
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
    except TokenError as e:
        raise InvalidToken(e.args[0])
    if "error" in data:
        response = Response(data=data, status=status.HTTP_403_FORBIDDEN)
        return response
    else:
        response = Response(data=data, status=status.HTTP_200_OK)
        return response


myTokens = {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMTUyNDEzMCwianRpIjoiODRhNWNkMTc3NmIyNGEwZWJhZDgwOGI0ZGZkZjZiMjciLCJ1c2VyX2lkIjo1LCJpc3N1ZWQiOiIyMDIxLTAxLTIzIDIxOjM1OjMwLjc0MzY1OCswMDowMCJ9.v4YQDbDVm3oh_bNgHUaUT7SUR4uReQmFSTIIvKUNVwE",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExNDM4MDMwLCJqdGkiOiJmNjc5Njc1ODZjZTI0MTE1YTkyOGM4OTUxN2ExZWIxYiIsInVzZXJfaWQiOjUsImlzc3VlZCI6IjIwMjEtMDEtMjMgMjE6MzU6MzAuNzQzNjU4KzAwOjAwIn0.t1Voc9CSnsm9-fpsGKTPFia1Fo2iW2wRCB0X8I1PNpI"
}


@api_view()
def jwt_test(request):
    # user = User.objects.get(id=5)
    # tokens = create_tokens_from_user(user)
    refresh_token = myTokens['refresh']
    validated_token = RefreshToken(refresh_token)
    print("\nValidated token: ", validated_token)
    user_id = validated_token['user_id']
    issued = validated_token['issued']
    issued = datetime.strptime(issued, "%Y-%m-%d %H:%M:%S.%f%z")
    print("\nIssued date and time: ", issued)
    print("\nUser id:", user_id)
    user = User.objects.get(pk=user_id)
    if user.last_reset < issued:
        print("\nduifhasdfdsjfuasjfk\n")
    return Response(data={"id": str(user_id)})


@api_view()
def loginproxyurl(request):
    return Response(data={'hi': 'my target proxy'}, status=status.HTTP_200_OK)
