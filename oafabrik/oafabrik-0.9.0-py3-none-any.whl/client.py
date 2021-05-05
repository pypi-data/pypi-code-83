import concurrent.futures
import typing
import uuid
from concurrent.futures._base import Future

import requests

from .data import DataFrameFacade
from .models import (
    FabrikReadRequest,
    FabrikReadResponse,
    FabrikWriteRequest,
    FabrikException,
    FabrikRawReadResponse,
    FabrikWriteResponse,
    FabrikRawWriteProfileResponse,
    FabrikRawWriteRequest,
)


def _perform_read(
        endpoint: str,
        req: FabrikReadRequest,
        session: requests.Session,
        df_facade: DataFrameFacade,
) -> FabrikReadResponse:
    try:
        res = session.post(endpoint + "/read", json=req.dict())
        if not res.ok:
            raise FabrikException("Received invalid response code.", res.text)

        fabrik_read_res: FabrikRawReadResponse = FabrikRawReadResponse.parse_obj(
            res.json()
        )

        return FabrikReadResponse(df=df_facade.read_data_frame(fabrik_read_res), context=fabrik_read_res.context)

    except Exception as ex:
        raise FabrikException("Failed to execute read request.", ex)


class FabrikClient(object):
    def __init__(self, endpoint: str, token: str, df_facade: DataFrameFacade):
        self.endpoint = endpoint
        self.token = token
        self.df_facade = df_facade

        self.session = requests.session()
        self.session.headers.update({"authorization": "Bearer " + self.token})

    def read_all(
            self, r: typing.List[FabrikReadRequest]
    ) -> typing.List[FabrikReadResponse]:
        futures: typing.List[Future] = []
        results: typing.List[FabrikReadResponse] = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for entry in r:
                futures.append(
                    executor.submit(
                        _perform_read,
                        self.endpoint,
                        entry,
                        self.session,
                        self.df_facade,
                    )
                )

            for f in futures:
                results.append(f.result())

        return results

    def read(self, r: FabrikReadRequest) -> FabrikReadResponse:
        return _perform_read(self.endpoint, r, self.session, self.df_facade)

    def write(self, r: FabrikWriteRequest) -> FabrikWriteResponse:

        res_profile = self.session.post(
            self.endpoint + "/write/profile", json={"reference": str(uuid.uuid4()), "format": r.format}
        )

        if not res_profile.ok:
            raise FabrikException("Failed to retrieve write profile.", res_profile.text)

        profile = FabrikRawWriteProfileResponse.parse_obj(res_profile.json())

        summary: DataFrameFacade.WriteSummary = self.df_facade.write_data_frame(r.df, profile)

        raw_write_req = FabrikRawWriteRequest(
            path=r.path,
            context={"path": summary.path, "columns": ",".join(summary.columns)},
            warehouse=r.warehouse,
            format=r.format,
        )

        res_write = self.session.post(
            self.endpoint + "/write", json=raw_write_req.dict()
        )

        if not res_write.ok:
            raise FabrikException("Failed to perform write.", res_write.text)

        return FabrikWriteResponse(reference="1234")
