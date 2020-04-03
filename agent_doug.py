from discord.ext import commands
import discord
import logging
import os


from bot_action_logger import set_up_logger
from acquire_token import receive_token
from cogs.info import Info
from config_parser import BotConfigParser


__CONFIG_PATH = os.path.expanduser('~/.config/discord.ini')
__DOTENV_PATH = os.path.expanduser('~/.config/discord.env')
__LOG_PATH = os.path.expanduser('~/.logs/agent_doug.log')


class AgentDoug(commands.Bot):
    def __init__(self, bot_config_parser, **options):
        self.__configure_standard_parameters(bot_config_parser)
        super().__init__(bot_config_parser.get_prefix(), **options)
        self.__add_cogs()

    def __configure_standard_parameters(self, bot_config_parser):
        self.bot_name = bot_config_parser.get_bot_name()
        self.bot_icon_url = bot_config_parser.get_bot_icon_url()
        self.__logging_channel = bot_config_parser.get_log_channel()
        self.__new_member_role_id = bot_config_parser.get_new_member_role_id()
        self.__default_role_id = bot_config_parser.get_default_role_id()
        self.help_description = bot_config_parser.get_help_description()

    def __add_cogs(self):
        self.add_cog(Info(self))

    async def on_ready(self):
        logging.info('Started {}.'.format(self.bot_name))

    async def assign_default_role(self, member):
        print(self.__default_role_id in [m.id for m in member.roles])
        if self.__default_role_id in [m.id for m in member.roles]:
            print("member being edited")
            await member.edit(roles= discord.utils.get(member.guild.roles, id=self.__new_member_role_id))

    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name=self.__logging_channel)
        await self.assign_default_role(member)
        if channel is not None:
            await channel.send(
                "{0} joined the server for the first time at {1}".format(member.display_name, member.joined_at))

    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name=self.__logging_channel)
        if channel is not None:
            await channel.send(
                "{0} left the server at {1}".format(member.display_name, member.joined_at))


if __name__ == '__main__':
    set_up_logger(__LOG_PATH)

    parser = BotConfigParser(__CONFIG_PATH)

    client = AgentDoug(bot_config_parser=parser,
                       description=parser.get_bot_description(),
                       help_command=None,
                       status=discord.Status.online,
                       activity=discord.Activity(name="{}help".format(parser.get_prefix()),
                                                 type=discord.ActivityType.listening))
    client.run(receive_token(__DOTENV_PATH))
