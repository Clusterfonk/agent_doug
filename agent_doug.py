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
    description = "Agent_Doug is a general purpose Bot"
    embedded_help_msg = discord.Embed(colour=discord.Colour.blue(), description=description)
    embedded_help_msg.set_author(name="Agent_Doug", icon_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette.wikia.nocookie.net%2Fuglyamericans%2Fimages%2Fe%2Fe6%2FDoug.jpg%2Frevision%2Flatest%3Fcb%3D20110307123143&f=1&nofb=1")
    await ctx.send("", embed=embedded_help_msg)


# @__CLIENT.command()
# async def add(ctx, left: int, right: int):
#     """Adds two numbers together."""
#     await ctx.send(left + right)


if __name__ == '__main__':
    set_up_logger()
    __CLIENT.run(receive_token())
