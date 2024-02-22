# main_controller.py

from flask import Response
import openai
from flask.json import dumps


class mainController:

    def chatgpt35(self):
        openai.api_key = 'api_key'

        # Use the ChatCompletion to interact with the chat model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "AI在3000年可以做什麼事情"}
            ]
        )

        # Extracting the message content from the response
        message_content = response['choices'][0]['message']['content']

        # Generate JSON string with non-escaped characters
        json_str = dumps(
            {"status": "success", "data": message_content}, ensure_ascii=False)

        # Create a HTTP response with the JSON string
        return Response(json_str, mimetype='application/json', status=200)
