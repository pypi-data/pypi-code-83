import argparse
import json
from avroc.codegen import read, write
from avroc import dataclassgen


def main():
    parser = argparse.ArgumentParser(
        description="Generate Python module for an Avro schema."
    )
    parser.add_argument(
        "schema", type=str, help="an Avro schema document to generate from"
    )
    parser.add_argument(
        "--writer", action="store_true", help="generate a writer module"
    )
    parser.add_argument(
        "--reader", action="store_true", help="generate a reader module"
    )
    parser.add_argument(
        "--dataclass", action="store_true", help="generate a dataclass module"
    )

    args = parser.parse_args()

    dec = json.JSONDecoder()
    schema = dec.decode(args.schema)
    if args.writer:
        compiler = write.WriterCompiler(schema)
    elif args.reader:
        compiler = read.ReaderCompiler(schema)
    elif args.dataclass:
        compiler = dataclassgen.DataclassCompiler(schema)

    code = compiler.generate_source_code()
    print(code)


if __name__ == "__main__":
    main()
