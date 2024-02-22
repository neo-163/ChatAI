# main_controller.py

from flask import jsonify, make_response, request
from .main_model import mainModel

# Define the start and end dates
clean_time_start = "2023-12-20 14:00:00"
clean_time_end = "2024-12-20 16:00:00"

# Create default data
posts_ids = {1, 2, 3}

class mainController:

    def get_posts(self):
        """Retrieve posts"""
        db_model = mainModel()
        data = db_model.get_posts(posts_ids)
        if "error" in data:
            return make_response(jsonify(data), 400)

        return jsonify(data)

    def delete_posts(self):
        """Delete posts within a certain date range"""
        db_model = mainModel()
        result = db_model.delete_posts(clean_time_start, clean_time_end)
        if result.get("error"):
            return make_response(jsonify(result), 500)

        return jsonify(result)