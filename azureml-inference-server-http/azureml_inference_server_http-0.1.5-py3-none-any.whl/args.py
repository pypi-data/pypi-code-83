import argparse
import logging
import sys
from .constants import DEFAULT_PORT, DEFAULT_WORKER_COUNT, ENV_AZUREML_MODEL_DIR


def print_arguments(args):
    for arg in vars(args):
        logging.debug(arg + ":" + str(args.__dict__[arg]))


def validate_port(port):
    port = int(port)
    if(port < 1 or port > 65535):
        raise ValueError(
            f"Specified port '{port}' is invalid. Please specify a port within range the [1, 65535] range.")
    return port


def validate_worker_count(worker_count):
    worker_count = int(worker_count)
    if(worker_count <= 0):
        raise ValueError(
            "Specified worker count '{worker_count}' is invalid. Please specify a worker count greater than zero.".format(worker_count=worker_count))
    return worker_count


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Azure ML Inferencing HTTP server",
        add_help=True)

    parser.add_argument(
        '--entry_script',
        required=True,
        help='The relative or absolute path to the scoring script.')

    parser.add_argument(
        '--model_dir',
        required=False,
        help="The relative or absolute path to the model directory. The model directory will be accessible through the '{ENV_AZUREML_MODEL_DIR}' environment variable."
        .format(ENV_AZUREML_MODEL_DIR=ENV_AZUREML_MODEL_DIR))

    parser.add_argument(
        '--port',
        required=False,
        type=validate_port,
        default=DEFAULT_PORT,
        help='The serving port of the server. Default is 5001.')

    parser.add_argument(
        '--worker_count',
        required=False,
        type=validate_worker_count,
        default=DEFAULT_WORKER_COUNT,
        help='The number of worker threads which will process concurrent requests. Default is 1.')

    try:
        args = parser.parse_args()
    except SystemExit as err:
        if err.code == 2:
            print()
            # Don't print usage when parsing the command line.
            parser.usage = argparse.SUPPRESS
            parser.print_help()
            parser.usage = None
        sys.exit(1)

    try:
        print_arguments(args)
    except:
        logging.debug("Failed to print arguments '{args}'".format(args=args))

    return args
