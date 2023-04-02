#!/usr/bin/env python3

import sys
from chatgpt import ChatGPTClient


def main(args):
    if len(args) < 2:
        print("Usage: {0} <prompt>".format(args[0]))
        sys.exit(1)
    prompt = args[1]
    chatgpt_client = ChatGPTClient(prompt)
    response = chatgpt_client.build_response()
    print(response)


if __name__ == "__main__":
    main(sys.argv)
