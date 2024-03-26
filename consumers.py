
import json

from channels.generic.websocket import WebsocketConsumer
from chatroom.managers.chat_room import CHATROOM_MANAGER
from gpm.websocket.decorators import websocket__simplifier
from gpm.http.request import FakeRequest
from gpm.interfaces.decorators import load_interface

class NotificationConsumer(WebsocketConsumer):
    """

    """

    def connect(self):
        """
        """

    def receive(self, text_data):
        """
        """

    def receive__initial_settings(self, settings):
        """
    
        """
        pass

    def receive__new_message(self, data):
        """
            @description:
        """


    def receive__init(self, message):
        """
            @description: Init.
        """

    def receive__create_personnal_room(self, message):
        """
            @description: Create a personnal room.
        """


    def receive__delete_room(self, chatroom):
        """
            @description: 
        """
