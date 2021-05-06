# coding=utf-8

import base64
import urllib.parse


def handle(args):
    if args.mode == 'base64':
        if args.decode is not None:
            print(base64.decodebytes(args.decode.encode()).decode())
        elif args.encode is not None:
            print(base64.encodebytes(args.encode.encode()).decode())
    elif args.mode == 'url':
        if args.decode is not None:
            print(urllib.parse.unquote(args.decode))
        elif args.encode is not None:
            print(urllib.parse.quote(args.encode))
