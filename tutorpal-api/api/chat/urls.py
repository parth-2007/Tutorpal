from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v

router = DefaultRouter()
router.register(r'rooms', v.RoomViewSet)
# router.register(r'messages', v.MessageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
