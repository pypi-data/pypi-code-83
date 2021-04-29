import requests
from dict_tools.data import NamespaceDict
from typing import Dict


async def delete(hub, ctx, url: str, headers: Dict[str, str] = None, **kwargs):
    if not headers:
        headers = {}

    headers["content-type"] = "application/json"
    response: requests.Response = await hub.tool.http.session.delete(
        ctx, url=url, headers=headers, **kwargs
    )
    return response.json()


async def get(hub, ctx, url: str, headers: Dict[str, str] = None, **kwargs):
    if not headers:
        headers = {}
    headers["content-type"] = "application/json"
    response: requests.Response = await hub.tool.http.session.get(
        ctx, url=url, headers=headers, **kwargs
    )
    return NamespaceDict(response.json())


async def head(hub, ctx, url: str, headers: Dict[str, str] = None, **kwargs):
    if not headers:
        headers = {}
    headers = kwargs.pop("headers", {})
    headers["content-type"] = "application/json"
    response: requests.Response = await hub.tool.http.session.head(
        ctx, url=url, headers=headers, **kwargs
    )
    return NamespaceDict(response.headers)


async def patch(hub, ctx, url: str, headers: Dict[str, str] = None, **kwargs):
    if not headers:
        headers = {}
    headers = kwargs.pop("headers", {})
    headers["content-type"] = "application/json"
    response: requests.Response = await hub.tool.http.session.patch(
        ctx, url=url, headers=headers, **kwargs
    )
    return NamespaceDict(response.json())


async def post(hub, ctx, url: str, headers: Dict[str, str] = None, **kwargs):
    if not headers:
        headers = {}
    headers = kwargs.pop("headers", {})
    headers["content-type"] = "application/json"
    response: requests.Response = await hub.tool.http.session.post(
        ctx, url=url, headers=headers, **kwargs
    )
    return NamespaceDict(response.json())


async def put(hub, ctx, url: str, headers: Dict[str, str] = None, **kwargs):
    if not headers:
        headers = {}
    headers = kwargs.pop("headers", {})
    headers["content-type"] = "application/json"
    response: requests.Response = await hub.tool.http.session.put(
        ctx, url=url, headers=headers, **kwargs
    )
    return NamespaceDict(response.json())
