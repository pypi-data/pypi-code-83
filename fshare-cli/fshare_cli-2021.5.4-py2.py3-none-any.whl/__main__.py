import sys
from fshare_cli import *

import argparse

def main():
    parser = argparse.ArgumentParser(description='Fshare command-line interface', usage='fshare [-v] [-q] (configure | download | upload | api) [options] [-h | --help]')
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true', default=False, help='Activate quiet mode')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Print various debugging information')

    if sys.version_info >= (3, 7):
        subparsers = parser.add_subparsers(title='command', dest='cmd', required=False)
    else:
        subparsers = parser.add_subparsers(title='command', dest='cmd')

    parser_configure = subparsers.add_parser('configure', usage='fshare configure')

    parser_download = subparsers.add_parser('download', usage='fshare download url [options] [--help]')
    parser_download.add_argument('url', help='the URL you want to download')
    parser_download.add_argument('-p', '--password', help='the password for this URL')
    parser_download.add_argument('-d', '--destination', default='.', help='the directory where you want to download this URL')

    parser_upload = subparsers.add_parser('upload')
    parser_upload.add_argument('file', help='the file you want to upload')
    parser_upload.add_argument('-p', '--password', help='the password for this file')
    parser_upload.add_argument('-d', '--destination', default='/', help='the directory where you want to upload this file')

    parser_api = subparsers.add_parser('api')
    parser_api.add_argument('path', help='the API path you want to trigger')
    parser_api.add_argument('--args', help='the arguments for this API')

    args = parser.parse_args()

    fshare_cli = FshareCLI(args)

if __name__ == '__main__':
    main()
