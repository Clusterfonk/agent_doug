from discord.ext import commands
import discord
import logging
import os


from bot_action_logger import set_up_logger
from acquire_token import receive_token
from config_parser import BotConfigParser


__CONFIG_PATH = os.path.expanduser('~/.config/discord.ini')
__DOTENV_PATH = os.path.expanduser('~/.config/discord.env')
__LOG_PATH = os.path.expanduser('~/.logs/agent_doug.log')


class AgentDoug(commands.Bot):
    def __init__(self, bot_config_parser, **options):
        self.__configure_standard_parameters(bot_config_parser)
        super().__init__(bot_config_parser.get_prefix(), **options)
        self.remove_command("help")

    def __configure_standard_parameters(self, bot_config_parser):
        self.__bot_name = bot_config_parser.get_bot_name()
        self.__bot_icon_url = bot_config_parser.get_bot_icon_url()
        self.__logging_channel = bot_config_parser.get_log_channel()
        self.__default_role = bot_config_parser.get_default_role()
        self.__help_description = bot_config_parser.get_help_description()

    async def on_ready(self):
        logging.info('Started {}.'.format(self.__bot_name))

    async def assign_default_role(self, member):
        if "@everyone" in member.roles:
            await member.edit(roles=self.__default_role)

    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name=self.__logging_channel)
        await self.assign_default_role(member)
        if channel is not None:
            await channel.send(
                "{0} joined the server for the first time at {1}".format(member.display_name, member.joined_at))

    async def on_member_remove(self, member):
        pass


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    # @commands.command(pass_context=True)
    # async def help(self, ctx):
    #     embedded_help_msg = discord.Embed(colour=discord.Colour.blue(),
    #                                       description=self.__help_description)
    #     embedded_help_msg.set_author(name=self.__bot_name,
    #                                  icon_url=self.__bot_icon_url)
    #     await ctx.send("", embed=embedded_help_msg)

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embedded_help_msg = discord.Embed(colour=discord.Colour.blue(),
                                          description="self.__help_description")
        embedded_help_msg.set_author(name="self.__bot_name")
        await ctx.send("", embed=embedded_help_msg)


if __name__ == '__main__':
    set_up_logger(__LOG_PATH)
    parser = BotConfigParser(__CONFIG_PATH)
    client = AgentDoug(bot_config_parser=parser,
                       description=parser.get_bot_description(),
                       status=discord.Status.online,
                       activity=discord.Activity(name="{}help".format(parser.get_prefix()),
                                                 type=discord.ActivityType.listening))
    client.add_cog(HelpCog(client))
    client.run(receive_token(__DOTENV_PATH))
