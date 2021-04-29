import uuid
import json
import zmq
import zmq.auth
from zmq.auth.thread import ThreadAuthenticator
import logging

from .worker import Worker
from .message import Message
from service_tools import start_worker

from configparser import ConfigParser
import os
from os import path
import socket
import shutil

import subprocess


class ServerConfig(object):

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
        config = ConfigParser()
        if config_path is None:
            raise ValueError(f'config_path is None')

        config.add_section('main')

        config.set('main', 'id', str(kwargs.get('id', uuid.uuid4())))
        config.set('main', 'name', kwargs.get('name', None))
        config.set('main', 'ip', kwargs.get('ip', None))
        config.set('main', 'port', str(kwargs.get('port', -1)))
        config.set('main', 'secure', str(kwargs.get('secure', True)))
        config.set('main', 'backend_port', str(kwargs.get('backend_port', None)))
        config.set('main', 'public_keys_dir', kwargs.get('public_keys_dir', None))
        config.set('main', 'secret_keys_dir', kwargs.get('secret_keys_dir', None))

        config.add_section('workers')
        config.set('workers', 'num_workers', str(kwargs.get('num_workers', 1)))
        config.set('workers', 'auto_start', str(kwargs.get('auto_start', True)))
        config.set('workers', 'worker_config_paths', json.dumps(kwargs.get('worker_config_paths', None)))
        config.set('workers', 'worker_script_path', str(kwargs.get('worker_script_path', None)))

        config.add_section('logging')
        config.set('logging', 'log_dir', kwargs.get('log_dir', None))
        config.set('logging', 'logging_mode', kwargs.get('logging_mode', 'DEBUG'))

        if not path.isfile(config_path):
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

        self._secure = None
        self._public_keys_dir = None
        self._secret_keys_dir = None

        self._ip = None
        try:
            self._ip = get_ip_address()
        except Exception as e:
            print(e)

        self._port = None
        self._backend_port = None

        # workers
        self._num_workers = None
        self._auto_start = None
        self._worker_script_path = None

        # logging
        self._log_dir = None
        self._logging_mode = None

        if not path.isfile(self.config_path):
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
    def secure(self):
        if self._secure is None:
            self.read_config()
        return self._secure

    @secure.setter
    def secure(self, value):

        self.config.set('main', 'secure', value)
        self.write_config()
        self._secure = value

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
    def backend_port(self):
        if self._backend_port is None:
            self.read_config()
        return self._backend_port

    @backend_port.setter
    def backend_port(self, value):

        self.config.set('main', 'backend_port', str(value))
        self.write_config()
        self._backend_port = value

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
    def num_workers(self):
        if self._num_workers is None:
            self.read_config()
        return self._num_workers

    @num_workers.setter
    def num_workers(self, value):

        self.config.set('workers', 'num_workers', str(value))
        self.write_config()
        self._num_workers = value

    @property
    def worker_config_paths(self):
        if self._worker_config_paths is None:
            self.read_config()
        return self._worker_config_paths

    @worker_config_paths.setter
    def worker_config_paths(self, value):

        self.config.set('workers', 'worker_config_paths', json.dumps(value))
        self.write_config()
        self._worker_config_paths = value

    @property
    def worker_script_path(self):
        if self._worker_script_path is None:
            self.read_config()
        return self._worker_script_path

    @worker_script_path.setter
    def worker_script_path(self, value):

        self.config.set('workers', 'worker_script_path', str(value))
        self.write_config()
        self._worker_script_path = value

    @property
    def auto_start(self):
        if self._auto_start is None:
            self.read_config()
        return self._auto_start

    @auto_start.setter
    def auto_start(self, value):

        self.config.set('workers', 'auto_start', str(value))
        self.write_config()
        self._auto_start = value

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

        if not path.isfile(self.config_path):
            raise FileExistsError(f'{self.config_path} does not exist')
        self.config.read(self.config_path)

        try:
            self._secure = self.config.getboolean('main', 'secure')
        except Exception as e:
            raise Exception(f'Error: secure in {self.config_path} does not exist')

        try:
            self._public_keys_dir = self.config.get('main', 'public_keys_dir')
        except Exception as e:
            raise Exception(f'Error: public_keys_dir in {self.config_path} does not exist')

        try:
            self._secret_keys_dir = self.config.get('main', 'secret_keys_dir')
        except Exception as e:
            raise Exception(f'Error: secret_keys_dir in {self.config_path} does not exist')

        try:
            self._ip = self.config.get('main', 'ip')
        except Exception as e:
            raise Exception(f'Error: ip in {self.config_path} does not exist')

        try:
            self._port = self.config.getint('main', 'port')
        except Exception as e:
            raise Exception(f'Error: port in {self.config_path} does not exist')

        try:
            self._backend_port = self.config.getint('main', 'backend_port')
        except Exception as e:
            print('port in {self.config_path} does not exist')

        try:
            self._name = self.config.get('main', 'name')
        except Exception as e:
            print('name in {self.config_path} does not exist')

        try:
            self._id = uuid.UUID(self.config.get('main', 'id'))
        except Exception as e:
            raise Exception(f'Error: id in {self.config_path} does not exist')

        ##############################################
        # workers
        ##############################################

        try:
            self._num_workers = self.config.getint('workers', 'num_workers')
        except Exception as e:
            print('num_workers in {self.config_path} does not exist')
            self._num_workers = 1

        try:
            self._auto_start = self.config.getboolean('workers', 'auto_start')
        except Exception as e:
            print('auto_start in {self.config_path} does not exist')
            self._auto_start = True

        try:
            worker_config_paths = json.loads(self.config.get('workers', 'worker_config_paths'))
            if not isinstance(worker_config_paths, list):
                worker_config_paths = [worker_config_paths]
            self.worker_config_paths = worker_config_paths
        except Exception as e:
            print('worker_config_paths in {self.config_path} does not exist')
            self._worker_config_paths = True

        try:
            self._worker_script_path = self.config.get('workers', 'worker_script_path')
        except Exception as e:
            print('worker_script_path in {self.config_path} does not exist')
            self._worker_script_path = None

        ##############################################
        # logging
        ##############################################

        try:
            self._log_dir = self.config.get('logging', 'log_dir')
        except Exception as e:
            print('log_dir in {self.config_path} does not exist')
            self._log_dir = None

        try:
            self._logging_mode = self.config.get('logging', 'logging_mode')
        except Exception as e:
            print('logging_mode in {self.config_path} does not exist')
            self._logging_mode = 'DEBUG'

    def write_config(self):

        try:
            with open(self.config_path, 'w') as f:
                self.config.write(f)
        except Exception as e:
            print(f'error writing config: {e}')


class Server(ServerConfig):

    def __init__(self, config_path, *args, **kwargs):

        ServerConfig.__init__(self, config_path, *args, **kwargs)

        self.fh = None  # logger file handler
        self.ch = None  # logger console channel
        self.logger = None
        self.init_logger()
        self.logging_mode = 'DEBUG'

        ctx = zmq.Context.instance()

        # Start an authenticator for this context.
        if self.secure:
            self.auth = ThreadAuthenticator(ctx)
            self.auth.start()
            # auth.allow('127.0.0.1')
            # Tell authenticator to use the certificate in a directory
            self.auth.configure_curve(domain='*', location=self.public_keys_dir)
            server_secret_file = os.path.join(self.secret_keys_dir, "server.key_secret")
            server_public, server_secret = zmq.auth.load_certificate(server_secret_file)

        self.server = ctx.socket(zmq.REP)

        ctx = zmq.Context.instance()

        self.frontend = ctx.socket(zmq.ROUTER)
        if self.secure:
            self.frontend.curve_secretkey = server_secret
            self.frontend.curve_publickey = server_public
            self.frontend.curve_server = True  # must come before bind

        if (self.port is None) or (self.port == 0):
            self.port = self.server.bind_to_random_port('tcp://*', min_port=6001, max_port=6150, max_tries=100)
        else:
            self.frontend.bind(f'tcp://*:{self.port}')

        self.workers = []

        context = zmq.Context()
        self.backend = context.socket(zmq.DEALER)
        self.backend_port = self.backend.bind_to_random_port('tcp://*', min_port=9001, max_port=9050, max_tries=100)
        self.logger.info(f'creat backend on port {self.backend_port}')

        self.logger.info(f'starting {self.num_workers} workers...')

        if self.auto_start:
            self.logger.info(f'Auto start active')
            self.start_workers()
            self.logger.info(f'all workers started')

    def init_logger(self):

        self.logger = logging.getLogger(str(self.id))

        log_filename = os.path.join(self.log_dir, f'server_{str(self.id)}' + "." + 'log')
        self.fh = logging.FileHandler(log_filename)  # create file handler which logs even debug messages
        self.ch = logging.StreamHandler()  # create console handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

        self.logger.info(f'logger started')

    @property
    def logging_mode(self):
        return self._logging_mode

    @logging_mode.setter
    def logging_mode(self, value):

        self.config.set('logging', 'logging_mode', value)
        self.write_config()
        self._logging_mode = value

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

        self.logger.info(f'logger level set to {value}')

    def add_worker(self, config_path, python_path):
        # new_worker = Worker(config_path)
        # self.workers.append(new_worker)
        # new_worker.start()

        if self.worker_script_path is None:
            script_path = os.path.abspath(start_worker.__file__)
        else:
            script_path = self.worker_script_path

        if not python_path:
            python_path = 'python'

        if os.path.isfile(script_path):
            p = subprocess.Popen(f'{python_path} {script_path} --config_file={config_path}', shell=True)
            self.logger.info(f'worker started: {p.poll()}')
            self.workers.append(p)
        else:
            self.logger.error(f'Error starting worker: {script_path} not found')
            return

        self.logger.info(f'worker started: {p.poll()}')
        self.workers.append(p)

    def start_workers(self):
        for i in range(self.num_workers):

            if self.worker_config_paths.__len__() == 0:
                self.logger.error(f'error while starting workers. No worker config found')
                return

            if (self.worker_config_paths.__len__() - 1) < i:
                worker_config_path = self.worker_config_paths[0]

                dirname = os.path.dirname(worker_config_path)
                filename = os.path.basename(worker_config_path)
                base_filename = os.path.splitext(filename)[0]
                extension = os.path.splitext(filename)[1]

                new_worker_config_path = os.path.join(dirname, base_filename + f'__worker{i}_copy' + extension)

                # copy the config and overwrite the id
                shutil.copy2(worker_config_path, new_worker_config_path)
                worker_config = ConfigParser()
                worker_config.read(new_worker_config_path)
                worker_config.set('main', 'id', str(uuid.uuid4()))
                try:
                    with open(new_worker_config_path, 'w') as f:
                        worker_config.write(f)
                except Exception as e:
                    print(f'error writing worker_config: {e}')
                worker_config_path = new_worker_config_path

            elif (self.worker_config_paths.__len__() - 1) >= i:
                # overwrite port:
                worker_config_path = self.worker_config_paths[i]
            else:
                self.logger.error(f'error while starting workers. No worker config found')
                continue

            worker_config = ConfigParser()
            worker_config.read(worker_config_path)

            try:
                python_path = worker_config.get('main', 'python_path', fallback=None)
            except Exception as e:
                print('python_path in {self.config_path} does not exist. Assume system python')
                python_path = 'python'

            worker_config.set('main', 'ip', str(self.ip))
            worker_config.set('main', 'port', str(self.backend_port))
            try:
                with open(worker_config_path, 'w') as f:
                    worker_config.write(f)
            except Exception as e:
                print(f'error writing worker_config: {e}')

            self.add_worker(worker_config_path, python_path)

    def start(self):

        self.logger.info(f'starting server {self.id} on port: {self.port};\n backend port: {self.backend_port}')
        zmq.proxy(self.frontend, self.backend)

    def __del__(self):
        self.logger.info(f'stopping server')
        self.backend_port = None
        try:
            for worker in self.workers:
                worker.terminate()
        except Exception as e:
            pass


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
