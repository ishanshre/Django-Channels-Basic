from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from chatApp5.models import Chat, Group

import json

class chat5AsyncConsumer(AsyncWebsocketConsumer):
    """Creating a asyn consumer inheriting generic async web socket consumer"""

    @database_sync_to_async
    def create_chat(self, msg, name):
        group = Group.objects.get(name=name)
        chat = Chat.objects.create(content=msg, group=group)
        chat.save()
        return chat

    async def connect(self):
        print("async web socket open...")
        # accepting the connection
        print("Channel Layer: ", self.channel_layer)
        print("channel name: ", self.channel_name)
        print("group name: ", self.scope['url_route']['kwargs']['groupName'])
        print("username: ", self.scope['user'].username)
        self.groupName = self.scope['url_route']['kwargs']['groupName']
        await self.channel_layer.group_add(self.groupName, self.channel_name)
        await self.accept()
    
    async def receive(self, text_data=None, bytes_data=None):
        print("Message from client received", text_data)
        print("text_data type", type(text_data))
        data = json.loads(text_data)
        print(data)
        message = data['msg']
        if self.scope['user'].is_authenticated:
            chat = await self.create_chat(message, self.groupName)
            await self.channel_layer.group_send(self.groupName, {
                "type":'chat.message',
                "message":message
            })
        else:
            await self.send(text_data=json.dumps({'msg':"Login Required"}))

    
    async def chat_message(self, event):
        print("chat message", event)
        username = self.scope['user'].username
        await self.send(text_data=json.dumps({
            'msg':event['message'],
            'username':username
        }))
    
    async def disconnect(self, code):
        print("websocket disconnected")
        await self.channel_layer.group_discard(self.groupName, self.channel_name)