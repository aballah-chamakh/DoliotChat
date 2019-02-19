from django.conf.urls import url
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .tokenmiddlware import TokenAuthMiddlewareStack
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({

    "websocket": TokenAuthMiddlewareStack(
        URLRouter([
            path('ws/chat_room/<username_id>/', ChatConsumer),

        ])
    ),

})
