import logging
import os
import sys

from dotenv import load_dotenv


def receive_token():
    load_dotenv(os.path.expanduser('~/.config/discord.env'))
    t = os.environ.get('DISCORD_TOKEN')
    if t is None:
        logging.error('Could not read env:[DISCORD_TOKEN]. Token invalid!')
        sys.exit(-1)
    return t