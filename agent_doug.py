import discord
from discord.ext import commands
import logging

from bot_action_logger import set_up_logger
from acquire_token import receive_token

__CLIENT = commands.Bot(command_prefix='!', description='General Purpose Bot',
                        status=discord.Status.online,
                        activity=discord.Activity(name="!help",
                                                  type=discord.ActivityType.listening))
__CLIENT.remove_command('help')


@__CLIENT.event
async def on_ready():
    logging.info('Started Agent Doug.')


@__CLIENT.event
async def on_member_join(member):
    pass


@__CLIENT.event
async def on_member_remove(member):
    pass


@__CLIENT.command(pass_context=True)
async def help(ctx):
    embedded_help_msg = discord.Embed(colour=discord.Colour.blue())
    embedded_help_msg.set_author(name="Agent_Doug")
    embedded_help_msg.add_field(name=" ", value="Agent_Doug is a general purpose Bot", inline=True)
    await ctx.send("", embed=embedded_help_msg)


# @__CLIENT.command()
# async def add(ctx, left: int, right: int):
#     """Adds two numbers together."""
#     await ctx.send(left + right)


if __name__ == '__main__':
    set_up_logger()
    __CLIENT.run(receive_token())
