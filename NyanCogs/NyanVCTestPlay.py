import discord
import asyncio
import youtube_dl
import os
from discord.ext import commands
from discord import opus

class NyanVCTestPlay:
	def __init__(self, bot):
		self.bot = bot
		discord.opus.load_opus("libopus.so.0")

	@commands.command(name='youtube', pass_context=True)
	@asyncio.coroutine
	async def _youtube(self, ctx):
		server = ctx.message.server
		voicebot = client.voice_client_in(message.server)
		print("Voicebot ",voicebot)
		channel = voicebot.channel
		print("Channel ",channel)		
		voice = self.bot.join_voice_channel(channel)
		player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=d62TYemN6MQ')
		player.start()
	
	@commands.command(name='testplay', pass_context=True)
	@asyncio.coroutine
	async def _join_voice_channel(self, ctx):
		server = ctx.message.server
		voicebot = self.bot.voice_client_in(server)
		channel = voicebot.channel
		print(channel)
		try:
			await self.bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player('cool.mp3')
			player.start()
		except:
			pass
		
def setup(bot):
	bot.add_cog(NyanVCTestPlay(bot))