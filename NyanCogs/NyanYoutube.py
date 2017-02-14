import asyncio
import discord
import youtube_dl
import os
from discord.ext import commands
from discord import opus

class NyanYoutube:
	def __init__(self, bot):
		self.bot = bot
		# discord.opus.load_opus("libopus.so.0")
	@commands.group()
	async def yt(self):
		pass
		
	@yt.command(name='play', pass_context=True)
	async def _play(self, ctx):
		server = ctx.message.server
		voice = self.bot.voice_client_in(server)
		url = ctx.message.content[len('!!yt play'):].strip()
		player = await voice.create_ytdl_player(url)
		self.player = player
		await asyncio.sleep(1)
		player.start()
	
	@yt.command(name='pause')
	async def _pause(self):
		self.player.pause()
			
	@yt.command(name='resume')
	async def _resume(self):
		self.player.resume()
			
def setup(bot):
	bot.add_cog(NyanYoutube(bot))