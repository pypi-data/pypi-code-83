from .get_gifNimage import get_gifNimage

import logging
try:
    open('CHANGELOG.md').read()
except FileNotFoundError as fnfe:
    logging.exception('Caught an error [in code used: except FileNotFoundError]' + str(fnfe))
    print('Caught an error [in code used: except FileNotFoundError]')
