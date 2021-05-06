import socket

from enum import Enum


class Format(Enum):
    JSON = 'json'
    TABLE = 'table'
    SIMPLE_TABLE = 'simple-table'


class Client:
    def __init__(self, port=8305, host='127.0.0.1'):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def _write(self, line):
        self.sock.sendall((line+'\r\n').encode())

    def _read(self):
        buf = bytearray()
        while True:
            buf.extend(self.sock.recv(256))
            if b'\r\n\r\n' in buf:
                break

        response = buf.decode().strip().split("\r\n")
        status = response.pop(0)
        if status not in ('ok', 'err'):
            raise InverterError(f"Unexpected status '{status}'")

        if status == 'err':
            raise InverterError(response[0] if len(response) >= 0 else "Unknown error")

        return '\r\n'.join(response)

    def protocol(self, v):
        self._write(f'v {v}')
        return self._read()

    def format(self, format):
        self._write(f'format {format}')
        return self._read()

    def exec(self, command, arguments=()):
        buf = f'exec {command}'
        for arg in arguments:
            buf += f' {arg}'
        self._write(buf)
        return self._read()


class InverterError(RuntimeError): pass