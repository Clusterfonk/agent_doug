from discord.ext import commands
from dotenv import load_dotenv
import discord
import os
import sys
from logging.handlers import RotatingFileHandler
import logging


__CLIENT = commands.Bot(command_prefix='!', description='General Purpose Bot')


def set_up_logger():
    logging.getLogger(__name__)
    logging.basicConfig(
        handlers=[RotatingFileHandler(filename=os.path.expanduser('~/.logs/agent_doug.log'),
                                      maxBytes=2000,
                                      backupCount=10)
                  ],
        format="[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )


def receive_token():
    load_dotenv(os.path.expanduser('~/.config/discord.env'))
    t = os.environ.get('DISCORD_TOKEN')
    if t is None:
        logging.error('Could not read env:[DISCORD_TOKEN]. Token invalid!')
        sys.exit(-1)
    return t


@__CLIENT.event
async def on_ready():
    logging.info('Started Agent Doug.')
    await __CLIENT.change_presence(activity="Listening to !help", status=discord.Status.online)


@__CLIENT.event
async def on_member_join(member):
    pass


@__CLIENT.event
async def on_member_remove(member):
    pass


# @__CLIENT.command()
# async def add(ctx, left: int, right: int):
#     """Adds two numbers together."""
#     await ctx.send(left + right)


if __name__ == '__main__':
    set_up_logger()
    __CLIENT.run(receive_token())
