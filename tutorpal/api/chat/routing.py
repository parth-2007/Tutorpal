from django.urls import re_path
from .views import RoomSockets

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_id>\w+)/$', consumers.ChatConsumer),
    # re_path(r'ws/room/(?P<room_id>\w+)/$', consumers.RoomSockets),
]
