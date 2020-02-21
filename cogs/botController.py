import discord
from discord.ext import commands
import subprocess


class BotController(commands.Cog):

    def __init__(self, client):
        self.client = client



    # -----------------------------------------------------
    # - -------RESTRICTED COMMAND ADMIN ONLY---------------
    # - Purpose: Shutsdown the bot
    # - Parameters:
    # -     ctx = context (aut defined by program)
    # -----------------------------------------------------

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):

        #Discord Messages
        await (ctx.bot.logout())




    # -----------------------------------------------------
    # - -------RESTRICTED COMMAND ADMIN ONLY---------------
    # - Purpose: Restarts the bot
    # - Parameters:
    # -     ctx = context (aut defined by program)
    # -----------------------------------------------------


    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):

        #Discord Messages
        await (ctx.send("Bot is restarting..."))
        await (ctx.bot.logout())

        #Start a batch file to start the bot
        subprocess.call([r'C:\\Users\\Richard\\PycharmProjects\\DNDBot\\startbot.bat'])




def setup(client):
    client.add_cog(BotController(client))