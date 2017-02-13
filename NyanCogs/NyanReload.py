import asyncio
import discord
import os
from discord.ext import commands

class NyanReload:
	def __init__(self, bot):
		self.bot = bot
	
	@commands.group()
	async def cogs(self):
		pass
	
	@cogs.command(name='reload', hidden=True, pass_context=True)
	async def _reload(self, ctx, *, cogs : str = None):
		await self.bot.say('-----Reloading Cogs-----')
		print('-----Reloading Cogs-----')
		if cogs != None:
			cogs = cogs.split(" ")
		elif cogs == None:
			cogs = [n for n in os.listdir("./NyanCogs") if os.path.isfile(os.path.join("./NyanCogs", n))]

		temp = [cog for cog in cogs]
		for cog in cogs:
			self.bot.unload_extension("NyanCogs."+cog.replace('.py',''))
		print("Unloaded: {}".format(", ".join(temp)))
		print(temp)
		del temp
		await asyncio.sleep(1)
		cogload = []
		notload = []
		for cog in cogs:
			rempy = cog.replace('.py','')
			try:
				self.bot.load_extension("NyanCogs."+rempy)
			except ImportError:
				await self.bot.say("`{}` is not a cog or it doesn't exist".format(rempy))
				notload.append(rempy)
			except Exception as e:
				notload.append(rempy)
				if (len(cogs) == 1):
					raise
			else:
				cogload.append(rempy)
		temp = []
		if len(cogload) != 0:
			msgnotload = '**Cogs Reloaded:** `{}`'.format(", ".join(cogload))
			temp.append(msgnotload)
		if len(notload) != 0:
			msgloaded = '**Cogs Not Loaded:** `{}`'.format(", ".join(notload))
			temp.append(msgloaded)
		await self.bot.say(" | ".join(temp))
		print(" | ".join(temp))
		del temp

def setup(bot):
	bot.add_cog(NyanReload(bot))
