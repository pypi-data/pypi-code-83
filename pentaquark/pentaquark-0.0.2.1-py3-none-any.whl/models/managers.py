"""Interface between objects and Cypher Query Builder
"""
from pentaquark.db import connection
from pentaquark.query_builders import MatchQueryBuilder, CreateQueryBuilder, ParameterStore
from pentaquark.exceptions import PentaQuarkObjectDoesNotExistError, PentaQuarkCardinalityError
from pentaquark.query_builders.call_query_builder import CallQueryBuilder
from pentaquark.query_builders.query_builder import RawQueryBuilder


class Manager:
    def __init__(self, model):
        self.model = model
        self._executed = False

    # RAW CYPHER
    def raw(self, query, parameters=None):
        """Raw Cypher query"""
        rqb = RawQueryBuilder(self.model, query, parameters)
        return rqb

    # MATCH
    def match(self, **kwargs):
        qb = MatchQueryBuilder(self.model)
        return qb.match(**kwargs)

    def match_full_text(self, index, text):
        cqb = CallQueryBuilder(self.model, procedure="db.index.fulltext.queryNodes", yield_names="node, score")
        return cqb.call(index, text)

    def all(self, limit=None):
        # TODO: add a batch mode to manage cases with MANY nodes and attributes
        return self.match().all(limit=limit)

    # EXISTENCE
    def exists(self, ins=None, **kwargs):
        if not ins:
            ins = self.model(**kwargs)
        return ins.exists()

    # CREATE
    def create(self, ins=None, **kwargs):
        """Create a node in DB using either the properties from ins or kwargs

        :param ins: Node instance
        :param kwargs: parameters
        :return: newly created instance
        """
        # if a similar object already exists raise Exception
        # (it's not up to pentaquark to decide what to do)
        if self.exists(ins, **kwargs):
            raise PentaQuarkCardinalityError(f"Node {ins} {kwargs} already exists")
        qb = CreateQueryBuilder(self.model)
        return qb.create(ins, **kwargs)

    def merge(self, ins) -> None:
        """Update a node instance

        :param ins:
        :return:
        """
        qb = CreateQueryBuilder(self.model)
        qb.merge(ins)

    # GET OR CREATE
    def get_or_create(self, **kwargs):
        try:
            obj = self.match(**kwargs).one()
            return obj
        except PentaQuarkObjectDoesNotExistError:
            pass
        return self.create(**kwargs)

    # DELETE
    def _delete(self, data, detach=False):
        alias = "a"
        ps = ParameterStore()
        data = self.model.kwargs_to_cypher(**data)
        n = self.model.to_cypher_match(
            alias=alias,
            param_store=ps,
            data=data,
        )
        cypher = f"MATCH {n.repr()} "
        if detach:
            cypher += "DETACH "
        cypher += f"DELETE {alias}"
        params = ps.params
        connection.cypher(cypher, params)

    def detach_delete(self, **kwargs):
        self._delete(kwargs, detach=True)

    def delete(self, **kwargs):
        self._delete(kwargs, detach=False)
