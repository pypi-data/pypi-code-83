import json

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5


class Transaction:
    def __init__(self, sender, receiver, content, signature=None):

        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.signature = signature

    def hash(self):

        tx = json.dumps({
            'sender': self.sender,
            'receiver': self.receiver,
            'content': self.content
        })
        return SHA256.new(str.encode(tx))

    def sign(self, private_key):

        signature = PKCS1_v1_5.new(private_key).sign(msg_hash=self.hash())

        if not signature:
            print('Signing transaction failed')
            return False

        self.signature = signature
        return True

    @staticmethod
    def calculate_hash(tx):

        tx_str = json.dumps(tx)

        return SHA256.new(str.encode(tx_str))

    @staticmethod
    def validate(hash, signature, public_key):

        valid = PKCS1_v1_5.new(public_key).verify(hash, signature)

        if not valid:
            print('Verifying failed')
            return False

        return True
