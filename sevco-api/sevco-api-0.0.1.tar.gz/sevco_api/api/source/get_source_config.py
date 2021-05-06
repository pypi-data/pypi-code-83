from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.configured_source import ConfiguredSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/integration/source/config".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_sevco_target_org is not UNSET:
        headers["x-sevco-target-org"] = x_sevco_target_org

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ConfiguredSource]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ConfiguredSource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ConfiguredSource]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Response[List[ConfiguredSource]]:
    kwargs = _get_kwargs(
        client=client,
        x_sevco_target_org=x_sevco_target_org,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Optional[List[ConfiguredSource]]:
    """description"""

    return sync_detailed(
        client=client,
        x_sevco_target_org=x_sevco_target_org,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Response[List[ConfiguredSource]]:
    kwargs = _get_kwargs(
        client=client,
        x_sevco_target_org=x_sevco_target_org,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Optional[List[ConfiguredSource]]:
    """description"""

    return (
        await asyncio_detailed(
            client=client,
            x_sevco_target_org=x_sevco_target_org,
        )
    ).parsed
