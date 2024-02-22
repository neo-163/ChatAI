# route.py

from flask import Blueprint
from .main_controller import mainController

# In Flask, the endpoint parameter when adding a route is used to uniquely identify a view function


class setup(object):
    def __init__(self):
        self.blueprint = Blueprint("LangChain", __name__)
        controller = mainController()

        # RESTful endpoint naming
        self.blueprint.add_url_rule(
            "/demo1",
            view_func=controller.demo1,
            methods=['GET'],
            endpoint="demo1"
        )
        self.blueprint.add_url_rule(
            "/demo2",
            view_func=controller.demo2,
            methods=['POST'],
            endpoint="demo2"
        )
