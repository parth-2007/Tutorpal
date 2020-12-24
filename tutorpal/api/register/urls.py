from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register(r'users', v.UserViewSet)
router.register(r'tutors', v.TutorViewSet)
router.register(r'students', v.StudentViewSet)
router.register(r'reviews', v.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/change-password/', v.ChangePasswordView.as_view(),
         name='change-password'),
    path('api/set-csrf/', v.set_csrf_token),
    # path('api/login/', csrf_exempt(v.login_view)),
    path('api/login/', v.login_view),
]
