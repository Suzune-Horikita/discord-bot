import discord
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix='\\')

@bot.event
async def on_ready():
    print("Bot is Online")

bot.run('NjQ1NDk1Nzk0NTQ3NTU2MzU0.XeHKDw.DODvoH3CsBUK2pHD9t7NKXlOr8c')
