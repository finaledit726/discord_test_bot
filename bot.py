import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import typing
import random
import os

Client = discord.Client()
client = commands.Bot(command_prefix="!")
chat_filter = ["BAD_WORD", "FUCK", "N-WORD", "N_WORD", "FUCKING", "NIGGER", "BITCH", "CUNT", "BASTARD"] #bad words
bypass_list = ["538501867269783564"] #list of roles or users how can say the bad words
def __init__(self):
    self.bot = discord.Client("205411115973214208")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="use | !help | for help"))
    print("Bot is operational")

@client.event
async def on_member_join(member):
    role1 = discord.utils.get(member.server.roles, name='New_people')
    role2 = discord.utils.get(member.server.roles, name='--------------------------')
    await client.add_roles(member, role1, role2)

@client.event
async def on_message(message):
#message content filter
    await client.process_commands(message)
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not "538501867269783564" in[role.id for role in message.author.roles]:
                await client.delete_message(message)
                await client.send_message(message.channel, "That is a bad word, dont say it again >_<")

#hello usr
@client.command()
async def hello(self, ctx: discord.Member):
    """
    hello [usr] (currently broken)
    """
    userID = ctx.message.author
    await client.say("<@%s> hello" % (userID))
@client.command()
async def hi(self, ctx: discord.Member):
    """
    hello [usr] (currently broken)
    """
    userID = ctx.message.author
    await client.say("<@%s> hello" % (userID))
#pingarooney
@client.command()
async def ping(self, ctx: discord.Member):
    """
    pong (currently broken)
    """
    userID = ctx.message.author
    await client.say("<@%s> Pong!" % (userID))
#repeats what usr says
@client.command()
async def echo():
    """
    repeats what is written after the command (currently broken)
    """
    args = message.content.split(" ")
    await client.say("%s" % (" ".join(args[1:])))


#admin commands
@client.command() #kick command
async def kick(ctx, member:discord.Member=None):
    """
    used to kick members (admin only)
    """

    if "494123972074668033" or "494125159372816385" in[role.id for role in message.author.roles]:
        if not member:
            await ctx.send("Please specify a membmber")
            return
        await member.kick()
        ctx.send(f"{member.mention} got kicked")
    else:
        ctx.send("You Don't Have Permission To Use This Command")

@client.command() #ban command
async def ban(ctx, member:discord.Member=None):
    """
    used to ban members (admin only)
    """
    if "494123972074668033" or "494125159372816385" in[role.id for role in message.author.roles]:
        if not member:
            await ctx.send("Please specify a membmber")
            return
        await member.ban()
        ctx.send(f"{member.mention} got banned")
    else:
        ctx.send("You Don't Have Permission To Use This Command")


@client.command()  #pat command
async def pat():
    """
    pat the bot or another usr (pat bot only available atm)
    """
    await client.say("**HEY** dont you dare put your filthy hands on me! >.<")


@client.command()
async def blush():
    """
    you are making me blush >///<
    """
    for x in range(1):
        x = random.randint(1, 3)
        if x == 1:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_author(name='>///<')
            emb.set_image(url='https://cdn.discordapp.com/attachments/499576648782315550/538758277417271297/blush1.gif')
            await client.say(embed=emb)
        elif x == 2:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_author(name='>///<')
            emb.set_image(url='https://cdn.discordapp.com/attachments/494121558437265408/538487343477424193/blush2.gif')
            await client.say(embed=emb)
        elif x == 3:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_author(name='>///<')
            emb.set_image(url='https://cdn.discordapp.com/attachments/493845493206745099/538687715601022986/blush3.gif')
            await client.say(embed=emb)

@client.command()
async def run():
    """
    gotta run!
    """
    embed = discord.Embed(
        colour = discord.Colour.green()
    )

    embed.set_image(url='https://i.imgur.com/ImoTCU3.gif')

    await client.say(embed=embed)
    
client.run(os.getenv('TOKEN'))
