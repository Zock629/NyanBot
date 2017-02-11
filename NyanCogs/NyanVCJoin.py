import discord
import asyncio
from discord.ext import commands

class NyanMusic:
	"""Default Cog Template"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name='join', pass_context=True)
	@asyncio.coroutine
	async def _join(self, ctx):
		server = ctx.message.server
		IfConnected = self.bot.is_voice_connected(server)
		print(IfConnected)
		if IfConnected == False:
			count = 0											 # Sets count to 0
			for channel in server.channels:						 # Loops for all of the channels within the server											[Used to get the amount of channels in the server]
				count = count + 1								 # Adds 1 to count																			[Used to get the amount of channels in the server]
			print("There are ",count," channels in the server ",server)
			
			size = count										 # Sets size to count
			channels = [size]									 # Array called channels made to hold the channel names of the server
			channeltype = [size]								 # Array called channelids made to hold the channel types of the channels on the server
			
			count = 0											 # Sets count back to 0
			for channel in server.channels:
				channels.append(0)
				channels[count] = channel						 # Writes the channel names to the arrray
				# print("Channel ",count + 1," ",channels[count])
				count = count + 1
					
			count = 0											 # Sets count back to 0
			for channel in server.channels:
				channeltype.append(0)
				channeltype2 = channel.type
				channeltype[count] = channeltype2			 # Writes the channel ids to the arrray
				# print("Channel Type for ",count + 1," ",channeltype[count])
				count = count + 1
			
			userinput = ctx.message.content[len('!!join'):].strip()	 # Strips !!join from users message
			
			count = 0
			while count <= size - 1:
				if channels[count].name.lower() == userinput.lower() and channeltype[count] == discord.ChannelType.voice:
					channelnum = count
				
				count = count + 1
			
			await self.bot.say("Joining channel nyan~")
			await self.bot.join_voice_channel(channels[channelnum])
			
			try:
				DidConnect = self.bot.is_voice_connected(server)	 # Checks if the voice client is connected to the server
				if DidConnect:
					print('Successfully connected to voice channel in ', channels[channelnum], 'on server:', server)
					await self.bot.say('Successfully connected to voice channel nyan~')
			except:
				print('Failed connected to voice channel in channel:', channels[channelnum], 'on server:', server)
				await self.bot.say('Failed connected to voice channel nyan~')
				pass	
		else:
			await self.bot.say('Please use !!leave first nyan~')
		
def setup(bot):
	bot.add_cog(NyanMusic(bot))
