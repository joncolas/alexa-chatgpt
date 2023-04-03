#!/usr/bin/env python3

import sys
from chatgpt import ChatGPTClient
import signal


def get_chatgpt_response(prompt):
    signal.signal(signal.SIGALRM, time_out)
    # Ensure query does not take for than the Alexa timeout(10s)
    signal.alarm(7)
    # If ChatGPT takes more time this query is terminated
    chatgpt_client = ChatGPTClient(prompt)
    return chatgpt_client.build_response()


def time_out(signum, frame):
    raise GPTPrompResolutionTakesToMuchTime


class GPTPrompResolutionTakesToMuchTime(Exception):
    pass


def main(args):
    if len(args) < 2:
        print("Usage: {0} <prompt>".format(args[0]))
        sys.exit(1)
    prompt = args[1]

    try:
        speak_output = get_chatgpt_response(prompt)
    except GPTPrompResolutionTakesToMuchTime:
        # Alexa response timeout: 10s
        speak_output = "Lo siento, la pregunta que has hecho necesita más de 10 segundos para resolverse, lo cual está por encima de mis posibilidades, reformula la pregunta"
        pass

    print(speak_output)


if __name__ == "__main__":
    main(sys.argv)
