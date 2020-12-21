from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v

router = DefaultRouter()
router.register(r'users', v.UserViewSet)
router.register(r'tutors', v.TutorViewSet)
router.register(r'students', v.StudentViewSet)
router.register(r'reviews', v.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/change-password/', v.ChangePasswordView.as_view(),
         name='change-password'),
]
