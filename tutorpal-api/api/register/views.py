from .tokens import account_activation_token, password_reset_token
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import User, Student, Tutor
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.timezone import now
from rest_framework.decorators import api_view
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
import json
from django.db.utils import IntegrityError
from .serializers import TutorOwnerSerializer, StudentOwnerSerializer, UserOwnerSerializer


@ensure_csrf_cookie
def ensure_csrf(request):
    return JsonResponse({"success": "CSRF Ensured!"})


def login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(email=email, password=password)

    if not user:
        return JsonResponse({"error": "Incorrect password"}, status=400)

    if not user.is_active:
        return JsonResponse({"error": "Inactive user (try checking email)"}, status=403)

    django_login(request, user)
    return JsonResponse({"success": "Successfully logged in user"})


def logout(request):
    django_logout(request)
    return JsonResponse({"success": "Successfully logged out user"})


@api_view(('POST',))
def register_student(request):
    try:
        pfp = request.FILES.get("profile_pic")
        user_data = request.data.get("user")
        user_data = json.loads(user_data)
        password = user_data.pop('password')
        student_data = request.data.get('student')
        student_data = json.loads(student_data)
        user = User(**user_data)
        user.set_password(password)
        if pfp is not None:
            user.profile_pic = pfp
        student = Student(**student_data)
        user.save()
        student.user = user
        student.save()
        user.student_pk = student.pk
        user.save()
    except IntegrityError:
        return Response(data={'error': 'this email is taken'}, status=status.HTTP_400_BAD_REQUEST)

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

    response = Response(
        data={'success': 'Successfully created student'}, status=status.HTTP_201_CREATED)
    # for query in connection.queries:
    #     print("sql query: ", query.get("sql"))
    # print('# of Queries: {}'.format(len(connection.queries)))
    return response


@api_view(('POST',))
def register_tutor(request):
    try:
        pfp = request.FILES.get("profile_pic")
        user_data = request.data.get("user")
        user_data = json.loads(user_data)
        password = user_data.pop('password')
        tutor_data = request.data.get('tutor')
        tutor_data = json.loads(tutor_data)
        user = User(**user_data)
        user.set_password(password)
        if pfp is not None:
            user.profile_pic = pfp
        tutor = Tutor(**tutor_data)
        user.save()
        tutor.user = user
        tutor.save()
        user.tutor_pk = tutor.pk
        user.save()
    except IntegrityError:
        return Response(data={'error': 'this email is taken'}, status=status.HTTP_400_BAD_REQUEST)

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

    response = Response(data={'success': 'Successfully created tutor'},
                        status=status.HTTP_201_CREATED)
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
        update_session_auth_hash(request, user)
        return Response(data="Successfully changed password", status=status.HTTP_200_OK)
    else:
        return Response(data="Invalid credentials provided", status=status.HTTP_400_BAD_REQUEST)


@api_view(('PATCH', 'PUT'))
def update_tutor(request):
    partial = True if request.method == "PATCH" else False
    tutor_data = request.data.get('tutor')
    tutor_data = json.loads(tutor_data)
    user_data = request.data.get('user')
    user_data = json.loads(user_data)
    profile_pic = request.FILES.get('profile_pic', None)
    if profile_pic is not None:
        user_data['profile_pic'] = profile_pic

    tutor_obj = request.user.tutor
    user_obj = request.user

    tutor_serializer = TutorOwnerSerializer(
        tutor_obj, data=tutor_data, partial=partial)
    user_serializer = UserOwnerSerializer(
        user_obj, data=user_data, partial=partial)

    tutor_serializer.is_valid(raise_exception=True)
    user_serializer.is_valid(raise_exception=True)

    tutor_serializer.save()
    user_serializer.save()

    return Response({'success': 'successfully updated tutor'})


@api_view(('PATCH', 'PUT'))
def update_student(request):
    partial = True if request.method == "PATCH" else False
    student_data = request.data.get('student')
    student_data = json.loads(student_data)
    user_data = request.data.get('user')
    user_data = json.loads(user_data)
    profile_pic = request.FILES.get('profile_pic', None)
    if profile_pic is not None:
        user_data['profile_pic'] = profile_pic

    student_obj = request.user.student
    user_obj = request.user

    student_serializer = StudentOwnerSerializer(
        student_obj, data=student_data, partial=partial)
    user_serializer = UserOwnerSerializer(
        user_obj, data=user_data, partial=partial)

    student_serializer.is_valid(raise_exception=True)
    user_serializer.is_valid(raise_exception=True)

    student_serializer.save()
    user_serializer.save()

    return Response({'success': 'successfully updated tutor'})
