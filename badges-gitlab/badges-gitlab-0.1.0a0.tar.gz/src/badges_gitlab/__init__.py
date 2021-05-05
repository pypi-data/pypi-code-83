"""Main Package File, parses CLI arguments and calls functions"""
import argparse
import os

from . import api_badges, badges_svg


def main():
    """Main Function for calling arg parser and executing functions"""
    parser = argparse.ArgumentParser(prog='badges-gitlab', description='Generate Gitlab Badges using JSON files.')
    parser.add_argument('-p', '--path', type=str, metavar='', default=os.path.join(os.getcwd(), "public", "badges"),
                        help='path where json and badges files will be generated/located (default: ''./public/badges/)')
    parser.add_argument('-t', '--token', type=str, metavar='', default='', help='specify the private-token in '
                                                                                'command line (default: ${'
                                                                                'PRIVATE_TOKEN})')
    args = parser.parse_args()
    # Assign a environment variable if token was not provided
    if args.token == '':
        if not os.environ.get('PRIVATE_TOKEN') is None:
            args.token = os.environ['PRIVATE_TOKEN']

    # Call the API Badges Creator
    api_badges.create_api_badges(args.path, args.token)
    print("Creating badges for files in directory", args.path)
    # Call the SVG Renderer
    badges_svg.print_badges(args.path)


if __name__ == "__main__":
    main()
