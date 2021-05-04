import os

BASE_DIR = ".yamlflow"
MANIFEST_FILE = "yamlflow.yaml"
#TODO: already defined in gunicorn logs, get rid of assigning default values here!
WEB_CONCURRENCY = int(os.getenv("WEB_CONCURRENCY", "1"))
