# coding=utf-8

import time


def handle(args):
    if args.timestamp is not None:
        if args.utc:
            t = time.gmtime(args.timestamp)
        else:
            t = time.localtime(args.timestamp)
        print(time.strftime(args.format, t))
    elif args.time is not None:
        t = time.strptime(args.time, args.format)
        print(int(time.mktime(t)))
    else:
        if args.utc:
            t = time.gmtime()
        else:
            t = time.localtime()
        print(int(time.mktime(t)))
        print(time.strftime(args.format, t))
