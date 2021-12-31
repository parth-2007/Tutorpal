from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_student, register_tutor, reset_password, password_reset, activate_account, ensure_csrf, login, logout, update_student, update_tutor, get_register_url_for_user, get_forgot_password_url_for_user
from .viewsets import UserViewSet, TutorViewSet, StudentViewSet, ReviewViewSet, TutorReviews
import os

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tutors', TutorViewSet)
router.register(r'students', StudentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tutors/<pk>/reviews/', TutorReviews.as_view({'get': 'get'})),
    path('auth/ensure-csrf/', ensure_csrf),
    path('auth/login/', login),
    path('auth/logout/', logout),
    # path('api-auth/token/', MyTokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api-auth/token/refresh/', refresh_token_from_cookie),
    # path('api-auth/token/logout/', cookie_logout),
    path('auth/register-student/', register_student),
    path('auth/register-tutor/', register_tutor),
    path('auth/update-student/', update_student),
    path('auth/update-tutor/', update_tutor),
    path('auth/activate-account/<uidb64>/<token>/',
         activate_account, name="activate"),
    path('auth/reset-password/', reset_password),
    path('auth/password-reset/<uidb64>/<token>/', password_reset, name="reset"),
]

if os.environ.get('RUN_ENV', 'local') == 'local':
    urlpatterns += [
        path('test/get_register_url_for_user/<email>', get_register_url_for_user),
        path('test/get_forgot_password_url_for_user/<email>', get_forgot_password_url_for_user),
    ]
