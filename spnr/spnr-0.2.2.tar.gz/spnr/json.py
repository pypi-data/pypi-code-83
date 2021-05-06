# coding=utf-8

import json
import pyperclip


def handle(args):
    if args.string is not None:
        j = args.string
    elif args.clipboard:
        j = pyperclip.paste()
    else:
        j = args.file.read()
    j = json.loads(j)
    print(json.dumps(j, indent=args.indent, ensure_ascii=False))
