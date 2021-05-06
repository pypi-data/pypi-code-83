# coding=utf-8

import hashlib
import pyperclip


def handle(args):
    if args.string is not None:
        data = args.string
    elif args.clipboard:
        data = pyperclip.paste()
    else:
        data = args.file.read()
    if isinstance(data, str):
        data = data.encode()
    print(hashlib.new(args.alg, data).hexdigest())
