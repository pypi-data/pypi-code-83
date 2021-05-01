from __future__ import annotations

import typing

import sqlalchemy as sa

from lime_uow import resource
from lime_uow.sqlalchemy_resources import sqlalchemy_transaction

__all__ = ("SqlAlchemyEngine",)


class SqlAlchemyEngine(resource.Resource[sa.engine.Engine]):
    def __init__(self, /, db_uri: str):
        self._db_uri = db_uri
        self._engine: typing.Optional[sa.engine.Engine] = None

    @staticmethod
    def key() -> str:
        return SqlAlchemyEngine.__name__

    def transaction(self) -> sqlalchemy_transaction.SqlAlchemyTransaction:
        return sqlalchemy_transaction.SqlAlchemyTransaction(self._engine)

    def open(self, **kwargs: typing.Dict[str, typing.Any]) -> sa.engine.Engine:
        if self._engine is None:
            self._engine = sa.create_engine(self._db_uri)
        return self._engine
