import discord
from discord.ext import commands

class Ping:
	"""Default Cog Template"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name='ping')
	async def _ping(self):
		await self.bot.say("pong nyan~")

def setup(bot):
	bot.add_cog(Ping(bot))
