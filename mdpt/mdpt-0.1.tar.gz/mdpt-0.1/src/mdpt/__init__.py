class mdpt:
    v = 0.1
    d = '2021.05.05'

    def __init__(self, meta: object = {}, encoding='utf-8'):
        if meta:
            re = ''
            for b in meta:
                bb = str(b)
                if len(bb.split(' ')) > 1:
                    bb = '\'' + bb.replace('\'', '\\\'') + '\''
                re += bb + ': ' + meta[b] + '\n'
            self.meta = re
        else:
            self.meta = ''
        self.encoding = encoding

    def g(self, data):
        b = f'mdpt/{mdpt.v}\nlength: {len(data)}\n{self.meta}\n\n-\n'.encode('utf-8')
        if self.encoding != None:
            b += str(data).encode(self.encoding)
        else:
            b += data
        return b

    def u(self, data: bytes):
        if self.encoding != None:
            return data.split(b'\n-\n')[1].decode(self.encoding)
        else:
            return data.split(b'\n-\n')[1]

    def l(self, data: bytes, include_meta=True, minus: int = 0):  # l
        length = int(data.split(b'\n-\n')[0].decode('utf-8').split('length: ')[1].split('\n')[0])

        if include_meta:
            length += len(data.split(b'\n-\n')[0]) + 3

        re = length - minus
        if re < 0:
            re = 0

        return re

    def m(self, data: bytes):  # m
        data = data.split(b'\n-\n')[0].decode('utf-8').split('\n')[2:]

        bb = []
        for b in data:
            if b != '':
                bb.append(b)

        re = {}
        for b in bb:
            re[b.split(': ')[0]] = b.split(': ')[1]

        return re


class sock:
    v = 0.1
    d = '2021.05.05'

    import socket

    class server():
        def __init__(self, ip: str = '', port: int = 9900, listen: int = -1, dev: bool = True):
            """
            dev remove port release delay
            """
            self.s = sock.socket.socket()
            self.s.bind((ip, port))
            if dev:
                self.s.setsockopt(sock.socket.SOL_SOCKET, sock.socket.SO_REUSEADDR, 1)
            self.s.listen(listen)

        def bind(self):
            return self.s

        def close(self):
            self.s.close()

    class client():
        def __init__(self, ip: str = '', port: int = 9900):
            self.s = sock.socket.socket()
            self.s.connect((ip, port))

        def connect(self):
            return self.s

        def close(self):
            self.s.close()
