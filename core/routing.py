from django.urls import path

from core.consumers import MyAsyncConsumer, MySyncConsumer


app_name = "core"
websocket_urlpatterns = [
    path("ws/sc/", MySyncConsumer.as_asgi(), name="mySyncConsumer"),
    path("ws/ac/", MyAsyncConsumer.as_asgi(), name="myAsyncConsumer"),
]