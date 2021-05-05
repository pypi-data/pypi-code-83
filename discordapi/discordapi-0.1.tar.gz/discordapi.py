import requests
import os

def send_message(token, channelid, message):
	os.system("title Created with Nekit's Discord API v9 Libary.")

	header = {
		"authorization": token
	}

	payload = {
		"content": message
	}

	r = requests.post("https://discord.com/api/v9/channels/"+channelid+"/messages", data=payload, headers=header)

def delete_channel(token, channelid):
	os.system("title Created with Nekit's Discord API v9 Libary.")

	header = {
		"authorization": token
	}

	payload = {
		"id": channelid
	}

	r = requests.delete("https://discord.com/api/v9/channels/"+channelid, headers=header, data=payload)