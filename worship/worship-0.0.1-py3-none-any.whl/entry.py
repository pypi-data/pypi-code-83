import sys

from soxutils.frame import Frame
from dofast.simple_parser import SimpleParser

msg = """Python implemented SOX 🛠️ 
-i, --info ::: Get audio file information.
"""


def run():
    sp = SimpleParser()
    sp.add_argument('-i', '--info')
    sp.parse_args()
    fm = Frame()

    if sp.info:
        fm.open(sp.info.value)
        fm.info()

    else:
        for l in msg.split("\n"):
            c, e = (l + " ::: ").split(':::')[:2]
            print("{:<50} {:<20}".format(c, e))
