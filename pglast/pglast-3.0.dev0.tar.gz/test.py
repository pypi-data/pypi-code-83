from pglast.parser import parse_sql_protobuf
from pglast import pg_query_pb2
from pglast import Node

result = parse_sql_protobuf('ALTER DEFAULT PRIVILEGES FOR ROLE admin REVOKE execute ON FUNCTIONS FROM PUBLIC')
tree = pg_query_pb2.ParseResult.FromString(result)
root = Node(tree)
stmt = root.stmts[0]

import pdb; pdb.set_trace()

from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper

enums = []

for k in dir(pg_query_pb2):
    v = getattr(pg_query_pb2, k)
    if isinstance(v, EnumTypeWrapper):
        enums.append(v)

import pdb; pdb.set_trace()
