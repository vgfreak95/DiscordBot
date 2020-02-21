import discord
from discord.ext import commands
import random
import DNDBotAPI
import mysql.connector
import os
import subprocess

cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='dndcharacters',
                              auth_plugin='mysql_native_password')
cursor = cnx.cursor()

client = commands.Bot(command_prefix = '!')

isBotOn = True

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')




# -----------------------------------------------------
# - Purpose: Rolls Dice 
# - Parameters: 
# -     ctx = context (aut defined by program)
# -     amount = the amount of dice you would like to roll
# -     dice_type = the sided dice you would like to roll (ex: 20)
# -----------------------------------------------------

roll_description = 'This command rolls dice. Input the amount and type of dice. \nExample: !roll 2 20'
@client.command(aliases=['roll'], description=roll_description)
async def roll_dice(ctx, amount, dice_type):
    for x in range(int(amount)):
        dice = DNDBotAPI.roll_dice(amount, dice_type)
        await (ctx.send("You roll: " + str(dice)))




# -----------------------------------------------------
# - Purpose: Automatically rolls a character for you
# - Parameters:
# -     ctx = context (aut defined by program)
# -     firstname = the first name of the character you are creating
# -     lastname = the last name of the character you are creating
# -----------------------------------------------------

character = 'This command rolls a new character. Input the name and last name of character. \nExample: !roll_character Quentin Redman'
@client.command(aliases=['rc'], description=character)
async def roll_character(ctx, firstname, lastname):
    userid = ctx.message.author.id
    dice = DNDBotAPI.roll_character()
    embed = discord.Embed(
        title='--------Rolled Character-----------',
        description=f'''
            First Name: {firstname}
            Last Name: {lastname}
            Strength: {dice[0]}
            Dexterity: {dice[1]}
            Constitution: {dice[2]}
            Intelligence: {dice[3]}
            Wisdom: {dice[4]}
            Charisma: {dice[5]}''')
    await (ctx.send(embed=embed))

    sql_statement = f"INSERT INTO characters VALUES ('{firstname}', '{lastname}', {dice[0]}, {dice[1]}, {dice[2]}, {dice[3]}, {dice[4]}, {dice[5]}, {userid});"
    cursor.execute(sql_statement)
    cnx.commit()




# -----------------------------------------------------
# - Purpose: Deletes an existing character
# - Parameters:
# -     ctx = context (aut defined by program)
# -     first = The first name of the character you would like to delete
# -     last = The lsat name of the character you would like to delete
# -----------------------------------------------------

@client.command(aliases=['del_char'])
async def del_character(ctx, first, last):

    user_id = ctx.message.author.id
    cursor.execute(f"SELECT user_id FROM characters WHERE first='{first}' AND last='{last}';")
    result = cursor.fetchone()
    cnx.commit()
    result_id = result[0]

    if (user_id != int(result_id)):
        await(ctx.send(f"You do not have access to this character."))

    else:
        cursor.execute(f"DELETE FROM characters WHERE first='{first}' AND last='{last}';")
        cnx.commit()
        await(ctx.send(f"Character {first} {last} was deleted."))




# -----------------------------------------------------
# - Purpose: Swaps values given for a given character
# - Parameters:
# -     ctx = context (aut defined by program)
# -     first = first name of the character
# -     last = last name of the character
# -     att1 = the first attribute that you would like to change (ex: dexterity)
# -     att2 = the second attribute that you would like to change (ex: strength)
# -----------------------------------------------------

@client.command(aliases=['swap'])
async def swap_values(ctx, first, last, att1, att2):


    # Retrieve values from the SQL Database from the given first attribute (ex: strength)
    cursor.execute(f"SELECT {att1} FROM characters WHERE first='{first}' AND last='{last}';")
    first_result = cursor.fetchone()
    first_value = first_result[0]

    # Retrieve values from the SQL Database from the given second attribute (ex: dexterity)
    cursor.execute(f"SELECT {att2} FROM characters WHERE first='{first}' AND last='{last}';")
    second_result = cursor.fetchone()
    second_value = second_result[0]

    #Update the existing database and change the values
    cursor.execute(f"UPDATE characters SET {att1}={second_value} WHERE first='{first}' AND last='{last}';")
    cnx.commit()

    #Update the existing database and change the values
    cursor.execute(f"UPDATE characters SET {att2}={first_value} WHERE first='{first}' AND last='{last}';")
    cnx.commit()

    #Put in the discord messages
    await(ctx.send(f"You have swapped your {att1} and {att2}."))
    await(stats(ctx, first, last))




# -----------------------------------------------------
# - Purpose: Swaps values given for a given character
# - Parameters:
# -     ctx = context (aut defined by program)
# -     first = first name of the character
# -     last = last name of the character
# -     att1 = the first attribute that you would like to change (ex: dexterity)
# -     att2 = the second attribute that you would like to change (ex: strength)
# -----------------------------------------------------

@client.command(aliases=['reroll'])
async def reroll_char(ctx, first, last, att1, att2):

    user_id = ctx.message.author.id
    cursor.execute(f"SELECT user_id FROM characters WHERE first='{first}' AND last='{last}';")
    user_array = cursor.fetchone()
    user_result = user_array[0]

    old_first = None
    old_second = None

    cursor.execute(f"SELECT {att1}, {att2} FROM characters WHERE first='{first}' AND last='{last}';")
    results = cursor.fetchall()

    for x in results:
        old_first = x[0]
        old_second = x[1]
    new_first = 0
    new_second = 0
    new_array_one = []
    new_array_two = []
    for x in range(4):
        new_first = DNDBotAPI.roll_dice(4, 6)
        new_array_one.append(new_first)

        new_second = DNDBotAPI.roll_dice(4, 6)
        new_array_two.append(new_second)

    new_first = DNDBotAPI.array_total(new_array_one) - DNDBotAPI.find_lowest(new_array_one)
    new_second = DNDBotAPI.array_total(new_array_two) - DNDBotAPI.find_lowest(new_array_two)

    cursor.execute(f"UPDATE characters SET {att1} = {new_first}, {att2} = {new_second} WHERE first='{first}' AND last='{last}';")
    cnx.commit()

    embed = discord.Embed(
        title='--------Character ReRoll-----------',
        description=f'''
{att1} = {old_first} {att2} = {old_second}
{att1} = {new_first} {att2} = {new_second}
''')

    if (user_id != int(user_result)):
        await(ctx.send("You are not the owner of this character!"))

    else:
        await(ctx.send(embed=embed))




# -----------------------------------------------------
# - Purpose: Swaps values given for a given character
# - Parameters:
# -     ctx = context (aut defined by program)
# -     first = first name of the character
# -     last = last name of the character
# -     att1 = the first attribute that you would like to change (ex: dexterity)
# -     att2 = the second attribute that you would like to change (ex: strength)
# -----------------------------------------------------

@client.command(aliases=['char'])
async def stats(ctx, first, last):
    #Return an integer value
    user_id = ctx.message.author.id

    cursor.execute(f"SELECT * FROM characters WHERE first='{first}' AND last='{last}'")
    results = cursor.fetchall()
    for x in results:

        embed = discord.Embed(
        title=f'{first} {last} stats:',
        description=f'''
Strength = {x[2]}
Dexterity = {x[3]}
Constitution = {x[4]}
Intelligence = {x[5]}
Wisdom = {x[6]}
Charisma = {x[7]}
''')

        await(ctx.send(embed=embed))


client.run('Njc2OTc3MjI1NzgyMDAxNjY1.XkNiNg.DOsjZ45JiVtnNSmnrejCJFVMOvQ');
