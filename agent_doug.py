import discord
from discord.ext import commands
import logging

from bot_action_logger import set_up_logger
from acquire_token import receive_token

__CLIENT = commands.Bot(command_prefix='!', description='General Purpose bot',
                        status=discord.Status.online,
                        activity=discord.Activity(name="!help",
                                                  type=discord.ActivityType.listening))
__CLIENT.remove_command('help')


@__CLIENT.event
async def on_ready():
    logging.info('Started Agent Doug.')


@__CLIENT.event
async def on_member_join(member):
    channel = discord.utils.get(__CLIENT.get_all_channels(), guild_name='Birds & Co', name='nsa_channel')
    await channel.send("{} joined the server for the first time.".format(member.nick))


@__CLIENT.event
async def on_member_remove(member):
    pass


@__CLIENT.command(pass_context=True)
async def help(ctx):
    description = "Agent_Doug is a general purpose Bot"
    embedded_help_msg = discord.Embed(colour=discord.Colour.blue(), description=description)
    embedded_help_msg.set_author(name="Agent_Doug", icon_url="https://i.imgur.com/lVxcNP9.png")
    await ctx.send("", embed=embedded_help_msg)


if __name__ == '__main__':
    set_up_logger()
    __CLIENT.run(receive_token())
