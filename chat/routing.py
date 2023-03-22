from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path(r'chat/ws/socket-server', consumers.ChatConsumer.as_asgi()),
]