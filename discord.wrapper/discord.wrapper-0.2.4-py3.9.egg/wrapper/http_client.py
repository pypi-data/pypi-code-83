import aiohttp, asyncio, json, sys, os
from pathlib import Path

if __name__ == '__main__' and __package__ is None:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[3]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass
        
    __package__ = '.'



from . import __version__



class HTTPClient:
	"""Represents an http client sending requests to discord."""
	
	def __init__(self, token : str):
		
						
		self.__session = aiohttp.ClientSession()
		self.BASE = "https://discordapp.com/api/v6"
		user_agent = 'DiscordBot (https://github.com/FrostiiWeeb/discord.wrapper {0}) Python/{1[0]}.{1[1]} aiohttp/{2}'
		self.user_agent = user_agent.format(__version__, sys.version_info, aiohttp.__version__)
		self.token = str(token)		
		self.headers = {
		"Authorization": "Bot {}".format(self.token),
		"User-Agent": self.user_agent,
		"Content-Type": "application/json"
		}
		
	async def get(self, endpoint, **kwargs):	
			
			async with self.__session.get(self.BASE + endpoint, headers=self.headers) as resp:
			    return await resp.json()
			    
	async def post(self, endpoint, **kwargs):
			
			data = kwargs.pop("data", None)
			
			async with self.__session.post(self.BASE + endpoint, headers=self.headers, data=data) as resp:
			    return await resp.json()			    
			
	async def send_message(self, channel_id=None, content=None):
		"""
		Sends a message to discord.
		"""
		
		data = {
		"content": content,
		}		
		
		return await self.post(f"/channels/{channel_id}/messages", data=data)
					
		
	async def fetch_message(self, channel_id : int, message_id : int):
		"""
		Fetches a channel from discord.
		
		channel_id : int
			The channel id to fetch.
		message_id : int
			The message id to fetch.			
		"""
		
		return await self.get("/channels/{channel_id}/messages/{message_id}")
