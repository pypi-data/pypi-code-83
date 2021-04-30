import functools
import itertools
import os
import time
from typing import Generator, List, Sequence, Union

import pandas  # type: ignore
import pyarrow  # type: ignore
import pyarrow.parquet as pq  # type: ignore
from cached_property import cached_property  # type: ignore

from tktl.core.config import settings
from tktl.core.exceptions import WrongPathError


def concatenate_urls(fst_part, snd_part):
    fst_part = fst_part if not fst_part.endswith("/") else fst_part[:-1]
    template = "{}{}" if snd_part.startswith("/") else "{}/{}"
    concatenated = template.format(fst_part, snd_part)
    return concatenated


class PathParser(object):
    LOCAL_DIR = 0
    LOCAL_FILE = 1
    GIT_URL = 2
    S3_URL = 3

    @classmethod
    def parse_path(cls, path):
        if cls.is_local_dir(path):
            return cls.LOCAL_DIR

        if cls.is_local_zip_file(path):
            return cls.LOCAL_FILE

        if cls.is_git_url(path):
            return cls.GIT_URL

        if cls.is_s3_url(path):
            return cls.S3_URL

        raise WrongPathError("Given path is neither local path, nor valid URL")

    @staticmethod
    def is_local_dir(path):
        return os.path.exists(path) and os.path.isdir(path)

    @staticmethod
    def is_local_zip_file(path):
        return os.path.exists(path) and os.path.isfile(path) and path.endswith(".zip")

    @staticmethod
    def is_git_url(path):
        return (
            not os.path.exists(path)
            and path.endswith(".git")
            or path.lower().startswith("git:")
        )

    @staticmethod
    def is_s3_url(path):
        return not os.path.exists(path) and path.lower().startswith("s3:")


def lru_cache(timeout: int, maxsize: int = 128, typed: bool = False):
    def wrapper_cache(func):
        func = functools.lru_cache(maxsize=maxsize, typed=typed)(func)
        func.delta = timeout * 10 ** 9
        func.expiration = time.monotonic_ns() + func.delta

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            if time.monotonic_ns() >= func.expiration:
                func.cache_clear()
                func.expiration = time.monotonic_ns() + func.delta
            return func(*args, **kwargs)

        wrapped_func.cache_info = func.cache_info
        wrapped_func.cache_clear = func.cache_clear
        return wrapped_func

    return wrapper_cache


def flatten(x: Sequence) -> List:
    return list(itertools.chain.from_iterable(x))


class DelayedLoadingFrame(object):
    def __init__(
        self,
        path: str,
        label_name: str,
        is_label: bool = False,
        profile_columns: List[str] = None,
        load_for_profiling: bool = False,
    ):
        self.path = path
        self.label_name = label_name
        self.is_label = is_label
        self.load_for_profiling = load_for_profiling
        self._reset_index = False
        self._profile_columns = profile_columns

    @property
    def profile_columns(self):
        return (
            self._profile_columns if self._profile_columns is not None else self.columns
        )

    @property
    def reset_index(self):
        return self._reset_index

    @reset_index.setter
    def reset_index(self, val):
        self._reset_index = val

    @cached_property
    def columns(self):
        return [
            c
            for c in pq.read_table(self.path, memory_map=True).column_names
            if not c.startswith("__index_level_") and c != self.label_name
        ]

    @cached_property
    def _parquet_file(self):
        return pq.ParquetFile(self.path, memory_map=True)

    @cached_property
    def schema(self):
        return self.first_batch.schema

    @cached_property
    def first_batch(self):
        return next(self.to_batches())

    @cached_property
    def batch_size(self) -> int:
        return settings.PARQUET_BATCH_DEFAULT_ROWS_READ // len(self.columns)

    def to_pandas_batches(
        self,
    ) -> Generator[Union[pandas.DataFrame, pandas.Series], None, None]:
        if self.load_for_profiling:
            return (self._profiling_frame(f.to_pandas()) for f in self.to_batches())
        if self.is_label:
            return (self._labels_frame(f.to_pandas()) for f in self.to_batches())
        return (x.to_pandas() for x in self.to_batches())

    def to_batches(self) -> Generator[pyarrow.RecordBatch, None, None]:
        if self.is_label:
            return self._parquet_file.iter_batches(
                batch_size=self.batch_size, columns=[self.label_name],
            )
        if self.load_for_profiling:
            return (
                f
                for f in self._parquet_file.iter_batches(
                    batch_size=self.batch_size, columns=self.columns
                )
            )
        return self._parquet_file.iter_batches(batch_size=self.batch_size)

    def load(self, first_batch: bool = False) -> Union[pandas.Series, pandas.DataFrame]:
        if first_batch:
            frame = self._load_first_batch()
        else:
            frame = self._load_full_frame()

        if self.is_label:
            return self._labels_frame(frame=frame)
        if self.load_for_profiling:
            return self._profiling_frame(frame=frame)
        return self._frame(frame=frame)

    def _load_first_batch(self) -> pandas.DataFrame:
        return self.first_batch.to_pandas()

    def _profiling_frame(self, frame: pandas.DataFrame) -> pandas.DataFrame:
        frame.columns = [str(c) for c in frame.columns]
        if self.reset_index:
            frame = frame.reset_index(drop=True)
        return frame

    def _labels_frame(self, frame: pandas.DataFrame) -> pandas.Series:
        return frame[self.label_name]

    def _frame(self, frame: pandas.DataFrame) -> pandas.DataFrame:
        return frame.drop(columns=[self.label_name])

    def _load_full_frame(self) -> pandas.DataFrame:
        return pq.read_table(
            self.path, columns=self.columns, memory_map=True
        ).to_pandas()


def check_and_get_value(value, first_batch=False):
    if isinstance(value, DelayedLoadingFrame):
        if value.load_for_profiling:
            return value.load(first_batch=first_batch)[value.profile_columns]
        return value.load(first_batch=first_batch)
    else:
        return value
