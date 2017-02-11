import discord
import asyncio
from discord.ext import commands

class NyanMusic:
	"""Default Cog Template"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name='leave', pass_context=True)
	@asyncio.coroutine
	async def _join(self, ctx):
		await self.bot.say("Leaving channel nyan~")
		
		
def setup(bot):
	bot.add_cog(NyanMusic(bot))
