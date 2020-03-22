import discord
from discord.ext import commands
import sys

__BOT = commands.Bot(command_prefix='!', description='General Purpose Bot')


@__BOT.event
async def on_ready():
    print('Logged in as')
    print(__BOT.user.name)
    print(__BOT.user.id)
    print('------')


@__BOT.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@__BOT.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


def load_token():
    try:
        with open("/.config/discord_bot_token") as token_file:
            return token_file.read()
    except FileNotFoundError as error:
        sys.exit(error.errno)


if __name__ == '__main__':
    token = load_token()
    __BOT.run(token)
