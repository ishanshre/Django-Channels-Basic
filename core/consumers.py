"""
Creating Consumers
"""

from channels.consumer import SyncConsumer


class MySyncConsumer(SyncConsumer):
    """Creating a Sync Consumer class. """
    def websocket_connect(self, event):
        """It is a handler that is called when a client initially opens a connection and is about to end the websocket handshake"""
        pass

    def websocket_receive(self, event):
        """It is a handler that is called when data is received from the client"""
        pass

    def websocket_disconnect(self, evevt):
        """It is a handler that is invoked when a server and clint loses connection, client closes the connection, server closes the connection, client is lost or the socket is lost"""
        pass