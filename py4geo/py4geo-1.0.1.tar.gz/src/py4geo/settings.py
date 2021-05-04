# -*- coding: utf-8 -*-

import os
from pathlib import Path
from . import __name__ as PACKAGENAME

HOME = str(Path.home())

# db settings
APP_FOLDER = HOME

# DB_FOLDER:    Sets the place where migration files will be created
#               and is the store location for SQLite databases
DB_FOLDER = os.path.join(APP_FOLDER, "databases")
DB_URI = None
DB_POOL_SIZE = 10
DB_MIGRATE = True
# DB_FAKE_MIGRATE = False  # maybe?

# location where to store uploaded files:
# UPLOAD_FOLDER = os.path.join(APP_FOLDER, "uploads")

# logger settings
LOGGERS = [
    "info:stdout"
]  # syntax "severity:filename" filename can be stderr or stdout

MATERIALIZED_VIEWS = []

PATHROOT = 'planet'

IS_H3_INSTALLED = False
