from pyppeteer import launch

class engine():
 def __init__(self):
     pass
     
 async def start(self):
     self.browser = await launch({'headless': True})
     self.page = await self.browser.newPage()
 
 async def goto(self,url):
  await self.page.goto(url)
  return await self.page.content()

 async def close(self):
  await self.browser.close()