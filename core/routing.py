from django.urls import path

from core import consumers


app_name = "core"
websocket_urlpatterns = [
    path("ws/sc/", consumers.MySyncConsumer.as_asgi(), name="mySyncConsumer"),
    path("ws/ac/", consumers.MyAsyncConsumer.as_asgi(), name="myAsyncConsumer"),
    path('ws/sc2/', consumers.MySyncConsumer2.as_asgi(), name="mySyncConsumer2"),
    path('ws/ac2/', consumers.MyAsyncConsumer2.as_asgi(), name="myAsyncConsumer2"),
]