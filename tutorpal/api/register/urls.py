from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views as v
from django.views.decorators.csrf import csrf_exempt
# from knox import views as knox_views
from .jwt import jwt_test, MyTokenObtainPairView, MyTokenRefreshView, refresh_token_from_cookie, cookie_logout
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'users', v.UserViewSet)
router.register(r'tutors', v.TutorViewSet)
router.register(r'students', v.StudentViewSet)
router.register(r'reviews', v.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('jwt/test/', jwt_test),
    path('api/change-password/', v.ChangePasswordView.as_view(),
         name='change-password'),
    path('api/set-csrf/', v.set_csrf_token),
    # path('api/login/', csrf_exempt(v.login_view)),
    # path('api/login/', v.login_view),
    # path('api/logout/', v.logout_view),
    # path('test/', v.test),
    path('api-auth/token/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    # path('api-auth/token/refresh/', jwt_views.TokenRefreshView.as_view(),
    #      name='token_refresh'),
    #     path('api-auth/token/refresh/', MyTokenRefreshView.as_view(),
    #          name='token_refresh'),
    path('api-auth/token/refresh/', refresh_token_from_cookie),
    path('api-auth/token/logout/', cookie_logout)
]
