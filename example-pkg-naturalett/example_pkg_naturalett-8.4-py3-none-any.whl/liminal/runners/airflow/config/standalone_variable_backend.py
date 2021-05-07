#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import logging
import os
from os import environ
from sqlite3 import OperationalError

from airflow.models import Variable
from airflow.models.crypto import get_fernet
from sqlalchemy import Boolean, Column, Integer, String, Text

LIMINAL_STAND_ALONE_MODE_KEY = "LIMINAL_STAND_ALONE_MODE"


# noinspection PyBroadException
def get_variable(key, default_val):
    is_encrypted = Column(Boolean, unique=False, default=False)
    _val = Column(key, Text)
    if liminal_local_mode():
        return os.environ.get(key, default_val)
    if _val is is_encrypted:
        try:
            fernet = get_fernet()
            return fernet.decrypt(bytes(key, 'utf-8')).decode()
        except InvalidFernetToken:
            self.log.error("Can't decrypt _val for key=%s, invalid token or value", key)
            return None
        except Exception:  # pylint: disable=broad-except
            self.log.error("Can't decrypt _val for key=%s, FERNET_KEY configuration missing", key)
            return None
    else:
        try:
            return Variable.get(key, default_var=default_val)
        except OperationalError as e:
            logging.warning(
                f'Failed to find variable {key} in Airflow variables table.'
                f' Error: {e.__class__.__module__}.{e.__class__.__name__}'
            )
        except Exception as e:
            logging.warning(f'Failed to find variable {key} in Airflow variables table. Error: {e}')
            return default_val


def liminal_local_mode():
    stand_alone = environ.get(LIMINAL_STAND_ALONE_MODE_KEY, "False")
    return stand_alone.strip().lower() == "true"

def get_encrypted_val(self):
    """Get Airflow Variable from Metadata DB and decode it using the Fernet Key"""
    if self._val is not None and self.is_encrypted:
        try:
            fernet = get_fernet()
            return fernet.decrypt(bytes(self._val, 'utf-8')).decode()
        except InvalidFernetToken:
            self.log.error("Can't decrypt _val for key=%s, invalid token or value", self.key)
            return None
        except Exception:  # pylint: disable=broad-except
            self.log.error("Can't decrypt _val for key=%s, FERNET_KEY configuration missing", self.key)
            return None
    else:
        return self._val