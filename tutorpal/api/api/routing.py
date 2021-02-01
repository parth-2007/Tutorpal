from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from chat.consumers import ChatConsumer
from django.conf.urls import url
from djangochannelsrestframework.consumers import view_as_consumer
from chat.views import RoomViewSet

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r'^chat/(?P<room_id>\w+)', ChatConsumer()),
                    # url(r'^wsroom/$', view_as_consumer(RoomViewSet))
                ]
            )
        ),
    )
})
