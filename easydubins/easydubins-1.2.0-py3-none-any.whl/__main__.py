"""
Main file
"""

import sys
from easydubins import dubin_path


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

    print("'easydubins' library imported.")


if __name__ == '__main__':
    main()
