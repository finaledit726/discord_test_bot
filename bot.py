import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import typing
import random
import os

Client = discord.Client()
client = commands.Bot(command_prefix=" ")

chat_filter = ["BAD_WORD", "FUCK", "N-WORD", "N_WORD", "FUCKING", "NIGGER", "BITCH", "CUNT", "BASTARD"] #bad words
bypass_list = ["538501867269783564"] #list of roles or users how can say the bad words


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="use | !helpme | for help"))
    print("Bot is operational")

@client.event
async def on_member_join(member):
    role1 = discord.utils.get(member.server.roles, name='New_people')
    role2 = discord.utils.get(member.server.roles, name='--------------------------')
    await client.add_roles(member, role1, role2)

@client.event
async def on_message(message):
#hello usr
    if message.content == "!hello":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> hello" % (userID))
    if message.content == "!hi":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> hello" % (userID))
#pingarooney
    if message.content.upper().startswith("!PING"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
#repeats what usr says
    if message.content.upper().startswith("!ECHO"):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
#base of admin commands
    if message.content.upper().startswith("!ABAN"):
        if "494123972074668033" or "494125159372816385" in[role.id for role in message.author.roles]:
            await client.send_message(message.channel, "feature not yet available")

        else:
            await client.send_message(message.channel, "you do not have permission to use this command")
#message content filter
    await client.process_commands(message)
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not "538501867269783564" in[role.id for role in message.author.roles]:
                await client.delete_message(message)
                await client.send_message(message.channel, "That is a bad word, dont say it again >_<")
    #pat command
    if message.content.upper().startswith("!PAT"):
        await client.send_message(message.channel, "**HEY** dont you dare put your filthy hands on me! >.<")
    #help command
    if message.content.upper().startswith("!HELPME"):
        await client.send_message(message.channel, """```
!sban - admin/moderator only command
(more functionality to be added later)

!pat - used to pat the bot & other users
(more functionality to be added later)

!echo - used to make the bot repeat what you type after the command

!hi - say hi to the bot

!hello - say hi to the bot

!blush - you're making me blush >///<

!run - gotta run

V = 0.02
```""")

    if message.content.upper().startswith("!RUN"):
        await client.send_file(message.channel, '/home/owen/github/.git/discord_bot/pics/run/run1.gif')


    if message.content.upper().startswith("!BLUSH"):
        for x in range(1):
            x = random.randint(1, 3)
            if x == 1:
                await client.send_file(message.channel, 'https://github.com/finaledit726/discord_test_bot/blob/master/pics/blush/blush1.gif')
            elif x == 2:
                await client.send_file(message.channel, 'https://github.com/finaledit726/discord_test_bot/blob/master/pics/blush/blush2.gif')
            elif x == 3:
                await client.send_file(message.channel, 'https://github.com/finaledit726/discord_test_bot/blob/master/pics/blush/blush3.gif')

client.run(os.getenv('TOKEN'))
