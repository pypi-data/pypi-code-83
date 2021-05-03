"""A collection of spark utils
"""

import socket


def adjust_schema(df):
    """infer schema to fix parquet to Spark's parquet"""
    for typ in df.schema:
        if typ.dataType.typeName() == 'decimal' and typ.dataType.precision < 19:
            typ.dataType.precision = 38
    return df


def local_ip():
    """find out local IP, when running spark driver locally for remote cluster"""
    ip = ((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(
        ("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])

    return ip
