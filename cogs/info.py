import discord
from discord.ext import commands


class Info:
    def __init__(self, bot):
        self.__bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embedded_help_msg = discord.Embed(colour=discord.Colour.blue(),
                                          description=self.__bot.help_description)
        embedded_help_msg.set_author(name=self.__bot.bot_name,
                                     icon_url=self.__bot.bot_icon_url)
        await ctx.send("", embed=embedded_help_msg)
