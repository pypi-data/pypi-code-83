from pyug import get_random_name
from argparse import ArgumentParser


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument("-c", "--count", help="Count of random names to print", default=1)
    a = ap.parse_args()

    for _ in range(a.count):
        print(get_random_name())
