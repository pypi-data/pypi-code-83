from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.algo_execution_test_case import AlgoExecutionTestCase
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    id_: int,
) -> Dict[str, Any]:
    url = "{}/algos/{id}/test/cases".format(client.base_url, id=id_)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AlgoExecutionTestCase]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AlgoExecutionTestCase.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AlgoExecutionTestCase]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id_: int,
) -> Response[List[AlgoExecutionTestCase]]:
    kwargs = _get_kwargs(
        client=client,
        id_=id_,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id_: int,
) -> Optional[List[AlgoExecutionTestCase]]:
    """Use these test cases with `/api/algos/{id}/test` to check if an algo will
    run a basic case scenario.
    """

    return sync_detailed(
        client=client,
        id_=id_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id_: int,
) -> Response[List[AlgoExecutionTestCase]]:
    kwargs = _get_kwargs(
        client=client,
        id_=id_,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id_: int,
) -> Optional[List[AlgoExecutionTestCase]]:
    """Use these test cases with `/api/algos/{id}/test` to check if an algo will
    run a basic case scenario.
    """

    return (
        await asyncio_detailed(
            client=client,
            id_=id_,
        )
    ).parsed
