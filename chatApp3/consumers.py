from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class MyGenericWebSocketConsumer(WebsocketConsumer):
    def connect(self):
        print("web socket connected....")
        self.accept()
    
    def receive(self, text_data=None, bytes_data=None):
        print("Message received...", text_data)
        self.send(text_data="Received message from client")
        # self.close() # it closes the websocket after send message to server

    def disconnect(self, code):
        print("web socket disconnect...", code)
        self.close() # can be written anywhere we want to clos our connection



class MyGenericAsyncWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("web socket connect;;;;;;")
        await self.accept()

    
    async def receive(self, text_data=None, bytes_data=None):
        print("Message received from client....", text_data)
        await self.send(text_data="This is response from server")
        await self.close(code=4212)

    async def disconnect(self, code):
        print("web socket disconnected")
        await self.close(code=code)