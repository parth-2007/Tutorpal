from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v

router = DefaultRouter()
router.register(r'bugs', v.BugViewSet)
router.register(r'feedback', v.FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls))
]
