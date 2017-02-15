import asyncio
import discord
import youtube_dl
import requests
import os
from discord.ext import commands
from discord import opus
from bs4 import BeautifulSoup

class NyanYoutube:
	def __init__(self, bot):
		self.bot = bot
		# discord.opus.load_opus("libopus.so.0")
	@commands.group()
	async def yt(self):
		pass
		
	@yt.command(name='play', pass_context=True)
	async def _play(self, ctx, *, url : str = None):
		await self.bot.say('Attempting to get song nyan~')
		self.opts = {"noplaylist": True}
		r = requests.get(url)
		soup = BeautifulSoup(r.text, "lxml")

		links = soup.find_all("a", class_="playlist-video")
		links = ["https://youtube.com"+link.attrs["href"] for link in links]
		
		if links != []:
			server = ctx.message.server
			self.voice = self.bot.voice_client_in(server)
			await self.playlist(links)
		else:
			server = ctx.message.server
			voice = self.bot.voice_client_in(server)
			player = await voice.create_ytdl_player(url, ytdl_options=self.opts)
			self.player = player
			await asyncio.sleep(2)
			await self.bot.say('Starting song nyan~')
			player.start()

	async def playlist(self, links):
		count = 0
		await self.bot.say('Starting playlist nyan~')
		while len(links) >= count:
			url = links[count]
			print (url)
			player = await self.voice.create_ytdl_player(url, ytdl_options=self.opts)
			self.player = player
			await asyncio.sleep(2)
			count = count + 1
			player.start()
			await asyncio.sleep(player.duration)
	
	@yt.command(name='pause')
	async def _pause(self):
		self.player.pause()
			
	@yt.command(name='resume')
	async def _resume(self):
		self.player.resume()
		
	@yt.command(name='skip')
	async def _skip(self):
		self.player.stop()
			
def setup(bot):
	bot.add_cog(NyanYoutube(bot))