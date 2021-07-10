import os
import discord
import re
import datetime

from discord import utils
from dotenv import load_dotenv
from urllib import parse, request


from discord.ext import commands

# load token (dont share pls)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

# Is this better?
bot = commands.Bot(command_prefix='!', description="This is a test bot")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game("Use !help"))
    servers = bot.guilds
    for server in bot.guilds:
        channel = server.text_channels
        await channel[0].send("wow i exist")


# commands here
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def youtube(ctx, *, search,):
    await ctx.send("finding video pls wait")
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    print(query_string)
    #print(html_content.read().decode())
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@bot.listen()
async def on_message(message):
    if "egg" in message.content.lower():
        await message.add_reaction("\N{EGG}")
        await message.send("egg")

bot.run(TOKEN)
