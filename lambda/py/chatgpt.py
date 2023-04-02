import openai
import os


class ChatGPTClient:
    def __init__(self, prompt):
        self.prompt = prompt
        openai.api_key = os.environ.get('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY')

    def send_prompt(self):
        return openai.Completion.create(
            model="text-davinci-003",
            prompt=self.prompt,
            temperature=0,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

    def build_response(self):
        response = self.send_prompt()
        return response.choices[0].text
