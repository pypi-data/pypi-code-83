#importing important library
from urllib import request
import json


def reply(text):
	try:
		req = text.replace(" ","%20")
		res = request.urlopen(f"https://alexa-bot-api-web-server.vercel.app/api/alexa?stimulus={req}")
		ans = res.read().decode("UTF-8")
		return json.loads(ans)["reply"]
	except:
		err = "Here is something wrong with server, Please try again later"
		return err


def replylang(text,lang):
	try:
		req = text.replace(" ","%20")
		lang_r = lang.replace(" ","")
		res = request.urlopen(f"https://alexa-bot-api-web-server.vercel.app/api/alexa?stimulus={req}?lang={lang_r}")
		ans = res.read().decode("UTF-8")
		return json.loads(ans)["reply"]
	except:
		err = "Here is something wrong with server, Please try again later"
		return err

