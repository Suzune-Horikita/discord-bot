import discord
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Bot is Online")

bot.run('')
