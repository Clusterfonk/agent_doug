from discord.ext import commands
import sys
import os


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


if __name__ == '__main__':
    token = os.getenv("DISCORD_TOKEN")
    if token is None:
        sys.exit(-1)
    __BOT.run(token)
