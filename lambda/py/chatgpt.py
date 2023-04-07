import openai
import os


class ChatGPTClient:
    def __init__(self, prompt):
        self.prompt = prompt
        openai.api_key = os.environ.get('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY')

    def send_prompt(self):
        return openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=self.prompt
        )

    def build_response(self):
        response = self.send_prompt()
        return response.choices[0].message.content
