import discord
import youtube_dl
import os
from discord.ext import commands
from discord import opus

class NyanVCTestPlay:
	def __init__(self, bot):
		self.bot = bot
		# discord.opus.load_opus("libopus.so.0")

	@commands.command(name='play', pass_context=True)
	async def _play(self, ctx):
		server = ctx.message.server
		voice = self.bot.voice_client_in(server)
		channel = voice.channel
		player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=EqbGLXZBaBM')
		player.start()
	
	@commands.command(name='playren', pass_context=True)
	async def _join_voice_channel(self, ctx):
		server = ctx.message.server
		voice = self.bot.voice_client_in(server)
		channel = voice.channel
		player = voice.create_ffmpeg_player('cool.mp3')
		player.start()
			
def setup(bot):
	bot.add_cog(NyanVCTestPlay(bot))