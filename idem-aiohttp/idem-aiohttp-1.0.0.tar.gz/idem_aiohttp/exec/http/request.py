import requests


async def delete(hub, ctx, url: str, **kwargs):
    response: requests.Response = await hub.tool.http.session.delete(
        ctx, url=url, **kwargs
    )
    return response.text


async def get(hub, ctx, url: str, **kwargs):
    response: requests.Response = await hub.tool.http.session.get(
        ctx, url=url, **kwargs
    )
    return response.text


async def patch(hub, ctx, url: str, **kwargs):
    response: requests.Response = await hub.tool.http.session.patch(
        ctx, url=url, **kwargs
    )
    return response.text


async def post(hub, ctx, url: str, **kwargs):
    response: requests.Response = await hub.tool.http.session.post(
        ctx, url=url, **kwargs
    )
    return response.text


async def put(hub, ctx, url: str, **kwargs):
    response: requests.Response = await hub.tool.http.session.put(
        ctx, url=url, **kwargs
    )
    return response.text
