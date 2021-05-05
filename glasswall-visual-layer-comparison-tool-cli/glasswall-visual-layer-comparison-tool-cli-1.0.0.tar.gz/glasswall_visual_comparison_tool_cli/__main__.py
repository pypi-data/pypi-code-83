import os
import logging
import json
import uuid
import click
import requests
from requests.exceptions import RequestException
from datetime import datetime
from visual_compare_result import VisualCompareResult

@click.group()
def cli():
    pass


class Logger:
    def __init__(self, log_directory: str, log_file_prefix: str, non_verbose: bool):
        self.non_verbose = non_verbose

        log_file_path = os.path.join(
            log_directory, f"{log_file_prefix}-{datetime.now():%Y-%m-%d_%H-%M-%S}.log")
        log_format = '[%(levelname)s] %(message)s'
        log_level = logging.INFO

        logging.basicConfig(
            filename=log_file_path,
            filemode="a",
            format=log_format,
            level=log_level)

        console = logging.StreamHandler()
        console.setLevel(log_level)
        console.setFormatter(logging.Formatter(log_format))

        logging.getLogger('').addHandler(console)

    def _process_message(self, message, extra_data=None) -> str:
        if not self.non_verbose and extra_data is not None:
            return message + f" -- {str(extra_data)}"
        else:
            return message

    def info(self, message, extra_data=None):
        logging.info(
            self._process_message(message, extra_data))

    def warning(self, message, extra_data=None):
        logging.warning(
            self._process_message(message, extra_data))

    def error(self, message, extra_data=None):
        logging.error(
            self._process_message(message, extra_data))


def api_health_check(url: str) -> bool:
    try:
        click.echo(f"Sending health check request to: {url}")

        response = requests.request("GET", url, headers={}, data={})

        return response.ok

    except RequestException as e:
        click.echo(f"API Health Check Failed:\n{e}")

        return False

def list_files(logger: Logger, dir: str) -> list:
    files = []

    for f in os.listdir(dir):
        file = os.path.join(dir, f)
        if (os.path.isfile(file)):
            files.append(f)
        else:
            logger.warning(f"Non-file found", os.path.join(dir, file))

    return files


@cli.command()
@click.option("--url", "-u", required=True, help="URL for the GW Comparison API")
@click.option("--left", "-l", required=True, help="Directory for the original files (the left side of the comparison)")
@click.option("--right", "-r", required=True, help="Directory for the rebuilt files (the right side of the comparison)")
@click.option("--log", required=True, help="Directory to store log file")
@click.option("--non_verbose", is_flag=True, help="Non Verbose logging (hides filenames)")
def dir_compare(url: str, left: str, right: str, log: str, non_verbose: bool):

    def send_to_api(file_pair: list, reference: str) -> requests.Response:
        left_file_path = os.path.join(left, file_pair[0])
        right_file_path = os.path.join(right, file_pair[1])

        fn, file_type = os.path.splitext(file_pair[0])
        file_type = file_type.replace(".", "")

        full_url = f"{url}/visual_compare?reference={reference}&filetype={file_type}"

        files = [
            ('left_file', (file_pair[0], open(left_file_path, 'rb'), '')),
            ('right_file', (file_pair[1], open(right_file_path, 'rb'), ''))
        ]

        return requests.request(
            "POST", full_url, headers={}, data={}, files=files)

    if not os.path.exists(left):
        click.echo("Left directory does not exist")
        return

    if not os.path.exists(right):
        click.echo("Right directory does not exist")
        return

    if not os.path.exists(log):
        click.echo("Log file Path Does Not Exist")
        return

    if not api_health_check(url):
        return

    logger = Logger(log, "dir-compare", non_verbose)

    left_files = list_files(logger, left)
    if (len(left_files) < 1):
        logger.error("Left directory was empty")
        return

    right_files = list_files(logger, right)
    if(len(right_files) < 1):
        logger.error("Right directory was empty")
        return

    missing_files = list(set(left_files) ^ set(right_files))
    if len(missing_files) != 0:
        logger.warning(
            "Some files were missing from the right directory", extra_data=missing_files)

    for file_pair in zip(left_files, right_files):
        # If FileNames match
        if file_pair[0] == file_pair[1]:
            reference = str(uuid.uuid4())

            response = send_to_api(file_pair, reference)

            if not response.ok:
                error = f"{response.status_code} - {response.reason}"
                logger.error(
                    f"reference: {reference} -- {error}", extra_data=f"file_name: {file_pair[0]}")
                continue

            vlc_tool_response = json.loads(response.text)
            return_status = vlc_tool_response["return_status"]
            result = VisualCompareResult(return_status)

            logger.info(
                f"reference: {reference} -- result: {result.name} ({return_status})", extra_data=f"file_name: {file_pair[0]}")

        else:
            logger.info(f"Could not find match",
                        extra_data=f"Left {file_pair[0]} - Right {file_pair[1]}")


if __name__ == "__main__":
    cli()
