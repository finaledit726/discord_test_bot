import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import typing
import os

Client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix='!')

chat_filter = ["BAD_WORD", "FUCK", "N-WORD", "N_WORD", "FUCKING"] #bad words
bypass_list = [] #list of roles or users how can say the bad words


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="use | !helpme | for help"))
    print("Bot is operational")

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
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "That is a bad word, dont say it again >_<")
                except discord.ext.commands.errors.CommandNotFound:
                    return
    #pat command
    if message.content.upper().startswith("!PAT"):
        await client.send_message(message.channel, "**HEY** dont you dare put your filthy hands on me! >.<")
    #help command
    if message.content.upper().startswith("!HELPME"):
        await client.send_message(message.channel, """```!sban - admin/moderator only command (more functionality to be added later)
!pat - used to pat the bot (more functionality to be added later)
!echo - used to make the bot repeat what you type after the command
!hi - say hi to the bot
!hello - say hi to the bot```""")

    if message.content.upper().startswith("!RUN"):
        await client.send_file(message.channel, '/home/owen/Downloads/discord_test_bot-master/pics/run.gif')

client.run(os.getenv('TOKEN'))
