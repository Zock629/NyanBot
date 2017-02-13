import asyncio
import discord
from discord.ext import commands

class Nyan:
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name='ping')
	async def _ping(self):
		await self.bot.say("pong nyan~")

def setup(bot):
	bot.add_cog(Nyan(bot))
