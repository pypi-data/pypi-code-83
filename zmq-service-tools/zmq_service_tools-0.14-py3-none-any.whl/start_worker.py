from configparser import ConfigParser
import argparse
import os
import uuid

from .worker import Worker
from .message import Message


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--config_file', required=True, help="worker config file", type=str)
    args = parser.parse_args()
    config_file = args.config_file

    print(f'reading config file: {config_file}')
    if not os.path.isfile(config_file):
        raise FileExistsError(f'{config_file} does not exist')
    config = ConfigParser()
    config.read(config_file)

    try:
        name = config.get('main', 'name', fallback=None)
    except Exception as e:
        name = ''

    try:
        id = uuid.UUID(config.get('main', 'id', fallback=None))
    except Exception as e:
        id = ''

    try:
        ip = config.get('main', 'ip', fallback=None)
    except Exception as e:
        print('ip in {self.config_path} does not exist. Assume localhost...')
        ip = 'localhost'

    print(f'starting worker: \n     name: {name} \n     id: {id} \n     ip: {ip}')
    new_worker = Worker(config_path=config_file)
    new_worker.start()
