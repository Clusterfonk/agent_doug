from discord.ext import commands
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
import logging
import os
import sys


__BOT = commands.Bot(command_prefix='!', description='General Purpose Bot')


def set_up_logger():
    logging.getLogger(__name__)
    logging.basicConfig(
        handlers=[RotatingFileHandler(filename=os.path.expanduser('~/.logs/agent_doug.log'), maxBytes=2000, backupCount=10)],
        format="[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def receive_token():
    load_dotenv('~/.config/discord.env')
    t = os.getenv('DISCORD_TOKEN')
    if t is None:
        logging.error('Could not read environment variable. Token invalid!')
        sys.exit(-1)
    return t


@__BOT.event
async def on_ready():
    await logging.info('Started Agent Doug.')


@__BOT.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@__BOT.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


if __name__ == '__main__':
    set_up_logger()
    __BOT.run(receive_token())
