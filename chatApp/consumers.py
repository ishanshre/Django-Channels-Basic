"""Create a simple group chat"""
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

from asgiref.sync import async_to_sync

class MySyncChatConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("web socket connected", event)
        print("Channel layer ", self.channel_layer)
        print("Channel name ", self.channel_name)
        # now adding this layer to a group using channel_layer.add_group
        # we are inside a sync consumser and group_add is an async method so we need to convert it to sync
        # we use async_to_sync from asgiref.sync and only wrap the group_add method
        async_to_sync(self.channel_layer.group_add)('programmer', self.channel_name )
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print("message from client received", event['text'])
        async_to_sync(self.channel_layer.group_send)("programmer", {
            'type':'chat.message',
            'message':event['text']
        })
    """"We create our own handler. type is chat.message then handle will be chat_message """
    def chat_message(self, event):
        print("event...", event)
        print("Actual message event...", event['message'])
        self.send({
            'type':'websocket.send',
            'text': event['message']
        })
        

    
    def websocket_disconnect(self, event):
        print("web socket disconnected", event)
        async_to_sync(self.channel_layer.group_discard)("programmer", self.channel_name)
        raise StopConsumer()