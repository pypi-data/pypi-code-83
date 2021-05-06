# TODO
# bash completion
import os
from subprocess import CalledProcessError

import sys

from polidoro_argument.polidoro_argument_parser import PolidoroArgumentParser
from polidoro_cli import CLI, CLI_DIR


# load_environment_variables(CONFIG_FILE)
# load_environment_variables(LOCAL_ENV_FILE)
#
VERSION = '3.0.0-RC2'


def load_clis(cli_dir):
    sys.path.append(cli_dir)
    for file in os.listdir(cli_dir):
        full_path = os.path.join(cli_dir, file)
        if os.path.isfile(full_path) and not file.startswith('__') and file.endswith('.py'):
            __import__(file.replace('.py', ''))

    for file in os.listdir(cli_dir):
        full_path = os.path.join(cli_dir, file)
        if os.path.isfile(full_path) and not file.startswith('__') and file.endswith('.cli'):
            CLI.create_file_commands(full_path)


def load_default_clis():
    load_clis(CLI_DIR)
#
#
# def load_custom_clis():
#     custom_cli_path = os.environ.get("CUSTOM_CLI_PATH")
#     if custom_cli_path:
#         load_clis(os.path.expanduser(custom_cli_path))


def main():
    # Load CLIs
    load_default_clis()
    # load_custom_clis()


    try:
        PolidoroArgumentParser(version=VERSION, prog='cli').parse_args()
    except CalledProcessError as error:
        return error.returncode
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    os.environ['CLI_PATH'] = os.path.dirname(os.path.realpath(__file__))

    main()
