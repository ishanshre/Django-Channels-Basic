from django.urls import path

from core import consumers
from chatApp import consumers as chatApp_consumers
from chatApp2 import consumers as chatApp_consumers2
from chatApp3 import consumers as chatApp_consumers3
from chatApp4 import consumers as chatApp_consumers4
from chatApp5 import consumers as chatApp_consumers5
from chatApp6 import consumers as chatApp_consumers6


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
    path("ws/Achat2/<str:groupName>/", chatApp_consumers2.MyDynamicGroupAsyncConsumer.as_asgi(), name="MyDynamicGroupAsyncConsumer"),

    # chatApp3 routing
    path("ws/Schat3/", chatApp_consumers3.MyGenericWebSocketConsumer.as_asgi(), name="MyGenricWebSocketConsumer"),
    path("ws/Achat3/", chatApp_consumers3.MyGenericAsyncWebSocketConsumer.as_asgi(), name="MyGenricAsyncWebSocketConsumer"),
    
    # chatApp 4 routing
    path("ws/chat4Sync/", chatApp_consumers4.chat4SyncConsumer.as_asgi()),
    path("ws/chat4Async/", chatApp_consumers4.chat4AsyncConsumer.as_asgi()),


    # chatApp 5 routing
    path("ws/chat5Async/<groupName>/", chatApp_consumers5.chat5AsyncConsumer.as_asgi()),

    # chatApp 6 routing
    path("ws/chat6Async/<str:groupName>/", chatApp_consumers6.chat6JsonAsyncWebSocketConsumer.as_asgi()),
]