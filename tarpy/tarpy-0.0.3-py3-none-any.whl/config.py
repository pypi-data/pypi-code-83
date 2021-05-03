''' Config

Config Variables for tarpy Package.
'''

import os
from datetime import datetime
from pathlib import Path


# Define Static Variables
SYSTEM = os.uname().sysname
SYSTEMNAME = os.uname().release
MACHINE = os.uname().machine
HOST = os.uname().nodename
ARCHITECTURE = os.uname().machine
OWNDIR = os.path.dirname(os.path.realpath(__file__))
TODAY = datetime.today().strftime('%Y-%m-%d')
EXCLUDE_FILE = '/usr/local/include/backup_exclusions.txt'

# The Config File
CONFIG_FILE = Path(Path.home() / '.tarpy/user.conf').resolve()


# Check for Config
if not os.path.exists(os.fspath(CONFIG_FILE)):
    # conf_dialog()
    ...

# Read Config and Set Variables
...
