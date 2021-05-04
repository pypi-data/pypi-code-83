# -*- coding: utf-8 -*-

from .sql import geoviews as views
from .. import settings

class BreakDatabaseIo(Exception):
    """ """

class Sqler(object):
    """docstring for Sqler."""

    def __init__(self):
        super(Sqler, self).__init__()
        from ..models import db
        self.db = db

    def __call__(self, query):
        """"""
        return self.db.executesql(query);

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if traceback:
            self.db.rollback()
            if isinstance(exc_value, BreakDatabaseIo):
                return True
        else:
            self.db.commit()

    def break_io(self, message=None):
        raise BreakDatabaseIo(message)

    def init_view(self, name, query, materialized=False):
        MATERIALIZED = ' MATERIALIZED' if materialized else ''
        _query = "DROP{MATERIALIZED} VIEW IF EXISTS {name} CASCADE;\n" if materialized else "DROP VIEW IF EXISTS {name} CASCADE;n"
        _query += "CREATE{MATERIALIZED} VIEW {name} AS {query}"

        return self(_query.format(**vars()))

def setup():

    with Sqler() as sqler:

        # execute("""
        # CREATE SEQUENCE IF NOT EXISTS mysegseq;
        # ALTER SEQUENCE mysegseq RESTART WITH 1;
        # """)

        sqler("""
        CREATE SEQUENCE IF NOT EXISTS snodesseq;
        ALTER SEQUENCE snodesseq RESTART WITH 1;
        CREATE SEQUENCE IF NOT EXISTS spolyseq;
        ALTER SEQUENCE spolyseq RESTART WITH 1;
        CREATE SEQUENCE IF NOT EXISTS rpathseq;
        ALTER SEQUENCE rpathseq RESTART WITH 1;
        """)

        sqler.init_view('addresses', views.ADDRESSES, materialized=("addresses" in settings.MATERIALIZED_VIEWS))

        sqler.init_view('housenumbers', views.HOUSENUMBERS, materialized=("housenumbers" in settings.MATERIALIZED_VIEWS))

        sqler.init_view('points', views.POINTS, materialized=("points" in settings.MATERIALIZED_VIEWS))

        sqler.init_view('ways', views.WAYS, materialized=("ways" in settings.MATERIALIZED_VIEWS))

        sqler.init_view('graph', views.GRAPH, materialized=("graph" in settings.MATERIALIZED_VIEWS))

        sqler.init_view('segment_points', views.SPLITTEDSEGMENTSNODES, materialized=True)

        sqler.init_view('spolys', views.SIMPLEPOLYGONS, materialized=True)

        sqler.init_view('rpath', views.REBUILDEDPOLYGONPATHS, materialized=True)

        sqler.init_view('rpolys', views.REBUILDEDPOLYGONS(rpath='rpath'),  materialized=True)

        sqler.init_view('polys', views.POLYS(spolys='spolys'), materialized=True)

    return

# init_view('segment_points', Q4SPLITTEDSEGMENTSNODES, materialized=True)
#
# init_view('ways', Q4WAYS, materialized=True)
#
# init_view('graph', Q4GRAPH)
#
# execute("""
# CREATE SEQUENCE IF NOT EXISTS mypolyseq;
# SELECT setval('mypolyseq', (SELECT id+1 FROM ways ORDER BY id DESC LIMIT 1));
# """)
#
# init_view('spolys', Q4SIMPLEPOLYGONS,  materialized=True)
#
# init_view('rpath', Q4REBUILDEDPOLYGONPATHS, materialized=True)
#
# init_view('rpolys', Q4REBUILDEDPOLYGONS,  materialized=True)
#
# init_view('polys', '(SELECT * FROM spolys) UNION (SELECT * FROM rpolys);')
