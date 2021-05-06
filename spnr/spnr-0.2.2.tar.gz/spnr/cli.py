# coding=utf-8

import argparse
import sys

import spnr
from spnr import code
from spnr import hash
from spnr import json
from spnr import qr
from spnr import table
from spnr import time


def init_qr_parser(parser):
    subparsers = parser.add_subparsers(required=True)

    gen_parser = subparsers.add_parser('generate', aliases=['gen', 'g'])
    gen_parser.set_defaults(func=qr.generate)
    gen_group = gen_parser.add_mutually_exclusive_group()
    gen_group.add_argument('-s', '--string', help='content')
    gen_group.add_argument('-c', '--clipboard', help='read content from clipboard', action='store_true')
    gen_group.add_argument('-f', '--file',
                           help='read content from the file, default stdin',
                           default=sys.stdin,
                           type=argparse.FileType('r'),
                           nargs='?')
    gen_out_group = gen_parser.add_mutually_exclusive_group()
    gen_out_group.add_argument('-S', '--screen', help='show the qrcode on the screen', action='store_true')
    gen_out_group.add_argument('-o', '--output-file',
                               help='output qrcode to a file, default stdout',
                               default=sys.stdout,
                               type=argparse.FileType('w'),
                               nargs='?')

    scan_parser = subparsers.add_parser('scan', aliases=['s'])
    scan_parser.set_defaults(func=qr.scan)
    scan_group = scan_parser.add_mutually_exclusive_group()
    scan_group.add_argument('-c', '--camera', help='scan a qrcode from the camera', action='store_true')
    scan_group.add_argument('-s', '--screen', help='scan a qrcode from the screen', action='store_true', default=True)
    scan_group.add_argument('-f', '--file',
                            help='scan a qrcode from the picture file',
                            type=argparse.FileType('rb'))
    scan_parser.add_argument('-C', '--clipboard', help='copy the result to the clipboard', action='store_true')


def init_table_parser(parser):
    parser.set_defaults(func=table.handle)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m', '--matrix', help='a matrix literal')
    group.add_argument('-f', '--file',
                       help='read a matrix literal or csv from the file, default stdin',
                       default=sys.stdin,
                       type=argparse.FileType('r'),
                       nargs='?')
    parser.add_argument('--row-span', choices=['head', 'none', 'all'], help='row span mode', default='head')


def init_time_parser(parser):
    parser.set_defaults(func=time.handle)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--timestamp', type=float, help='timestamp', )
    group.add_argument('-T', '--time', help='time in string')
    parser.add_argument('-f', '--format', help='time format', default='%Y-%m-%d %H:%M:%S')
    parser.add_argument('-u', '--utc', help='use utc time', action='store_true')


def init_json_parser(parser):
    parser.set_defaults(func=json.handle)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--string', help='a json string')
    group.add_argument('-c', '--clipboard', help='read the json from the clipboard', action='store_true')
    group.add_argument('-f', '--file',
                       help='read the json from a file, default stdin',
                       default=sys.stdin,
                       type=argparse.FileType('r'),
                       nargs='?')
    parser.add_argument('-i', '--indent', type=int, help='indent', default=2)


def init_code_parser(parser):
    parser.set_defaults(func=code.handle)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encode', help='encode a string')
    group.add_argument('-d', '--decode', help='decode a string')
    parser.add_argument('-m', '--mode', choices=['base64', 'url'], help='code mode', required=True)


def init_hash_parser(parser):
    parser.set_defaults(func=hash.handle)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--string', help='hash a string')
    group.add_argument('-c', '--clipboard', help='read the string from the clipboard', action='store_true')
    group.add_argument('-f', '--file',
                       help='hash a file, default stdin',
                       default=sys.stdin,
                       type=argparse.FileType('rb'),
                       nargs='?')
    parser.add_argument('-a', '--alg', help='hash algorithm', required=True)


def main():
    parser = argparse.ArgumentParser(description='A toolset.', add_help=True)
    parser.add_argument('-v', '--version', action='version', version=spnr.version)

    subparsers = parser.add_subparsers(required=True)

    qr_parser = subparsers.add_parser('qr')
    init_qr_parser(qr_parser)
    table_parser = subparsers.add_parser('table')
    init_table_parser(table_parser)
    time_parser = subparsers.add_parser('time')
    init_time_parser(time_parser)
    json_parser = subparsers.add_parser('json')
    init_json_parser(json_parser)
    code_parser = subparsers.add_parser('code')
    init_code_parser(code_parser)
    hash_parser = subparsers.add_parser('hash')
    init_hash_parser(hash_parser)

    args = parser.parse_args()
    args.func(args)
