import sys
import subprocess
import time
from loguru import logger


def execute_subprocess() -> None:
    command = sys.argv[1:]
    while True:
        logger.info(f"Executing `{command}`")
        subprocess.run(command)
        time.sleep(5)


def main() -> None:
    execute_subprocess()
