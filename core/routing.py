from django.urls import path

from core import consumers
from chatApp import consumers as chatApp_consumers
from chatApp2 import consumers as chatApp_consumers2


websocket_urlpatterns = [
    path("ws/sc/", consumers.MySyncConsumer.as_asgi(), name="mySyncConsumer"),
    path("ws/ac/", consumers.MyAsyncConsumer.as_asgi(), name="myAsyncConsumer"),
    path('ws/sc2/', consumers.MySyncConsumer2.as_asgi(), name="mySyncConsumer2"),
    path('ws/ac2/', consumers.MyAsyncConsumer2.as_asgi(), name="myAsyncConsumer2"),
    path('ws/sc3/', consumers.MySyncConsumer3.as_asgi(), name="mySyncConsumer3"),
    path('ws/ac3/', consumers.MyAsyncConsumer3.as_asgi(), name="myAsyncConsumer3"),
    
    # chatApp routing
    path("ws/Schat1/", chatApp_consumers.MySyncChatConsumer.as_asgi(), name="MySyncChatConsumer"),
    path("ws/Achat1/", chatApp_consumers.MyAsyncChatConsumer.as_asgi(), name="AySyncChatConsumer"),
    path("ws/Achat2/<str:groupName>/", chatApp_consumers2.MyDynamicGroupAsyncConsumer.as_asgi(), name="MyDynamicGroupAsyncConsumer")
]