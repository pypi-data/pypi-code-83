from locale import getdefaultlocale
from os.path import expanduser

DAYS_IN_A_SECOND = 0.0000115741
BUDGET_FILE = "./budget.yml"
HISTORY_FILE = "./history.csv"
DEFAULT_LOCALE = getdefaultlocale()[0]
CONFIG_FILE_PATH = expanduser("~/.lbudrc.yml")
