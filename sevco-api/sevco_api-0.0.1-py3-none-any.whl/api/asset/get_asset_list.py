from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.asset_request import AssetRequest
from ...models.device_results import DeviceResults
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: AssetRequest,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/asset/device".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_sevco_target_org is not UNSET:
        headers["x-sevco-target-org"] = x_sevco_target_org

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[DeviceResults]:
    if response.status_code == 200:
        response_200 = DeviceResults.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DeviceResults]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AssetRequest,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Response[DeviceResults]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_sevco_target_org=x_sevco_target_org,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: AssetRequest,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Optional[DeviceResults]:
    """description"""

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_sevco_target_org=x_sevco_target_org,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AssetRequest,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Response[DeviceResults]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_sevco_target_org=x_sevco_target_org,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: AssetRequest,
    x_sevco_target_org: Union[Unset, str] = UNSET,
) -> Optional[DeviceResults]:
    """description"""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_sevco_target_org=x_sevco_target_org,
        )
    ).parsed
