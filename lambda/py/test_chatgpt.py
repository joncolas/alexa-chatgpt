#!/usr/bin/env python3

import sys
from chatgpt import ChatGPTClient
import signal
import languaje

locale = "es-ES"


def get_chatgpt_response(prompt):
    signal.signal(signal.SIGALRM, time_out)
    # Ensure query does not take for than the Alexa timeout(10s)
    signal.alarm(7)
    # If ChatGPT takes more time this query is terminated
    chatgpt_client = ChatGPTClient(prompt)
    return chatgpt_client.build_response()


def time_out(signum, frame):
    raise GPTPrompResolutionTakesTooMuchTime


class GPTPrompResolutionTakesTooMuchTime(Exception):
    pass


def main(args):
    if len(args) < 2:
        print("Usage: {0} <prompt>".format(args[0]))
        sys.exit(1)
    prompt = args[1]
    print(languaje.strings[locale]["CHAT_GPT_ACTIVATED"])
    try:
        speak_output = get_chatgpt_response(prompt)
    except GPTPrompResolutionTakesTooMuchTime:
        # Alexa response timeout: 10s
        speak_output = languaje.strings[locale]["ALEXA_TIMEOUT"]
        pass

    print(speak_output)


if __name__ == "__main__":
    main(sys.argv)
