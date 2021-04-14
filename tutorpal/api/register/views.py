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
from .serializers import StudentOwnerSerializer, TutorOwnerSerializer, UserOwnerSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import JsonResponse


@ensure_csrf_cookie
def ensure_csrf(request):
    return JsonResponse("CSRF Ensured!")


def login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(email=email, password=password)

    if not user:
        return JsonResponse({"error": "Incorrect email/password"}, status=400)

    if not user.is_active:
        return Response({"error": "Inactive user (try checking email)"}, status=403)

    django_login(request, user)
    return JsonResponse({"user": UserOwnerSerializer(user).data})


def logout(request):
    django_logout(request)
    return JsonResponse({"success": "Successfully logged out user"})


@api_view(('POST',))
def register_student(request):
    try:
        pfp = request.FILES.get("profile_pic")
        data = request.data.get("data")
        user_data = data.get('user')
        password = user_data.pop('password')
        student_data = data.get('student')
        user = User(**user_data)
        user.set_password(password)
        if pfp:
            user.profile_pic = pfp
        student = Student(**student_data)
        user.save()
        student.user = user
        student.save()
        user.student_pk = student.pk
        user.save()
    except Exception as e:
        print("error: ", e)
        raise e

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

    response = Response(data=StudentOwnerSerializer(
        student).data, status=status.HTTP_201_CREATED)
    # for query in connection.queries:
    #     print("sql query: ", query.get("sql"))
    # print('# of Queries: {}'.format(len(connection.queries)))
    return response


@api_view(('POST',))
def register_tutor(request):
    try:
        pfp = request.FILES.get("profile_pic")
        data = request.data.get("data")
        user_data = data.get('user')
        password = user_data.pop('password')
        tutor_data = data.get('tutor')
        user = User(**user_data)
        user.set_password(password)
        if pfp:
            user.profile_pic = pfp
        tutor = Tutor(**tutor_data)
        user.save()
        tutor.user = user
        tutor.save()
        user.tutor_pk = tutor.pk
        user.save()
    except Exception as e:
        print("error: ", e)
        raise e

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

    response = Response(data=TutorOwnerSerializer(
        tutor).data, status=status.HTTP_201_CREATED)
    # for query in connection.queries:
    #     print("sql query: ", query.get("sql"))
    # print('# of Queries: {}'.format(len(connection.queries)))
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
        print(email)
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
        return Response(data="Successfully changed password", status=status.HTTP_200_OK)
    else:
        return Response(data="Invalid credentials provided", status=status.HTTP_400_BAD_REQUEST)
