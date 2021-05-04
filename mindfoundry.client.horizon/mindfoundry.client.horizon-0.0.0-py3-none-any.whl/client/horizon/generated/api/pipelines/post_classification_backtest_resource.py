import json
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.classification_backtest_form import ClassificationBacktestForm
from ...models.classification_backtest_response import ClassificationBacktestResponse
from ...types import Response, is_file


def _get_kwargs(
    *,
    client: Client,
    id_: int,
    multipart_data: ClassificationBacktestForm,
) -> Dict[str, Any]:
    url = "{}/pipelines/{id}/expert/classification/backtest".format(client.base_url, id=id_)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    files = {}
    data = {}
    for key, value in multipart_data.to_dict().items():
        if is_file(value):
            files[key] = value
        elif isinstance(value, str):
            data[key] = value
        else:
            data[key] = json.dumps(value)

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": files,
        "data": data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ClassificationBacktestResponse]:
    if response.status_code == 200:
        response_200 = ClassificationBacktestResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ClassificationBacktestResponse]:
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
    multipart_data: ClassificationBacktestForm,
) -> Response[ClassificationBacktestResponse]:
    kwargs = _get_kwargs(
        client=client,
        id_=id_,
        multipart_data=multipart_data,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id_: int,
    multipart_data: ClassificationBacktestForm,
) -> Optional[ClassificationBacktestResponse]:
    """To make a single prediction for the whole batch,
    use `/expert/classification/predict` instead.

    """

    return sync_detailed(
        client=client,
        id_=id_,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id_: int,
    multipart_data: ClassificationBacktestForm,
) -> Response[ClassificationBacktestResponse]:
    kwargs = _get_kwargs(
        client=client,
        id_=id_,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id_: int,
    multipart_data: ClassificationBacktestForm,
) -> Optional[ClassificationBacktestResponse]:
    """To make a single prediction for the whole batch,
    use `/expert/classification/predict` instead.

    """

    return (
        await asyncio_detailed(
            client=client,
            id_=id_,
            multipart_data=multipart_data,
        )
    ).parsed
