"""
ASGI config for chatapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
# from channels.routing import get_default_application
from django.core.asgi import get_asgi_application
# from .routing import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapi.settings')

django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import re_path, path
from chat.consumers import ChatConsumer
from django.conf.urls import url
# from django.core.asgi import get_asgi_application



application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('ws/chat/<int:room_id>/', ChatConsumer.as_asgi()),
                    path('ws/chat/<int:room_id>', ChatConsumer.as_asgi()),
                    url(r'^ws/chat/(?P<room_id>[^/]+)/$', ChatConsumer.as_asgi()),
                    re_path(r'^ws/chat/(?P<room_id>\w+)', ChatConsumer.as_asgi()),
                    re_path(r'^ws/chat/(?P<room_id>\w+)/$', ChatConsumer.as_asgi()),
                    url(r'^ws/chat/(?P<room_id>\w+)', ChatConsumer.as_asgi()),
                    url(r'^ws/chat/(?P<room_id>\w+)/$', ChatConsumer.as_asgi()),
                    url(r'^ws/chat/(?P<room_id>[^/]+)/$', ChatConsumer.as_asgi()),
                    # re_path(r'ws/chat/(?P<user_id>\w+)/$', ChatConsumer.as_asgi()),
                    # re_path(r'ws/room/(?P<room_id>\w+)/$', consumers.RoomSockets),
                ]
            )
        ),
    )
})