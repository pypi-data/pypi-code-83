import sqlalchemy


def stringify(
    query: sqlalchemy.orm.orm.query.Query = None,
    engine: sqlalchemy.engine.Engine = None,
    dialect: sqlalchemy.engine.default.DefaultDialect = None,
) -> str:
    """
    @query: Query object to get plain SQL query from
    @engine: Database type to know the SQL dialect to convert into
    """
    return (
        query.statement.compile(engine)
        if engine is not None
        else query.statement.compile(dialect=dialect)
    )
