import os
import sys
import argparse
import logging

from .constants import *
from .args import parse_arguments


def print_python_path():
    logging.debug('Current PYTHONPATH:')
    for p in sys.path:
        logging.debug(f'\t{p}')


def print_cli_args(args):
    print()
    print("Server Settings")
    print("---------------")
    for arg in args.__dict__:
        print(arg + ": " + str(args.__dict__[arg]))
    print()


def print_routes(args):
    print()
    print("Server Routes")
    print("---------------")
    print(f"Liveness Probe: GET   127.0.0.1:{args.port}/")
    print(f"Score:          POST  127.0.0.1:{args.port}/score")
    print()


def set_environment_variables(args):
    os.environ[ENV_AML_APP_ROOT] = os.path.dirname(
        os.path.realpath(args.entry_script))
    os.environ[ENV_AZUREML_ENTRY_SCRIPT] = os.path.basename(
        os.path.realpath(args.entry_script))
    if(args.model_dir is not None):
        os.environ[ENV_AZUREML_MODEL_DIR] = args.model_dir
    else:
        print("The environment variable '{ENV_AZUREML_MODEL_DIR}' has not been set.".format(
            ENV_AZUREML_MODEL_DIR=ENV_AZUREML_MODEL_DIR))
        print("Use the --model_dir command line argument to set it.")


def set_path_variable(args):
    sys.path.append(os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'server'))
    sys.path.append(os.path.dirname(os.path.realpath(args.entry_script)))


def run():
    args = parse_arguments()

    set_environment_variables(args)
    set_path_variable(args)

    print_cli_args(args)
    print_routes(args)
    print_python_path()

    if sys.platform == 'win32':
        from azureml_inference_server_http import amlserver_win as srv
    else:
        from azureml_inference_server_http import amlserver_linux as srv

    srv.run(DEFAULT_HOST, args.port, args.worker_count)


if __name__ == "__main__":
    run()
