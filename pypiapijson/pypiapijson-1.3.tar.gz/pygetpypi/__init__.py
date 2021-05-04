
import requests,aiohttp
def get(name):
      r = requests.get(f"https://pypi.org/pypi/{name}/json")
      if r.json() is None:
             print("Error occured!\nI can\'t get the package info maybe check your typo or check your connection if you check it was all right, pypi api may gone maintenance.")
      else:
             js = r.json()
             return js
def getbyv(name,ver):
      r = requests.get(f"https://pypi.org/pypi/{name}/{ver}/json")
      js = r.json()
      if js is None:
             print("Error occured!\nI can\'t get the package info with provided version maybe check your typo or check your connection if you check it was all right, pypi api may gone maintenance.")
            
             
      else:
             return js
async def status():
             h = {"Accept" : "application/json","Content-type":"application/json"}
             async with aiohttp.ClientSession(headers=h) as s:
                   async with s.get("https://pypi.org/stats") as data:
                         if data.status is 200 or "200":
                               return await data.json()
                         else:
                               
                               print("Error!")
