import openai
import os
from chatgpt import ChatGPTClient


def main():
    openai.api_key = os.environ.get('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY')
    saved_prompts = [
          {"role": "system", "content": "Eres un asistente amable y servicial."}
      ]

    while True:
        prompt = input("User > ")
        saved_prompts.append({"role": "user", "content": prompt})
        chatgpt_client = ChatGPTClient(saved_prompts)
        chat_response = chatgpt_client.build_response()
        print("Alexa > {}".format(chat_response))
        saved_prompts.append({"role": "assistant", "content": chat_response})


if __name__ == "__main__":
    main()
