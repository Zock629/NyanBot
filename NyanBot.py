import discord
import asyncio
import os
from os import listdir
from os.path import isfile, join
from discord.ext import commands

desc = "NyanBot is a bot coded in Python"
bot = commands.Bot(command_prefix="!!", description=desc, pm_help=True)

@bot.event
async def on_ready():
	print('-' * 20)
	print("NyanBot Launched")
	print(bot.user.id)
	print('-' * 20)
	mypath = './NyanCogs'
	NyanCogs = [CogFiles for CogFiles in listdir(mypath) if isfile(join(mypath, CogFiles))]
	for cog in NyanCogs:
		Nyu = 'NyanCogs.' + cog.replace('.py', '')
		bot.load_extension(Nyu)
		
@bot.event
@asyncio.coroutine
async def on_message(message):
        await bot.process_commands(message)
	
with open("token.txt", "r") as file:
	token = file.read().strip()

bot.run(token)