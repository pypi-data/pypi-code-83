import requests

"""
More information at https://pypi.org/project/pytokapi
"""

__version__ = "1.0.0"

class TikTok:

  def __init__(self):
    """ TikTok API Wrapper """
    pass

  def getInfo(self, url : str):

    req = requests.get(f"https://www.tiktok.com/oembed?url={url}").json()

    if ("status_msg" in req):
      raise SystemExit("Invalid URL | TikTok API Response Error")
    else:
      return {
        "version": req["version"],
        # Basic Video Information
        "title": req["title"],
        "author": {
          "url": req["author_url"],
          "name": req["author_name"],
        },
        # These would be the average key of the object in a response
        "provider": {
          "url": "https://www.tiktok.com",
          "name": "TikTok",
        },
        # Video Information
        "video": {
          # Usage for websites
          "html": {
            "embed": req["html"],
            "width": req["width"],
            "height": req["height"],
          },
          # Video Size & URL
          "height": req["thumbnail_height"],
          "url": req["thumbnail_url"],
          "width": req["thumbnail_width"],
        }
      }