import zmq
import zmq.auth
import uuid


class Client(object):

    def __init__(self, *args, **kwargs):

        self.name = kwargs.get('name', None)
        self.id = kwargs.get('id', uuid.uuid4())

        self.ip = kwargs.get('ip', 'localhost')
        self.port = kwargs.get('port', None)

        self.secret_key_path = kwargs.get('secret_key_path', None)
        self.server_public_key_path = kwargs.get('server_public_key_path', None)

        self.ctx = zmq.Context.instance()
        self.socket = self.ctx.socket(zmq.REQ)

    def connect(self):

        client_public, client_secret = zmq.auth.load_certificate(self.secret_key_path)
        server_public, _ = zmq.auth.load_certificate(self.server_public_key_path)

        self.socket.curve_secretkey = client_secret
        self.socket.curve_publickey = client_public
        self.socket.curve_serverkey = server_public

        self.socket.connect(f'tcp://{self.ip}:{self.port}')

    def send_message(self, message):

        self.socket.send_pyobj(message)
        return self.socket.recv_pyobj()
