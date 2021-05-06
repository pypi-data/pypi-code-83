import os
import sys
from copy import deepcopy

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tisdb.types import StoreType
from tisdb.client import TsdbClient
from tisdb.config import TsdbConfig

import logging
import os

logger = logging.getLogger("tisdb")


def make_db_params(key):
    params = {}
    env_vars = [
        (part, "TISDB_%s_%s" % (key, part.upper()))
        for part in ("host", "port", "user", "password")
    ]
    for param, env_var in env_vars:
        value = os.environ.get(env_var)
        if value:
            params[param] = int(value) if param == "port" else value
    return params


PORM_PARAMS = make_db_params("PORM")


def db_loader(engine: str, **params):
    db_params = deepcopy(PORM_PARAMS)
    db_params.update(params)
    return TsdbClient(
        store_type=StoreType[engine.upper()], conn_conf=TsdbConfig(**db_params)
    )


class QueryLogHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        self.queries = []
        logging.Handler.__init__(self, *args, **kwargs)

    def emit(self, record):
        self.queries.append(record)
