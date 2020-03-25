from dotenv import load_dotenv
import logging
import os
import sys


def receive_token(path_dotenv):
    load_dotenv(path_dotenv)
    t = os.environ.get('DISCORD_TOKEN')
    if t is None:
        logging.error('Could not read env:[DISCORD_TOKEN]. Token invalid!')
        sys.exit(-1)
    return t
