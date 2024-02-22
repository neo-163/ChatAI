# route.py

from flask import Blueprint
from .mainController import mainController


class setup(object):
    def __init__(self):
        self.blueprint = Blueprint("ChatGPT", __name__)
        controller = mainController()

        # RESTful endpoint naming
        self.blueprint.add_url_rule(
            "/chatgpt35",
            view_func=controller.chatgpt35,
            methods=['GET'],
            endpoint="chat_chatgpt35"
        )
