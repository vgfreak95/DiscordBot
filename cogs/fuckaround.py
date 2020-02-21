import discord
from discord.ext import commands
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import DNDBot
from DNDBot import cursor

class FuckAround(commands.Cog):

    def __init__(self, client):
        self.client = client


    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')


    

    # -----------------------------------------------------
    # - Purpose: Returns what channel the user is in and what guild(Server) they are in
    # - Parameters:
    # -     ctx = context (aut defined by program)
    # -----------------------------------------------------
        
    @commands.command(aliases=['channel'])
    async def channel_info(self, ctx):
        name = ctx.message.channel #returns the current channel that you are in.
        guildname = ctx.message.guild #returns the current server that you are in.

        #Discord messages
        await (ctx.send("The channel name is: " + str(name) + " in server: " + str(guildname)))



    
    # -----------------------------------------------------
    # - -------RESTRICTED COMMAND ADMIN ONLY---------------
    # - Purpose: Creates a channel in the default section
    # - Parameters:
    # -     ctx = context (aut defined by program)
    # -     channelname = What you would like the channel name to be
    # -----------------------------------------------------

    @commands.command()
    @commands.is_owner()
    async def create_channel(self, ctx, channelname):
        guild = ctx.message.guild
        await (guild.create_text_channel(f'{channelname}'))




    # -----------------------------------------------------
    # - Purpose: Test the Embed in discord
    # - Parameters:
    # -     ctx = context (aut defined by program)
    # -----------------------------------------------------

    @commands.command(aliases=['embed'])
    async def embedpleasework(self, ctx):
        embed = discord.Embed(
            title = 'Hello there this is my first embed',
            description = 'Please work for me lol',
        )
        await (ctx.send(embed=embed))




    # -----------------------------------------------------
    # - -------RESTRICTED COMMAND ADMIN ONLY---------------
    # - Purpose: This allows the user to check to entire character database
    # - Parameters:
    # -     ctx = context (aut defined by program)
    # -----------------------------------------------------

    check_db_desc = 'This checks the current characters that exist.'
    @commands.command(aliases=['check_db'], description=check_db_desc)
    async def check_character_db(self, ctx):
        user_id = ctx.message.author.id
        cursor.execute(f"SELECT * FROM characters WHERE user_id={user_id}")
        myresult = cursor.fetchall()
        for x in myresult:
            embed = discord.Embed(
                title='--------Character Information-----------',
                description=f'''
    First Name: {x[0]}
    Last Name: {x[1]}
    Strength: {x[2]}
    Dexterity: {x[3]}
    Constitution: {x[4]}
    Intelligence: {x[5]}
    Wisdom: {x[6]}
    Charisma: {x[7]}''')

        await(ctx.send(embed=embed))    





def setup(client):
    client.add_cog(FuckAround(client))