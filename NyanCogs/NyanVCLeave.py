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
		server = ctx.message.server
		print("Attempting ot leave voice channel in Sever: ",server)
	
		voicebot = self.bot.voice_client_in(server)
		print("Voicebot ",voicebot)
		await self.bot.say("Leaving channel nyan~")
		await voicebot.disconnect()
			
		DidConnect = self.bot.is_voice_connected(server)
		if DidConnect is False:
			print('Successfully disconnected from voice channel in server: ',server)
			await self.bot.say('Successfully disconnected from voice channel nyaa~')
		else:
			print('Failed to disconnect from voice channel in server: ',server)
			await self.bot.say('Failed to disconnected from voice channel nyaa~')
			
def setup(bot):
	bot.add_cog(NyanMusic(bot))
