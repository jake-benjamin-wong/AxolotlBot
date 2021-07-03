import os
import discord
from dotenv import load_dotenv

from discord.ext import commands

# load token (dont share pls)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

# Is this better?
bot = commands.Bot(command_prefix='$', description="This is a test bot")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# commands here

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


bot.run(TOKEN)
