
import requests,asyncio
def get(name):
      r = requests.get(f"https://pypi.org/pypi/{name}/json")
      js = r.json()
      return js