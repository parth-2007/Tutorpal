from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_student, register_tutor, reset_password, password_reset, activate_account, ensure_csrf, login, logout
from .viewsets import UserViewSet, TutorViewSet, StudentViewSet, ReviewViewSet
# from .jwt import MyTokenObtainPairView, refresh_token_from_cookie, cookie_logout

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tutors', TutorViewSet)
router.register(r'students', StudentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/ensure-csrf/', ensure_csrf),
    path('auth/login/', login),
    path('auth/logout/', logout),
    # path('api-auth/token/', MyTokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api-auth/token/refresh/', refresh_token_from_cookie),
    # path('api-auth/token/logout/', cookie_logout),
    path('auth/register-student/', register_student),
    path('auth/register-tutor/', register_tutor),
    path('auth/activate-account/<uidb64>/<token>/',
         activate_account, name="activate"),
    path('auth/reset-password/', reset_password),
    path('auth/password-reset/<uidb64>/<token>/', password_reset, name="reset"),
]
