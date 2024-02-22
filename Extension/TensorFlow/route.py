# route.py

from flask import Blueprint
from .mainController import mainController


class setup(object):
    def __init__(self):
        self.blueprint = Blueprint("TensorFlow", __name__)
        controller = mainController()

        # RESTful endpoint naming
        self.blueprint.add_url_rule(
            "/tensorflow",
            view_func=controller.analyze_logs,
            methods=['GET'],
            endpoint="/tensorflow/url1"
        )
