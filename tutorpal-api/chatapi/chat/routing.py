from django.urls import re_path
from .consumers import ChatConsumer
from django.conf.urls import url

websocket_urlpatterns = [
    re_path(r'^/ws/chat/(?P<room_id>\w+)', ChatConsumer.as_asgi()),
    url(r'^/ws/chat/(?P<room_id>\w+)', ChatConsumer.as_asgi()),
    # re_path(r'ws/chat/(?P<user_id>\w+)/$', ChatConsumer.as_asgi()),
    # re_path(r'ws/room/(?P<room_id>\w+)/$', consumers.RoomSockets),
]
