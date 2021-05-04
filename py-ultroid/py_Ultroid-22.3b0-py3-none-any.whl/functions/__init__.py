from pyUltroid import *

from ..dB.database import Var

DANGER = [
    "SESSION",
    "HEROKU_API",
    "base64",
    "base32",
    "get_me()",
    "phone",
    "REDIS_PASSWORD",
    "load_addons",
    "load_plugins",
    "os.system",
    "sys.stdout",
    "sys.stderr",
    "subprocess",
]
