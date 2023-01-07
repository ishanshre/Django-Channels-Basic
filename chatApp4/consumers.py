from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

from time import sleep
import asyncio

class chat4SyncConsumer(WebsocketConsumer):
    def connect(self):
        print("web socket connected....")
        self.accept()
    
    def receive(self, text_data=None, bytes_data=None):
        print("Message received...", text_data)
        self.send(text_data="Received message from client")
        for i in range(20):
            self.send(text_data=f"server responding with :{str(i)}")
            sleep(1)
        # self.close() # it closes the websocket after send message to server

    def disconnect(self, code):
        print("web socket disconnect...", code)
        


class chat4AsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("web socket connectoin accepted")
        await self.accept()
    
    async def receive(self, text_data=None, bytes_data=None):
        print("message received::", text_data)
        for i in range(20):
            await self.send(str(i))
            await asyncio.sleep(1)

    
    async def disconnect(self, code):
        print("web socket disconnected", code)