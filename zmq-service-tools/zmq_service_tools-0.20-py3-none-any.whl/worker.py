import uuid
import os
import zmq
import zmq.auth
from zmq.auth.thread import ThreadAuthenticator
import logging
import time

from configparser import ConfigParser
from .message import Message
import socket
import sys


class WorkerConfig(object):

    @classmethod
    def create_new(cls, config_path, *args, **kwargs):
        """
        Creates a new server config file at config_path.

        :param config_path:         path where to store the config file; example: 'config.ini'
        :param args:
        :param kwargs:
        :keyword id:                id of the server; uuid.UUID4
        :keyword name:              name of the server; str
        :keyword ip:                ip address of the server; str; examples: 'localhost', '127.0.0.1'
        :keyword port:              port of the server; str; examples: 8005
        :keyword backend_port:      port used for communication with the workers; int; examples: 8006; optional; as default a free port between 9001 and 9050 is choosen
        :keyword public_keys_dir:   directory where public_keys are stored; str
        :keyword secret_keys_dir:   directory where secret_keys are stored; str
        :keyword num_workers:       number of workers which are created; int
        :keyword log_dir:           directory of log; str
        :return:
        """
        config = ConfigParser(allow_no_value=True)
        if config_path is None:
            raise ValueError(f'config_path is None')

        config.add_section('main')

        config.set('main', 'id', str(kwargs.get('id', uuid.uuid4())))
        config.set('main', 'name', kwargs.get('name', None))
        config.set('main', 'ip', str(kwargs.get('ip', None)))
        config.set('main', 'port', str(kwargs.get('port', None)))
        config.set('main', 'public_keys_dir', str(kwargs.get('public_keys_dir', None)))
        config.set('main', 'secret_keys_dir', str(kwargs.get('secret_keys_dir', None)))
        config.set('main', 'python_path', str(kwargs.get('python_path', '')))

        config.add_section('logging')
        config.set('logging', 'log_dir', kwargs.get('log_dir', None))
        config.set('logging', 'logging_mode', kwargs.get('logging_mode', 'DEBUG'))

        if not os.path.isfile(config_path):
            f = open(config_path, 'a')
            f.close()
            with open(config_path, 'w') as f:
                config.write(f)

        return cls(config_path)

    def __init__(self, config_path, *args, **kwargs):

        self.config = ConfigParser()
        self.config_path = config_path

        if self.config_path is None:
            raise ValueError(f'config_path is None')

        self._id = None
        self._name = None

        self._public_keys_dir = None
        self._secret_keys_dir = None
        self._ip = None
        self._port = None
        self._python_path = None

        # logging
        self._log_dir = None
        self._logging_mode = None

        if not os.path.isfile(self.config_path):
            raise Exception(f'{self.config_path} does not exist')

        self.read_config()

    @property
    def id(self):
        if self._id is None:
            self.read_config()
        return self._id

    @id.setter
    def id(self, value):

        self.config.set('main', 'id', str(value))
        self.write_config()
        self._id = value

    @property
    def name(self):
        if self._name is None:
            self.read_config()
        return self._name

    @name.setter
    def name(self, value):

        self.config.set('main', 'name', value)
        self.write_config()
        self._name = value

    @property
    def ip(self):
        if self._ip is None:
            self.read_config()
        return self._ip

    @ip.setter
    def ip(self, value):

        self.config.set('main', 'ip', str(value))
        self.write_config()
        self._ip = value

    @property
    def port(self):
        if self._port is None:
            self.read_config()
        return self._port

    @port.setter
    def port(self, value):

        self.config.set('main', 'port', str(value))
        self.write_config()
        self._port = value

    @property
    def python_path(self):
        if self._python_path is None:
            self.read_config()
        return self._python_path

    @python_path.setter
    def python_path(self, value):
        self.config.set('main', 'python_path', str(value))
        self.write_config()
        self._python_path = value

    @property
    def public_keys_dir(self):
        if self._public_keys_dir is None:
            self.read_config()
        return self._public_keys_dir

    @public_keys_dir.setter
    def public_keys_dir(self, value):

        self.config.set('main', 'public_keys_dir', value)
        self.write_config()
        self._public_keys_dir = value

    @property
    def secret_keys_dir(self):
        if self._secret_keys_dir is None:
            self.read_config()
        return self._secret_keys_dir

    @secret_keys_dir.setter
    def secret_keys_dir(self, value):

        self.config.set('main', 'secret_keys_dir', value)
        self.write_config()
        self._secret_keys_dir = value

    @property
    def log_dir(self):
        if self._log_dir is None:
            self.read_config()
        return self._log_dir

    @log_dir.setter
    def log_dir(self, value):

        self.config.set('logging', 'log_dir', value)
        self.write_config()
        self._log_dir = value

    @property
    def logging_mode(self):
        if self._logging_mode is None:
            self.read_config()
        return self._logging_mode

    @logging_mode.setter
    def logging_mode(self, value):

        self.config.set('logging', 'logging_mode', value)
        self.write_config()
        self._logging_mode = value

    def read_config(self):

        if not os.path.isfile(self.config_path):
            raise FileExistsError(f'{self.config_path} does not exist')
        self.config.read(self.config_path)

        try:
            self._public_keys_dir = self.config.get('main', 'public_keys_dir', fallback=None)
        except Exception as e:
            raise Exception(f'Error: public_keys_dir in {self.config_path} does not exist')

        try:
            self._secret_keys_dir = self.config.get('main', 'secret_keys_dir', fallback=None)
        except Exception as e:
            raise Exception(f'Error: secret_keys_dir in {self.config_path} does not exist')

        try:
            self._port = self.config.getint('main', 'port', fallback=None)
        except Exception as e:
            print('port in {self.config_path} does not exist')

        try:
            self._name = self.config.get('main', 'name', fallback=None)
        except Exception as e:
            print('name in {self.config_path} does not exist')

        try:
            self._id = uuid.UUID(self.config.get('main', 'id', fallback=None))
        except Exception as e:
            raise Exception(f'Error: id in {self.config_path} does not exist')

        try:
            self._ip = self.config.get('main', 'ip', fallback=None)
        except Exception as e:
            print('ip in {self.config_path} does not exist. Assume localhost...')
            self._ip = 'localhost'

        try:
            self._python_path = self.config.get('main', 'python_path', fallback=None)
        except Exception as e:
            print('python_path in {self.config_path} does not exist. Assume system python')
            self._python_path = 'python'

        ##############################################
        # logging
        ##############################################

        try:
            self._log_dir = self.config.get('logging', 'log_dir', fallback=None)
        except Exception as e:
            print('log_dir in {self.config_path} does not exist')
            self._log_dir = None

        try:
            self._logging_mode = self.config.get('logging', 'logging_mode', fallback=None)
        except Exception as e:
            print('logging_mode in {self.config_path} does not exist')
            self._logging_mode = 'DEBUG'

    def write_config(self):

        try:
            with open(self.config_path, 'w') as f:
                self.config.write(f)
        except Exception as e:
            print(f'error writing config: {e}')


class Worker(WorkerConfig):

    def __init__(self, config_path, *args, **kwargs):

        WorkerConfig.__init__(self, config_path, *args, **kwargs)

        self.logger = None
        self.init_logger()

        self.fh = None  # logger file handler
        self.ch = None  # logger console channel

        self.context = zmq.Context()

        self.socket = self.context.socket(zmq.REP)

    @property
    def address(self):
        return f'tcp://{self.ip}:{self.port}'

    @property
    def logging_mode(self):
        return self._logging_mode

    @logging_mode.setter
    def logging_mode(self, value):
        self._logging_mode = value

        # if self.logging_mode == 'DEBUG':
        #     level = logging.DEBUG
        # elif self.logging_mode == 'INFO':
        #     level = logging.INFO
        # elif self.logging_mode == 'WARN':
        #     level = logging.WARN
        # elif self.logging_mode == 'ERROR':
        #     level = logging.ERROR
        # else:
        #     level = logging.INFO
        #
        # self.logger.setLevel(level)
        # self.fh.setLevel(level)
        # self.ch.setLevel(level)

        self.logger.info(f'logger level set to {value}')
        self.update_logging_mode()

    def init_logger(self):

        self.logger = logging.getLogger(str(self.id))
        log_filename = os.path.join(self.log_dir, f'worker_{str(self.id)}' + "." + 'log')
        self.fh = logging.FileHandler(log_filename)  # create file handler which logs even debug messages
        self.ch = logging.StreamHandler()  # create console handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

        self.update_logging_mode()

        self.logger.info(f'logger started')

    def update_logging_mode(self):

        if self.logging_mode == 'DEBUG':
            level = logging.DEBUG
        elif self.logging_mode == 'INFO':
            level = logging.INFO
        elif self.logging_mode == 'WARN':
            level = logging.WARN
        elif self.logging_mode == 'ERROR':
            level = logging.ERROR
        else:
            level = logging.INFO

        self.logger.setLevel(level)
        self.fh.setLevel(level)
        self.ch.setLevel(level)

        self.logger.info(f'logger level is {self.logging_mode}')

    def start(self):

        self.logger.info(f'starting on: {self.address}')

        try:
            self.socket.connect(self.address)
        except Exception as e:
            self.logger.error(f'error while starting worker: \n{e}')
            return e

        self.logger.info(f'worker started')

        while True:
            try:
                message = self.socket.recv_pyobj()
            except Exception as e:
                self.logger.error(f'error receiving message:\n{e}')
                self.socket.send_pyobj(e)
                continue

            try:
                self.socket.send_pyobj(self.process_request(message))
            except Exception as e:
                self.logger.error(f'error while processing {message}:\n{e}')
                self.socket.send_pyobj(e)

    def shutdown(self):
        sys.exit()

    def process_request(self, message):

        # self.logger.info(f'hello from new worker. processing request...')
        method = getattr(self, message.method)
        # self.logger.info(f'method to execute: {method}')

        return getattr(self, message.method)(*message.args, **message.kwargs)

    def get_ip(self, *args, **kwargs):
        return 'try to get your ip'
        hostname = "max"
        ip_address = socket.gethostbyname(hostname)

    def __del__(self):
        self.logger.info(f'deleted')
