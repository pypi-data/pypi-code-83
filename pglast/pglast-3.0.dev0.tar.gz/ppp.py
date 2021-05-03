from pathlib import Path
from pglast import split


pg_regressions_dir = Path() / 'libpg_query' / 'test' / 'sql' / 'postgres_regress'


def split_statements(src):
    source = src.read_text()
    try:
        slices = split(source, with_parser=False, only_slices=True)
    except Exception as e:
        return
    for slice in slices:
        statement = source[slice]
        lineno = source[:slice.start].count('\n') + 1
        yield lineno, statement


x = list((src, lineno, statement)
         for src in sorted(pg_regressions_dir.glob('*.sql'))
         for (lineno, statement) in split_statements(src))

import pdb; pdb.set_trace()
