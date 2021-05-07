from typing import Dict

import sqlalchemy


def stringify(
    query: sqlalchemy.orm.orm.query.Query = None,
    engine: sqlalchemy.engine.Engine = None,
    dialect: sqlalchemy.engine.default.DefaultDialect = None,
    compile_kwargs: Dict = {},
) -> str:
    """
    @query: Query object to get plain SQL query from
    @engine: Database type to know the SQL dialect to convert into

    src: https://stackoverflow.com/a/23835766/219728
    """
    return (
        query.statement.compile(engine)
        if engine is not None
        else query.statement.compile(
            dialect=dialect, compile_kwargs={"literal_binds": True, **compile_kwargs}
        )
    )
