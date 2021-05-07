import os
import logging
import json
import uuid
import click
import requests
from enum import Enum
from requests.exceptions import RequestException
from datetime import datetime
from typing import List

@click.group()
def cli():
    pass


class VisualCompareResult(Enum):
    Match = 0
    ContentMismatch = 1
    FileMismatch = 2
    ProcessingError = 3
    ConversionError = 4
    UnsupportedFileType = 5
    InvalidArguements = 6
    TimeOut = 7
    ReferenceExists = 8


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
    
    def debug(self, message, extra_data=None):
        logging.debug(
            self._process_message(message, extra_data))

    def info(self, message, extra_data=None):
        logging.info(
            self._process_message(message, extra_data))

    def warning(self, message, extra_data=None):
        logging.warning(
            self._process_message(message, extra_data))

    def error(self, message, extra_data=None):
        logging.error(
            self._process_message(message, extra_data))


class CoreAPIs:
    def __init__(self, file_pair: List):
        self.is_test_submitted = False
        self.time_submitted = None
        self.is_ready_to_get_result = False
        self.reference = str(uuid.uuid4())
        self.file_pair = file_pair
    
    def submit_test_api(self, left, right, url) -> None:
        left_file_path = os.path.join(left, self.file_pair[0])
        right_file_path = os.path.join(right, self.file_pair[1])

        fn, file_type = os.path.splitext(self.file_pair[0])
        file_type = file_type.replace(".", "")

        full_url = f"{url}/core/visual_compare?reference={self.reference}&filetype={file_type}"

        files = [
            ('left_file', (self.file_pair[0], open(left_file_path, 'rb'), '')),
            ('right_file', (self.file_pair[1], open(right_file_path, 'rb'), ''))
        ]

        response = requests.request("POST", full_url, headers={}, data={}, files=files)

        vlc_tool_response = json.loads(response.text)
        return_status = vlc_tool_response["return_status"]

        if return_status == 0:
            self.is_test_submitted = True
            self.time_submitted = datetime.now()

    def poll_api(self, url) -> None:
        full_url = f"{url}/core/poll/{self.reference}"
        
        response = requests.request("GET", full_url, headers={}, data={})

        if response.status_code == 200:
            if int(response.text) == 0:
                self.is_ready_to_get_result = True

    def get_result_api(self, url) -> requests.Response:
        full_url = f"{url}/core/result/{self.reference}"
        
        return requests.request("GET", full_url, headers={}, data={})

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

def send_to_api(left, right, url, file_pair: list, reference: str) -> requests.Response:
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

def dir_compare_validation(left, right, log) -> int:
    """
    Validate the Paths exist

    Return:
        - 0: Passed Validation
        - 1: Validation Failure Detected
    """
    if not os.path.exists(left):
        click.echo("Left directory does not exist")
        return 1

    if not os.path.exists(right):
        click.echo("Right directory does not exist")
        return 1

    if not os.path.exists(log):
        click.echo("Log file Path Does Not Exist")
        return 1

    return 0

def check_for_empty_dirs(left_files: List, right_files: List, logger) -> int:
    """
    Validate the Paths exist
    
    Return:
        - 0: Passed Checks
        - 1: Issue Detected
    """
    if (len(left_files) < 1):
        logger.error("Left directory was empty")
        return 1

    if(len(right_files) < 1):
        logger.error("Right directory was empty")
        return 1

    return 0

def log_result(response: requests.Response, logger, reference, file_pair, is_aws=False) -> None:
    """
    Log the result obtained from the visual comparison process.
    """
    vlc_tool_response = json.loads(response.text)
    if is_aws:
        return_status = vlc_tool_response["result"]
    else:
        return_status = vlc_tool_response["return_status"]
    result = VisualCompareResult(return_status)
    logger.info(
        f"reference: {reference} -- result: {result.name} ({return_status})", extra_data=f"file_name: {file_pair[0]}")

def log_issue(response: requests.Response, logger, reference, file_pair) -> None:
    """
    Log an issue.
    """
    error = f"{response.status_code} - {response.reason}"
    logger.error(
        f"reference: {reference} -- {error}", extra_data=f"file_name: {file_pair[0]}")

def detect_missing_files(left_files: List, right_files: List, logger) -> None:
    """
    Detect any missing files and log missing files.
    """
    missing_files = list(set(left_files) ^ set(right_files))
    if len(missing_files) != 0:
        logger.warning(
            "Some files were missing from the right directory", extra_data=missing_files)

@cli.command(help="Recommended (> 500 file pairs) for performance enhancement.")
@click.option("--url", "-u", required=True, help="URL for the GW Comparison API")
@click.option("--left", "-l", required=True, help="Directory for the original files (the left side of the comparison)")
@click.option("--right", "-r", required=True, help="Directory for the rebuilt files (the right side of the comparison)")
@click.option("--log", required=True, help="Directory to store log file")
@click.option("--non_verbose", is_flag=True, help="Non Verbose logging (hides filenames)")
def aws_dir_compare(url: str, left: str, right: str, log: str, non_verbose: bool):

    if dir_compare_validation(left, right, log) == 1:
        return

    if not api_health_check(url):
        return

    logger = Logger(log, "dir-compare", non_verbose)

    left_files = list_files(logger, left)
    right_files = list_files(logger, right)

    if check_for_empty_dirs(left_files, right_files, logger) == 1:
        return

    detect_missing_files(left_files, right_files, logger)

    tests_submitted = []

    click.echo("Starting Submission of Files to Gw Visual Comparison Tool API...")
    for file in left_files:
        file_pair = [os.path.join(left, file), os.path.join(right, file)]
        if os.path.exists(file_pair[0]) and os.path.exists(file_pair[1]):

            api = CoreAPIs(file_pair)
            api.submit_test_api(left, right, url)

            tests_submitted.append(api)
            click.echo(".", nl=False)
        
        else:
            logger.info(f"Could not find match",
                        extra_data=f"Left {file_pair[0]} - Right {file_pair[1]}")

    click.echo("")
    del left_files
    del right_files

    while len(tests_submitted) > 0:
        test_submitted = tests_submitted.pop(0)

        test_submitted.poll_api(url)

        if test_submitted.is_ready_to_get_result == False:
            # Add To Back of List to allow process time
            tests_submitted.append(test_submitted)
        else:
            response = test_submitted.get_result_api(url)

            if not response.ok:
                log_issue(response, logger, test_submitted.reference, test_submitted.file_pair)
                continue

            log_result(response, logger, test_submitted.reference, test_submitted.file_pair, is_aws=True)



@cli.command()
@click.option("--url", "-u", required=True, help="URL for the GW Comparison API")
@click.option("--left", "-l", required=True, help="Directory for the original files (the left side of the comparison)")
@click.option("--right", "-r", required=True, help="Directory for the rebuilt files (the right side of the comparison)")
@click.option("--log", required=True, help="Directory to store log file")
@click.option("--non_verbose", is_flag=True, help="Non Verbose logging (hides filenames)")
def dir_compare(url: str, left: str, right: str, log: str, non_verbose: bool):

    if dir_compare_validation(left, right, log) == 1:
        return

    if not api_health_check(url):
        return

    logger = Logger(log, "dir-compare", non_verbose)

    left_files = list_files(logger, left)
    right_files = list_files(logger, right)

    if check_for_empty_dirs(left_files, right_files, logger) == 1:
        return

    detect_missing_files(left_files, right_files, logger)

    for file in left_files:
        file_pair = [os.path.join(left, file), os.path.join(right, file)]
        if os.path.exists(file_pair[0]) and os.path.exists(file_pair[1]):

            reference = str(uuid.uuid4())

            response = send_to_api(left, right, url, file_pair, reference)

            if not response.ok:
                log_issue(response, logger, reference, file_pair)
                continue

            log_result(response, logger, reference, file_pair)

        else:
            logger.info(f"Could not find match",
                        extra_data=f"Left {file_pair[0]} - Right {file_pair[1]}")


if __name__ == "__main__":
    cli()
