from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from chatApp6.models import Group, Chat
import json

class chat6JsonAsyncWebSocketConsumer(AsyncJsonWebsocketConsumer):
    """
    Inheriting generic async json web socket consumer
    It has wrapped up some functionality of encoding and decoding json unlike websocket and generic websockets
    """

    @database_sync_to_async
    def create_chat(self, content, name):
        group = Group.objects.get(name=name)
        chat = Chat.objects.create(content=content, group=group)
        chat.save()
        return chat

    async def connect(self):
        print("Json async web socket is open")
        print("channel layer:::::", self.channel_layer)
        print("channel name:::::", self.channel_name)
        self.groupName = self.scope['url_route']['kwargs']['groupName']
        self.username = self.scope['user'].username
        print("Current group::::::", self.groupName)
        print("Current logged in user::::", self.username)

        await self.channel_layer.group_add(self.groupName, self.channel_name)
        # accepting the initial conenction 
        await self.accept()
    
    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        print("message from client received ---> ", text_data)
        data = json.loads(text_data)
        print("actual message::::::", data['msg'])
        message = data['msg']
        if self.scope['user'].is_authenticated:
            chat = await self.create_chat(message, self.groupName)
            await self.channel_layer.group_send(self.groupName, {
                "type":"chat.message",
                "message":message
            })
        else:
            await self.send_json({"msg":"Login Required"})
    
    async def chat_message(self, event):
        print("chat messages::::", event)
        
        await self.send_json(
            {
                "msg":event['message'],
                "username":self.username
            }
        )

    async def disconnect(self, code):
        print("web socket disconnected")
    
