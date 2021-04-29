import uuid
import os
import zmq
import zmq.auth
from os import path
from zmq.auth.thread import ThreadAuthenticator
import logging
import time
import colorlog

from configparser import ConfigParser
from .message import Message
import socket
import sys
import socketserver

from ruamel.yaml import YAML, yaml_object, add_representer
from functools import wraps

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources


formatters = {
    logging.DEBUG: logging.Formatter("[%(app_name)s - %(name)s] %(message)s"),
    logging.INFO: logging.Formatter("[%(app_name)s - %(name)s] %(message)s"),
    logging.WARN: logging.Formatter("[%(app_name)s - %(name)s] %(message)s"),
    logging.ERROR: logging.Formatter("[%(app_name)s - %(name)s] %(message)s"),
    logging.CRITICAL: logging.Formatter("[%(app_name)s - %(name)s] %(message)s")
}

color_formatter = colorlog.ColoredFormatter(
    "%(log_color)s[%(app_name)s] %(asctime)s; %(log_color)s%(levelname)-8s%(reset)s %(message_log_color)s:%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'bold_red',
        'CRITICAL': 'bold_black,bg_red',
    },
    secondary_log_colors={
        'message': {
            'DEBUG':    'cyan',
            'INFO':     'white',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red'
        }
    },
    style='%'
)


def represent_none(self, _):
    return self.represent_scalar('tag:yaml.org,2002:null', '')


add_representer(type(None), represent_none)
yaml = YAML()
yaml.indent(sequence=4, offset=2)


def file_sync(method):
    """
    If synced attribute has changed write config to file

    Example:

    class Test(object):

        yaml_tag = u'!Test'
        config_path = None

        def __init__(self):
            self._a = 1

        @property
        def a(self):
            return self.a


        @a.setter
        @file_sync
        def a(self, value):
            self._a = value

        def write(self, filepath=None):

            if filepath is None:
                filepath = self.config_path

            with open(filepath, mode='w') as f_obj:
                yaml.dump(self, f_obj)

    Test.config_path = 'config.yml'
    test = Test()


    :param method:
    :return:
    """
    attr = method.__name__
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        old_val = self.__getattribute__(attr)
        method_output = method(self, *method_args, **method_kwargs)
        new_val = self.__getattribute__(attr)

        if old_val != new_val:
            self.write()
        return method_output
    return _impl


@yaml_object(yaml)
class WorkerConfig(object):

    yaml_tag = u'!WorkerConfig'

    @classmethod
    def create_new(cls, *args, **kwargs):
        worker_config = cls(*args, **kwargs)
        worker_config.config_path = kwargs.get('config_path')

        return worker_config

    def __init__(self, *args, **kwargs):

        self.config_path = kwargs.get('config_path')

        self.__update_file = False
        self.__on_init = True

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

        if not path.isfile(self.config_path):
            f = open(self.config_path, 'a')
            f.close()

        defaults = {'id': str(uuid.uuid4()),
                    'name': '',
                    'public_keys_dir': None,
                    'secret_keys_dir': None,
                    'ip': '127.0.0.1',
                    'port': None,
                    'python_path': None,
                    'log_dir': None,
                    'logging_mode': 'INFO'}

        for key in ['id',
                    'name',
                    'public_keys_dir',
                    'secret_keys_dir',
                    'ip',
                    'port',
                    'python_path',
                    'log_dir',
                    'logging_mode']:

            setattr(self, key, kwargs.get(key, kwargs.get('_'+key, defaults[key])))

        self.__on_init = False

        if self.__update_file:
            self.write()

    @property
    def id(self):
        return self._id

    @id.setter
    @file_sync
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    @file_sync
    def name(self, value):
        self._name = value

    @property
    def ip(self):
        return self._ip

    @ip.setter
    @file_sync
    def ip(self, value):
        self._ip = value

    @property
    def port(self):
        return self._port

    @port.setter
    @file_sync
    def port(self, value):
        self._port = value

    @property
    def python_path(self):
        return self._python_path

    @python_path.setter
    @file_sync
    def python_path(self, value):
        self._python_path = value

    @property
    def public_keys_dir(self):
        return self._public_keys_dir

    @public_keys_dir.setter
    @file_sync
    def public_keys_dir(self, value):
        self._public_keys_dir = value

    @property
    def secret_keys_dir(self):
        return self._secret_keys_dir

    @secret_keys_dir.setter
    @file_sync
    def secret_keys_dir(self, value):
        self._secret_keys_dir = value

    @property
    def log_dir(self):
        return self._log_dir

    @log_dir.setter
    @file_sync
    def log_dir(self, value):
        self._log_dir = value

    @property
    def logging_mode(self):
        return self._logging_mode

    @logging_mode.setter
    @file_sync
    def logging_mode(self, value):
        self._logging_mode = value

    def write(self, filepath=None):

        if self.__on_init:
            self.__update_file = True
            return

        if filepath is None:
            filepath = self.config_path

        with open(filepath, mode='w') as f_obj:
            yaml.dump(self, f_obj)

    def __getstate__(self):

        state = self.__dict__.copy()

        keys_to_del = ['config_path',
                       '__update_file',
                       '__on_init',
                       '_WorkerConfig__update_file',
                       '_WorkerConfig__on_init']

        for key in keys_to_del:
            if key in state.keys():
                del state[key]

        return state

    def __setstate__(self, state):

        state['__update_file'] = False
        state['__on_init'] = True

        self.__dict__ = state

        self.__on_init = False




# class WorkerConfig(object):
#
#     @classmethod
#     def create_new(cls, config_path, *args, **kwargs):
#         """
#         Creates a new server config file at config_path.
#
#         :param config_path:         path where to store the config file; example: 'config.ini'
#         :param args:
#         :param kwargs:
#         :keyword id:                id of the server; uuid.UUID4
#         :keyword name:              name of the server; str
#         :keyword ip:                ip address of the server; str; examples: 'localhost', '127.0.0.1'
#         :keyword port:              port of the server; str; examples: 8005
#         :keyword backend_port:      port used for communication with the workers; int; examples: 8006; optional; as default a free port between 9001 and 9050 is choosen
#         :keyword public_keys_dir:   directory where public_keys are stored; str
#         :keyword secret_keys_dir:   directory where secret_keys are stored; str
#         :keyword num_workers:       number of workers which are created; int
#         :keyword log_dir:           directory of log; str
#         :return:
#         """
#         config = ConfigParser(allow_no_value=True)
#         if config_path is None:
#             raise ValueError(f'config_path is None')
#
#         config.add_section('main')
#
#         config.set('main', 'id', str(kwargs.get('id', uuid.uuid4())))
#         config.set('main', 'name', kwargs.get('name', None))
#         config.set('main', 'ip', str(kwargs.get('ip', None)))
#         config.set('main', 'port', str(kwargs.get('port', None)))
#         config.set('main', 'public_keys_dir', str(kwargs.get('public_keys_dir', None)))
#         config.set('main', 'secret_keys_dir', str(kwargs.get('secret_keys_dir', None)))
#         config.set('main', 'python_path', str(kwargs.get('python_path', '')))
#
#         config.add_section('logging')
#         config.set('logging', 'log_dir', kwargs.get('log_dir', None))
#         config.set('logging', 'logging_mode', kwargs.get('logging_mode', 'DEBUG'))
#
#         if not os.path.isfile(config_path):
#             f = open(config_path, 'a')
#             f.close()
#             with open(config_path, 'w') as f:
#                 config.write(f)
#
#         return cls(config_path)
#
#     def __init__(self, config_path, *args, **kwargs):
#
#         self.config = ConfigParser()
#         self.config_path = config_path
#
#         if self.config_path is None:
#             raise ValueError(f'config_path is None')
#
#         self._id = None
#         self._name = None
#
#         self._public_keys_dir = None
#         self._secret_keys_dir = None
#         self._ip = None
#         self._port = None
#         self._python_path = None
#
#         # logging
#         self._log_dir = None
#         self._logging_mode = None
#
#         if not os.path.isfile(self.config_path):
#             raise Exception(f'{self.config_path} does not exist')
#
#         self.read_config()
#
#     @property
#     def id(self):
#         if self._id is None:
#             self.read_config()
#         return self._id
#
#     @id.setter
#     def id(self, value):
#
#         self.config.set('main', 'id', str(value))
#         self.write_config()
#         self._id = value
#
#     @property
#     def name(self):
#         if self._name is None:
#             self.read_config()
#         return self._name
#
#     @name.setter
#     def name(self, value):
#
#         self.config.set('main', 'name', value)
#         self.write_config()
#         self._name = value
#
#     @property
#     def ip(self):
#         if self._ip is None:
#             self.read_config()
#         return self._ip
#
#     @ip.setter
#     def ip(self, value):
#
#         self.config.set('main', 'ip', str(value))
#         self.write_config()
#         self._ip = value
#
#     @property
#     def port(self):
#         if self._port is None:
#             self.read_config()
#         return self._port
#
#     @port.setter
#     def port(self, value):
#
#         self.config.set('main', 'port', str(value))
#         self.write_config()
#         self._port = value
#
#     @property
#     def python_path(self):
#         if self._python_path is None:
#             self.read_config()
#         return self._python_path
#
#     @python_path.setter
#     def python_path(self, value):
#         self.config.set('main', 'python_path', str(value))
#         self.write_config()
#         self._python_path = value
#
#     @property
#     def public_keys_dir(self):
#         if self._public_keys_dir is None:
#             self.read_config()
#         return self._public_keys_dir
#
#     @public_keys_dir.setter
#     def public_keys_dir(self, value):
#
#         self.config.set('main', 'public_keys_dir', value)
#         self.write_config()
#         self._public_keys_dir = value
#
#     @property
#     def secret_keys_dir(self):
#         if self._secret_keys_dir is None:
#             self.read_config()
#         return self._secret_keys_dir
#
#     @secret_keys_dir.setter
#     def secret_keys_dir(self, value):
#
#         self.config.set('main', 'secret_keys_dir', value)
#         self.write_config()
#         self._secret_keys_dir = value
#
#     @property
#     def log_dir(self):
#         if self._log_dir is None:
#             self.read_config()
#         return self._log_dir
#
#     @log_dir.setter
#     def log_dir(self, value):
#
#         self.config.set('logging', 'log_dir', value)
#         self.write_config()
#         self._log_dir = value
#
#     @property
#     def logging_mode(self):
#         if self._logging_mode is None:
#             self.read_config()
#         return self._logging_mode
#
#     @logging_mode.setter
#     def logging_mode(self, value):
#
#         self.config.set('logging', 'logging_mode', value)
#         self.write_config()
#         self._logging_mode = value
#
#     def read_config(self):
#
#         if not os.path.isfile(self.config_path):
#             raise FileExistsError(f'{self.config_path} does not exist')
#         self.config.read(self.config_path)
#
#         try:
#             self._public_keys_dir = self.config.get('main', 'public_keys_dir', fallback=None)
#         except Exception as e:
#             raise Exception(f'Error: public_keys_dir in {self.config_path} does not exist')
#
#         try:
#             self._secret_keys_dir = self.config.get('main', 'secret_keys_dir', fallback=None)
#         except Exception as e:
#             raise Exception(f'Error: secret_keys_dir in {self.config_path} does not exist')
#
#         try:
#             self._port = self.config.getint('main', 'port', fallback=None)
#         except Exception as e:
#             print('port in {self.config_path} does not exist')
#
#         try:
#             self._name = self.config.get('main', 'name', fallback=None)
#         except Exception as e:
#             print('name in {self.config_path} does not exist')
#
#         try:
#             self._id = uuid.UUID(self.config.get('main', 'id', fallback=None))
#         except Exception as e:
#             raise Exception(f'Error: id in {self.config_path} does not exist')
#
#         try:
#             self._ip = self.config.get('main', 'ip', fallback=None)
#         except Exception as e:
#             print('ip in {self.config_path} does not exist. Assume localhost...')
#             self._ip = 'localhost'
#
#         try:
#             self._python_path = self.config.get('main', 'python_path', fallback=None)
#         except Exception as e:
#             print('python_path in {self.config_path} does not exist. Assume system python')
#             self._python_path = 'python'
#
#         ##############################################
#         # logging
#         ##############################################
#
#         try:
#             self._log_dir = self.config.get('logging', 'log_dir', fallback=None)
#         except Exception as e:
#             print('log_dir in {self.config_path} does not exist')
#             self._log_dir = None
#
#         try:
#             self._logging_mode = self.config.get('logging', 'logging_mode', fallback=None)
#         except Exception as e:
#             print('logging_mode in {self.config_path} does not exist')
#             self._logging_mode = 'DEBUG'
#
#     def write_config(self):
#
#         try:
#             with open(self.config_path, 'w') as f:
#                 self.config.write(f)
#         except Exception as e:
#             print(f'error writing config: {e}')


@yaml_object(yaml)
class Worker(WorkerConfig):

    yaml_tag = u'!WorkerConfig'

    @classmethod
    def from_config(cls, config_path):
        worker = yaml.load(open(config_path, mode='r'))
        worker.config_path = config_path
        return worker

    def __init__(self, config_path, *args, **kwargs):

        self.config_path = config_path
        self._logger = None
        self.fh = None  # logger file handler
        self.ch = None  # logger console channel

        WorkerConfig.__init__(self, config_path, *args, **kwargs)

        self.init_logger()

        self.context = zmq.Context()

        self.socket = self.context.socket(zmq.REP)

    @property
    def logger(self):
        # if self._logger is None:
        #     self.init_logger()
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value

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

    def get_free_port(self):
        with socketserver.TCPServer(("localhost", 0), None) as s:
            self.port = s.server_address[1]
        return self.port

    def init_logger(self):

        self.logger = logging.getLogger(str(self.id))

        id = self.id

        class AppFilter(logging.Filter):
            def filter(self, record):
                record.app_name = f'Worker {str(id)}'
                return True

        self._logger.addFilter(AppFilter())

        os.makedirs(self.log_dir, exist_ok=True)
        log_filename = os.path.join(self.log_dir, f'worker_{str(self.id)}' + "." + 'log')
        self.fh = logging.FileHandler(log_filename)  # create file handler which logs even debug messages
        self.ch = logging.StreamHandler()  # create console handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(color_formatter)
        # add the handlers to the logger
        self.logger.handlers = [self.fh, self.ch]
        # self.logger.addHandler(self.fh)
        # self.logger.addHandler(self.ch)
        self.update_logging_mode()
        self.logger.info(f'logger started')

        if self.logging_mode == 'DEBUG':
            level = logging.DEBUG
        elif self.logging_mode == 'INFO':
            level = logging.INFO
        elif self.logging_mode == 'WARN':
            level = logging.WARN
        elif self.logging_mode == 'ERROR':
            level = logging.ERROR
        else:
            self.logging_mode = 'INFO'
            level = logging.INFO

        self.logger.setLevel(level)
        self.fh.setLevel(level)
        self.ch.setLevel(level)

        self.logger.info(f'logger level set to {self.logging_mode}')

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
                self.logger.debug(f'receiving message')
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

        self.logger.debug(f'hello from new worker. processing request...')
        method = getattr(self, message.method)
        self.logger.debug(f'method to execute: {method}')

        return getattr(self, message.method)(*message.args, **message.kwargs)

    def check(self, *args, **kwargs):
        return True

    def write(self, filepath=None):

        if self.__on_init:
            self.__update_file = True
            return

        if filepath is None:
            filepath = self.config_path

        with open(filepath, mode='w') as f_obj:
            yaml.dump(self, f_obj)

    def __del__(self):
        try:
            self.logger.info(f'deleted')
            self.socket.close()
        except Exception as e:
            print(f'Error while finalizing worker:\n  {e}')
            return e

    def __getstate__(self):

        state = self.__dict__.copy()

        keys_to_del = ['_logger',
                       'fh',
                       'ch',
                       'context',
                       'socket',
                       '_WorkerConfig__update_file',
                       '_WorkerConfig__on_init',
                       '__on_init',
                       '__update_file',
                       '_Worker__update_file',
                       '_Worker__on_init',
                       'config_path']

        for key in keys_to_del:
            if key in state.keys():
                del state[key]

        return state

    def __setstate__(self, state):

        self.__dict__ = state

        self.__update_file = False
        self.__on_init = True

        self._logger = None
        self.fh = None  # logger file handler
        self.ch = None  # logger console channel
        self.init_logger()
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)

        self.__on_init = False