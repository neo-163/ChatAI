# route.py

from flask import Blueprint
from .mainController import mainController

class setup(object):
    def __init__(self):
        self.blueprint = Blueprint("DataHandling", __name__)
        controller = mainController()

        # RESTful endpoint naming
        self.blueprint.add_url_rule(
            "/posts",
            view_func=controller.get_posts,
            methods=['GET'],
            endpoint="get_posts"
        )
        self.blueprint.add_url_rule(
            "/posts/delete",
            view_func=controller.delete_posts,
            methods=['DELETE'],
            endpoint="delete_posts"
        )