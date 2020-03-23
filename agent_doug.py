from discord.ext import commands
from dotenv import load_dotenv
import sys
import os
import logging

__BOT = commands.Bot(command_prefix='!', description='General Purpose Bot')
logging.basicConfig(filename='~/.logs/agent_doug.log',
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


@__BOT.event
async def on_ready():
    logging.info('Started Agent Doug.')


@__BOT.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@__BOT.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


if __name__ == '__main__':
    load_dotenv('~/.config/discord.env')
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        logging.error('Could not read environment variable. Token invalid!')
        sys.exit(-1)
    __BOT.run(token)
