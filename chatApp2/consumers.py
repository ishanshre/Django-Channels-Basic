from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer

from asgiref.sync import async_to_sync
import json

from django.shortcuts import get_object_or_404

from chatApp2.models import Chat, Group

from channels.db import database_sync_to_async

class MyDynamicGroupAsyncConsumer(AsyncConsumer):
    """Async consumer chat app wit dynamic group"""


    # convert django orm from sync to async consumer
    @database_sync_to_async
    def create_chat(self, msg, name):
        group = Group.objects.get(name=name)
        return Chat.objects.create(content=msg, group=group)

    async def websocket_connect(self, event):
        print("async web socket connected...", event)
        print("channel layer :::", self.channel_layer)
        print("channel name :::", self.channel_name)
        print("Group Name:   ",self.scope['url_route']['kwargs']['groupName'])
        print("Current User ::::", self.scope['user'])
        self.groupName = self.scope['url_route']['kwargs']['groupName']
        await self.channel_layer.group_add(self.groupName, self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print("Message received...", event['text'])
        print("message type:   ", type(event['text']))
        data = json.loads(event['text']) # event['text'] is str class so converting into dict
        actual_message = data['msg']
        print("actual message...", actual_message)
        if self.scope['user'].is_authenticated:
        # django orm is sync. So we must make it aync
            chat = await self.create_chat(actual_message, self.groupName)
            data['user'] = self.scope['user'].username
            print(data)
            await self.channel_layer.group_send(self.groupName, {
                "type":"chat.message",
                "message":json.dumps(data)
            })
        else:
            await self.send({
                "type":"websocket.send",
                "text": json.dumps({"msg":"Login Required"})
            })
    
    async def chat_message(self, event):
        print("Message from client::: ", event['message'])
        await self.send({
            'type':'websocket.send',
            'text': event['message']
        })
    
    async def websocket_disconnect(self, event):
        print("web socket disconnected...", event)
        await self.channel_layer.group_discard(self.groupName, self.channel_name)
        raise StopConsumer()