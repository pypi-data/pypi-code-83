from response import Response
import requests

class Client:
  def __init__(self, client:str=None, authorization:str=None, default_expire:int=None):
    self.client = client
    self.authorization = authorization
    self.default_expire = default_expire
  
  def __setitem__(self, key, value):
    if isinstance(value, tuple):
      return self.set(key, value[0], value[1])
    return self.set(key, value)

  def __getitem__(self, key):
    return self.get(key)

  def __delitem__(self, key):
    return self.delete(key)

  def set(self, key:str=None, value:str=None, expire:int=None):
    expire = expire or self.default_expire
    try:
      result = requests.post("https://db.hostinghq.xyz/v1/post", headers = {"Client-ID": self.client, "Authorization": self.authorization}, data={"key": key, "value": value, "expire": expire if expire == None else expire*1000}).text
      return Response("set", result)
    except Exception as e:
      return e
  
  def get(self, key:str=None):
    try:
      result = requests.post("https://db.hostinghq.xyz/v1/query", headers = {"Client-ID": self.client, "Authorization": self.authorization}, data={"key": key}).text
      return Response("get", result)
    except Exception as e:
      return e

  def delete(self, key:str=None):
    try:
      result = requests.post("https://db.hostinghq.xyz/v1/delete", headers = {"Client-ID": self.client, "Authorization": self.authorization}, data={"key": key}).text
      return Response("delete", result)
    except Exception as e:
      return e
