# import openai
# import os


# class ChatGPTClient:
#     def __init__(self, prompt):
#         self.prompt = prompt
#         openai.api_key = os.environ.get('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY')

#     def send_prompt(self):
#         return openai.Completion.create(
#             model="text-davinci-003",
#             prompt=self.prompt,
#             temperature=0,
#             max_tokens=4000,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0,
#         )

#     def build_response(self):
#         response = self.send_prompt()
#         return response.choices[0].text

import openai

messages = [
 {"role": "system", "content": "You’re a kind helpful assistant"}
]

while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})
    if content == "para":
        break
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    # Asistant Role is used to save responses
    messages.append({"role": "assistant", "content": chat_response})

print("hasta la vista!")