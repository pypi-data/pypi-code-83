from . import connection


def command_index(args):
    src_es = connection.make(args.src_url)
    dst_es = connection.make(args.dst_url)

    src_count = src_es.cat.count(index=args.src_index, format='json')['count']
    dst_count = dst_es.cat.count(index=args.dst_index, format='json')['count']

    if src_count != dst_count:
        print('index document count mismatch:')
        print(f'{args.src_index}@{args.src_url} has {src_count} docs.')
        print(f'{args.dst_index}@{args.dst_url} has {dst_count} docs.')
    elif args.verbose:
        print(f'{args.src_index}@{args.src_url} matches {args.dst_index}@{args.dst_url} document count ({src_count} docs).')


def command_doc(args):
    pass


def add_index(sub_parser):
    index_parser = sub_parser.add_parser(
        "index",
        help="verifies high-level index integrity.",
    )
    index_parser.set_defaults(command=command_index)
    index_parser.add_argument(
        "src_index", help="source ES cluster index name.",
    )
    index_parser.add_argument(
        "dst_index", help="destination ES cluster index name.",
    )


def add_doc(sub_parser):
    doc_parser = sub_parser.add_parser(
        "doc",
        help="verifies document-level integrity.",
    )
    doc_parser.set_defaults(command=command_doc)
    doc_parser.add_argument(
        "src_index_pattern", help="source ES cluster index pattern to pick docs from.",
    )
    doc_parser.add_argument(
        "dst_index_pattern", help="destination ES cluster index pattern to pick docs from.",
    )
