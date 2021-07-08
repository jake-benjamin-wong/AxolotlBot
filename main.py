import os
import discord
from dotenv import load_dotenv
from urllib import parse, request
import re
import datetime

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
  egg = "\N{EGG}"
  await message.add_reaction(egg)
  print(egg)

bot.run(TOKEN)
