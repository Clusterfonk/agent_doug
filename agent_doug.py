import discord
from discord.ext import commands
import logging


from bot_action_logger import set_up_logger
from acquire_token import receive_token


__CLIENT = commands.Bot(command_prefix='!', description='General Purpose Bot')


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
