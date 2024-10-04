"""
A simple module to simplify sending messages to Microsoft Teams Channels. 

It includes two styles of messages: one with just a message and a title, and another with a message, title, and a person to tag.
"""

import requests
from .templates import gen_card_to_person, gen_card_no_person

class TeamsAlert:
    """
    A class to send messages to Microsoft Teams Channels.

    Attributes:
        url (str): The webhook URL for the Teams Channel.
    """
    def __init__(self, url: str):
        self.url = url

    def send(self, title: str = "A Nice Title", message: str = "This is a message.", attention: str = None) -> requests.models.Response:
        """
        Sends a message to the Teams Channel. If a person is tagged, the message will include the person's name.

        Args:
            title (str): The title of the message.
            message (str): The message to send.
            attention (str): (optional) The email of the person to tag in the message.
        """
        self.title = title
        self.attention = attention
        self.message = message

        if self.attention:
            return self.send_message_with_attention()
        else:
            return self.send_message()

    def send_message(self) -> requests.models.Response:
        """
        Sends a message to the Teams Channel without tagging a person.
        """
        payload = gen_card_no_person(self.title, self.message)
        headers = {
            'Content-Type': 'application/json'        
        }

        return requests.request("POST", self.url, headers=headers, data=payload)

    def send_message_with_attention(self) -> requests.models.Response:
        """
        Sends a message to the Teams Channel with a person tagged.
        """
        payload = gen_card_to_person(self.title, self.message, self.attention)
        headers = {
            'Content-Type': 'application/json'        
        }

        return requests.request("POST", self.url, headers=headers, data=payload)

        