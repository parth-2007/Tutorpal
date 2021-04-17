from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_id>\w+)/$', ChatConsumer.as_asgi()),
    # re_path(r'ws/room/(?P<room_id>\w+)/$', consumers.RoomSockets),
]
