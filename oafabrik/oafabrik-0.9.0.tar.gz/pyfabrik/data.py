from abc import abstractmethod, ABC
from typing import List

import pandas as pd
import pydantic
from pydantic import typing

from pyfabrik.models import (
    FabrikRawReadResponse,
    FabrikException,
    FabrikRawWriteProfileResponse,
)


class DataFrameFacade(ABC):
    class WriteSummary(pydantic.BaseModel):
        path: str
        columns: List[str]

    @abstractmethod
    def read_data_frame(self, r: FabrikRawReadResponse) -> pd.DataFrame:
        pass

    @abstractmethod
    def write_data_frame(
        self, df: pd.DataFrame, profile: FabrikRawWriteProfileResponse
    ) -> WriteSummary:
        pass


class DefaultDataFrameFacade(DataFrameFacade):
    class ParquetContext(pydantic.BaseModel):
        landing_zone_kind: str
        path: str

    class CSVContext(pydantic.BaseModel):
        landing_zone_kind: str
        path: str

    def write_data_frame(
        self, df: pd.DataFrame, profile: FabrikRawWriteProfileResponse
    ) -> DataFrameFacade.WriteSummary:
        fmt = profile.context.get("format")

        if fmt == "parquet":
            return DefaultDataFrameFacade.write_parquet(df, profile.context.get("path"))

        if fmt == "csv":
            return DefaultDataFrameFacade.write_csv(df, profile.context.get("path"))

        raise FabrikException(f"Unsupported format `{fmt}`.")

    def read_data_frame(self, r: FabrikRawReadResponse) -> pd.DataFrame:
        if r.format.lower() == "parquet":
            return DefaultDataFrameFacade.read_parquet(r)

        if r.format.lower() == "csv":
            return DefaultDataFrameFacade.read_csv(r)

        raise FabrikException(f"Unsupported format `{r.format}`.")

    @staticmethod
    def write_parquet(df: pd.DataFrame, dest: str, **kwargs) -> DataFrameFacade.WriteSummary:
        path: str = dest + "results.parquet.snappy"

        df.to_parquet(path, **kwargs)
        return DataFrameFacade.WriteSummary(path=path, columns=[x for x in df.columns])

    @staticmethod
    def write_csv(df: pd.DataFrame, dest: str, sep: str = '\t', index: bool = False, header: bool = False, **kwargs) -> DataFrameFacade.WriteSummary:
        path: str = dest + "results.csv.gz"

        df.to_csv(path, index=index, sep=sep, header=header, **kwargs)
        return DataFrameFacade.WriteSummary(path=path, columns=[x for x in df.columns])

    @staticmethod
    def read_parquet(r: FabrikRawReadResponse) -> pd.DataFrame:
        ctx = DefaultDataFrameFacade.ParquetContext.parse_obj(r.context)
        return pd.read_parquet(ctx.path)

    @staticmethod
    def read_csv(r: FabrikRawReadResponse) -> pd.DataFrame:
        ctx = DefaultDataFrameFacade.CSVContext.parse_obj(r.context)
        return pd.read_csv(ctx.path)
