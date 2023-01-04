"""
Creating Consumers
"""

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.consumer import StopConsumer


class MySyncConsumer(SyncConsumer):
    """Creating a Sync Consumer class. """
    def websocket_connect(self, event):
        """It is a handler that is called when a client initially opens a connection and is about to end the websocket handshake"""
        print("Websocket connected: ....", event)
        # websocket.accept is used to accept the connection
        self.send({
            'type':"websocket.accept",
        })

    def websocket_receive(self, event):
        """It is a handler that is called when data is received from the client"""
        print("Message Received: .....", event)
        print("received message is ", event['text'])

    def websocket_disconnect(self, event):
        """It is a handler that is invoked when a server and clint loses connection, client closes the connection, server closes the connection, client is lost or the socket is lost"""
        print("Websocket disconnected: ...", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    """Creating an Async Consumer class"""
    async def websocket_connect(self, event):
        """It is a async handler for new connection"""
        print("Async Websocket connected....", event)
        await self.send({
            "type":"websocket.accept"
        })
    async def websocket_receive(self, event):
        """It is a async handler for receiving new messages"""
        print("Message received...", event)
        print("Received message is :  ", event['text'])
    async def websocket_disconnect(self, event):
        """It is a async handler for disconnecting the websocket connection"""
        print("Websocket disconneced", event)
        raise StopConsumer()


class MySyncConsumer2(SyncConsumer):
    """Another sync websocket"""
    def websocket_connect(self, event):
        print("++++Sync Websocket connected++++")
        print("++++", event, "++++")
        # accepting the connection opened initally by the client
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self, event):
        """Receiving the message from client and also responding to the client"""
        print("++++Message Received++++")
        print("++++Received Message is: ", event['text'], "++++")
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

    def websocket_disconnect(self, event):
        """Disconnecting the websocket connection"""
        print(f"++++Web socket disconnected++++:+++{event}")
        raise StopConsumer()


class MyAsyncConsumer2(AsyncConsumer):
    """Another example for async consumer with resoponding  the message to the client"""
    async def websocket_connect(self, event):
        print("++++Async Websocket connected++++")
        # accepting the connection
        await self.send({
            'type':'websocket.accept',
        })
    
    async def websocket_receive(self, event):
        print("++++Message Receive++++")
        print(f"++++{event['text']}++++")
        await self.send({
            'type':'websocket.send',
            'text':'Message was received and this is sent from server'
        })
    
    async def websocket_disconnect(self, event):
        print(f"++++Web socket disconnected++++:+++{event}")
        raise StopConsumer()
    