# Import all the modules

import asyncio, sys
import json
import asyncio
import aiohttp
import json
from .gateway import Gateway
from .intents import Intents
from .http_client import HTTPClient
from models.user import ClientUser
from models.channel import Channel
from models.guild import Guild
import random
import string
import functools
import inspect
import time
import traceback
from collections import deque
import subprocess, functools
import logging

class Bot:
	"""
	A class for discord bots.
	
	Attributes
    ----------	
	
	token : str
		The token for the bot.
	intents : int
		The priveliged intents.
	command_prefix : str
		The command prefix for the bot.	
	"""
	def __init__(self, token : str, *, command_prefix : str = None, intents : int = 0, log_info : bool = False):
		self.http = HTTPClient(str(token))
		self.intents = intents
		self.cache = {}
		self.token = token
		self.logger = logging.getLogger(__name__)
		self.gateway = Gateway(self)			
		self.command_prefix = command_prefix		

	async def get_guild_data(self):
		"""
		:function:
		    
        A function to get the bot\'s guild data.
         		 				    
		"""
		call = await self.http.get("/users/@me/guilds")
		return call		
						
	async def get_user_data(self):
		"""
		:function:
		    
        A function to get the bot\'s user data.
         		 				    
		"""
		call = await self.http.get("/users/@me")
		return call       
				
	async def fetch_channel(self, id : int):
		"""
		:function:
		    
        A function to fetch a channel.

        .. note::
            This is an API call, not from the bots cache.	 				    		 				    
		"""
		if id in self.cache:
		    return self.cache[str(id)]
		call = await self.http.get("/users/@me")
		return call		        
		  
               	           
	def init(self):
		"""
		:function:
		
		This function initializes the bot to have its attributes.		 
		"""	
		user = asyncio.get_event_loop().run_until_complete(self.get_user_data())
		guilds = asyncio.get_event_loop().run_until_complete(self.get_guild_data())
		self.user = ClientUser(user)
		self.guilds = []
		for g in guilds:
		    self.guilds.append(Guild(g))
	
	async def close(self):
		"""
		:function:
			
		The function to close the websocket connection.
		"""
		
		await self.gateway.close()


	def run(self):
		"""
		:function:
			
		A function to run the bot.
		
		.. warning::
		    This is a blocking function, so if you try to run any code after this function, it won\'t run.
		"""
		payload = self.gateway.connect(str(self.token), self.intents)
		payload						