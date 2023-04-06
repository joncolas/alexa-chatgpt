import openai
import os


class ChatGPTClient:
    def __init__(self, prompt, saved_prompts):
        self.prompt = prompt
        self.saved_prompts = saved_prompts
        openai.api_key = os.environ.get('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY')

    def send_prompt(self):
        return openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=self.saved_prompts
        )

    def build_response(self):
        response = self.send_prompt()
        return response.choices[0].message.content
