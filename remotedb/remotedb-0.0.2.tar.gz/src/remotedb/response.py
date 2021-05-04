import json

class Response:
  def __init__(self, type, response):
    self.type = type
    self.raw = json.loads(response)
 
  def __str__(self):
    if self.type == "get":
      return str(self.value)
    else:
      return str(self.status)

  @property
  def status(self):
    return self.raw.get("status")

  @property
  def message(self):
    return self.raw.get("message")

  @property
  def key(self):
    return self.raw.get("data").get("key")

  @property
  def value(self):
    return self.raw.get("data").get("value")

  @property
  def expire(self):
    if self.type == "set":
      return self.raw.get("data").get("expire") * 1000
    else:
      return None
