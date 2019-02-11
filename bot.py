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
bot = commands.Bot(commands.when_mentioned_or('!'))
chat_filter = ["BAD_WORD", "FUCK", "N-WORD", "N_WORD", "FUCKING", "NIGGER", "BITCH", "CUNT", "BASTARD"] #bad words
bypass_list = ["538501867269783564"] #list of roles or users who can say the bad words
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
@bot.command()
async def hello():
    """
    hello [usr] (in development)
    """
    await bot.say("hello")
    
#pingarooney
@client.command(pass_context=True)
async def ping(ctx):
    """Pong!"""
    now = datetime.datetime.utcnow()
    delta = now-ctx.message.timestamp
    await client.say('Pong! = {}ms'.format(delta(microseconds=1)))



    
#repeats what usr says
@client.command()
async def echo():
    """
    repeats what is written after the command (currently broken)
    """
    args = message.content.split(" ")
    await client.say("%s" % (" ".join(args[1:])))

    
@client.command() #neko command(needs to be in cog!!)
async def neko():
    """cute nekos >///< (36 different nekos)"""
    for n in range(1):
        n = random.randint(1,36)
        if n == 1:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_157.jpg')
            await client.say(embed=emb)
        if n == 2:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_158.jpg')
            await client.say(embed=emb)
        if n == 3:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_159.jpg')
            await client.say(embed=emb)
        if n == 4:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_160.jpg')
            await client.say(embed=emb)
        if n == 5:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_161.jpg')
            await client.say(embed=emb)
        if n == 6:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_165.jpg')
            await client.say(embed=emb)
        if n == 7:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_166.jpg')
            await client.say(embed=emb)
        if n == 8:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_167.jpg')
            await client.say(embed=emb)
        if n == 9:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_169.jpg')
            await client.say(embed=emb)
        if n == 10:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_170.jpg')
            await client.say(embed=emb)

        if n == 11:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_171.jpg')
            await client.say(embed=emb)
        if n == 12:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_172.jpg')
            await client.say(embed=emb)
        if n == 13:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_173.jpg')
            await client.say(embed=emb)
        if n == 14:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_174.jpg')
            await client.say(embed=emb)
        if n == 15:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_176.jpg')
            await client.say(embed=emb)
        if n == 16:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_179.jpg')
            await client.say(embed=emb)
        if n == 17:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_182.jpg')
            await client.say(embed=emb)
        if n == 18:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_183.jpg')
            await client.say(embed=emb)
        if n == 19:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_184.jpg')
            await client.say(embed=emb)
        if n == 20:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_185.jpg')
            await client.say(embed=emb)

        if n == 21:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_186.jpg')
            await client.say(embed=emb)
        if n == 22:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_187.jpg')
            await client.say(embed=emb)
        if n == 23:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_188.jpg')
            await client.say(embed=emb)
        if n == 24:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_189.jpg')
            await client.say(embed=emb)
        if n == 25:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_190.jpg')
            await client.say(embed=emb)
        if n == 26:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_191.jpg')
            await client.say(embed=emb)
        if n == 27:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_195.jpg')
            await client.say(embed=emb)
        if n == 28:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_196.jpg')
            await client.say(embed=emb)
        if n == 29:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_197.jpg')
            await client.say(embed=emb)
        if n == 30:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_198.jpg')
            await client.say(embed=emb)

        if n == 31:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_199.jpg')
            await client.say(embed=emb)
        if n == 32:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_200.jpg')
            await client.say(embed=emb)
        if n == 33:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_207.jpg')
            await client.say(embed=emb)
        if n == 34:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_209.jpg')
            await client.say(embed=emb)
        if n == 35:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_211.jpg')
            await client.say(embed=emb)
        if n == 36:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_image(url='https://cdn.nekos.life/neko/neko_212.jpg')
            await client.say(embed=emb)
            
            

#admin commands
@client.command()  #kick command
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    """
    (admin command) kick [usr] (currently broken)
    """
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.kick()
    await ctx.send(f"{member.mention} got kicked")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You Don't Have Permission To Use This Command")

@client.command() #ban command
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    """
    (admin command) ban [usr] (currently broken)
    """
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.ban()
    await ctx.send(f"{member.mention} got banned")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You Don't Have Permission To Use This Command")


@client.command()  #pat command
async def pat(ctx, member:discord.Member = None):
    """
    pat the bot or another usr (currently broken)
    """
    if not member:
        await ctx.send("**HEY** dont you dare put your filthy hands on me! >.<")
        return

    for x in range(1):
        x = random.randint(1,1)
        if x == 1:
            pat = discord.Embed(colour = discord.Colour.green())
            pat.set_author(name=f'{member.mention} got patted')
            pat.set_image(url='https://github.com/finaledit726/discord_test_bot/blob/master/pics/pat/pat1.gif')
            await ctx.send(embed=pat)

@client.command() #blush command
async def blush():
    """
    you are making me blush >///<
    """
    for x in range(1):
        x = random.randint(1, 5)
        if x == 1:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_author(name='>///<')
            emb.set_image(url='https://github.com/finaledit726/discord_test_bot/blob/master/pics/blush/blush1.gif')
            await client.say(embed=emb)
        elif x == 2:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_author(name='>///<')
            emb.set_image(url='https://github.com/finaledit726/discord_test_bot/blob/master/pics/blush/blush2.gif')
            await client.say(embed=emb)
        elif x == 3:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_author(name='>///<')
            emb.set_image(url='https://github.com/finaledit726/discord_test_bot/blob/master/pics/blush/blush3.gif')
            await client.say(embed=emb)
        elif x == 4:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_author(name='>///<')
            emb.set_image(url='https://github.com/finaledit726/discord_test_bot/blob/master/pics/blush/blush4.gif')
            await client.say(embed=emb)
        elif x == 5:
            emb = discord.Embed(colour = discord.Colour.green())
            emb.set_author(name='>///<')
            emb.set_image(url='https://github.com/finaledit726/discord_test_bot/blob/master/pics/blush/blush5.gif')
            await client.say(embed=emb)



            

@client.command() #run command
async def run():
    """
    gotta run!
    """
    embed = discord.Embed(
        colour = discord.Colour.green()
    )

    embed.set_image(url='https://github.com/finaledit726/discord_test_bot/blob/master/pics/run/run1.gif')

    await client.say(embed=embed)
    
client.run(os.getenv('TOKEN'))
