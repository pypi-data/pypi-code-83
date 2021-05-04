from pyug import get_random_username
from argparse import ArgumentParser


def main():
    ap = ArgumentParser()
    ap.add_argument("-c", "--count", help="Count of random names to print", default=1)
    a = ap.parse_args()

    for _ in range(a.count):
        print(get_random_username())


if __name__ == '__main__':
    main()
