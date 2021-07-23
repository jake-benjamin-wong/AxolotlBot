import os
import sys

import discord
import re
import datetime
import random

from discord import utils
from dotenv import load_dotenv
from urllib import parse, request
import asyncio
import csv
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
        #await channel[0].send("wow i exist")
    nouns = ["tension","connection","resolution","performance","potato","description"]
    nouns_length = len(nouns)
    adjectives = ["exultant","obedient","inexpensive","feigned","supreme"]
    adjectives_length = len(adjectives)
    while True:
        try:
            time = random.randint(10,20)
            print("waiting " + str(time) + " seconds")
            await asyncio.sleep(time)
            print("Creating Channel Name...")
            channel_name = adjectives[random.randint(0, len(adjectives))] + " " + nouns[random.randint(0, len(nouns) - 1)]
            print("New name = " + channel_name)
            for server in bot.guilds:
                print("Old name: " + str(server.text_channels[0]))
                channel = server.text_channels
                await channel[0].edit(name = channel_name)
                print("changed channel name to " + str(server.text_channels[0]))
        except:
            print("oh no eror")
            e = sys.exc_info()[0]
            print("Error: "+str(e))
        finally:
            print("ah yes")
            print()


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
        print("Egg in " + message.content)
        # await message.channel.send("egg")
        # sorry

bot.run(TOKEN)
