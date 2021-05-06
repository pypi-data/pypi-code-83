"""
Main file
"""

import sys
from testeasydubins import dubin_path


def main():
    """
    Library initiation.
    :return:
    """
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [o for o in sys.argv[1:] if o.startswith("-")]

    if "-h" in opts or "--help" in opts:
        print(dubin_path.__doc__)
        return

    print("'testeasydubins' library imported.")


if __name__ == '__main__':
    main()
