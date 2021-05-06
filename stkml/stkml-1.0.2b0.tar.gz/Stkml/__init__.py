#Copyright STACKEO - INRIA 2020
#!/usr/bin/python
import os
MODULE_DIR = os.path.realpath(os.path.join(__file__, '..'))
STKML_URL_SCHEMA = 'https://stkml.stackeo.io/_static/stackml.schema.json'
LOCAL_STKML_SCHEMA = 'stackml.schema.json'
STKML_PACKAGES = '.stkml_packages'
STKML_EXTENSION = '.stkml.yaml'
ICONS = os.path.join(MODULE_DIR, 'templates/diagram/resources/')
__version__ = '1.0.2b'
STACKIHUB_URL = 'https://stackhub-dev.osc-fr1.scalingo.io/api/v1'
STKML_METADATA = os.path.join(MODULE_DIR, 'templates', 'StkmlIn', 'stkml.yaml.json')
