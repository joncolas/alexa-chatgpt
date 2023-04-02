#!/usr/bin/env python3

import sys
from chatgpt import ChatGPTClient
import timeout_decorator


@timeout_decorator.timeout(8)
def get_chatgpt_response(prompt):
    chatgpt_client = ChatGPTClient(prompt)
    return chatgpt_client.build_response()


def main(args):
    if len(args) < 2:
        print("Usage: {0} <prompt>".format(args[0]))
        sys.exit(1)
    prompt = args[1]
    try:
        speak_output = get_chatgpt_response(prompt)
    except timeout_decorator.timeout_decorator.TimeoutError:
        speak_output = "Lo siento, la pregunta que has hecho necesita más de 10 segundos para resolverse, lo cual está por encima de mis posibilidades. Prueba Chat GPT web."
        pass

    print(speak_output)


if __name__ == "__main__":
    main(sys.argv)
