#!/usr/bin/env python

"""Tests for `crypto_fernet` package."""

import os
import unittest

from crypto_fernet.crypto_fernet import encrypt, decrypt


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.secret = os.urandom(128)
        self.test_phrase = b'The ultimate answer is 42!'

    def test_encryption_decryption(self):
        cipher_text = encrypt(self.test_phrase, self.secret)
        self.assertNotEqual(self.test_phrase, cipher_text)
        plain_text = decrypt(cipher_text, self.secret)
        self.assertEqual(self.test_phrase, plain_text)


if __name__ == '__main__':
    unittest.main()
