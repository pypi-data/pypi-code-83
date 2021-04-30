# -*- coding: utf-8 -*-
# @author: leesoar

"""IMAP client"""

import base64
import imaplib
from email.parser import Parser
from urllib.parse import unquote

from postcard import setting


__all__ = ["Imap"]


class Imap(object):
    def __init__(self):
        self.user = None
        self.pwd = None
        self._client = None
        self.imap_addr = None
        self.imap_port = None
        self.parser = Parser()

    def login(self, user, pwd, imap_addr=None, imap_port=None, ssl=False):
        """Login current mailbox"""
        self.user = user
        self.pwd = pwd
        self.imap_addr = imap_addr or self.imap_addr
        self.imap_port = imap_port or self.imap_port

        if not self.imap_addr:
            self.imap_addr = self._set_imap_addr_auto(user)

        if not self.imap_port:
            self.imap_port = imaplib.IMAP4_SSL_PORT if ssl else imaplib.IMAP4_PORT

        if ssl:
            self._client = imaplib.IMAP4_SSL(self.imap_addr, self.imap_port)
        else:
            self._client = imaplib.IMAP4(self.imap_addr, self.imap_port)
        self._client.login(self.user, self.pwd)
        return self._client

    def close(self):
        self._client.close()
        self._client.logout()

    @staticmethod
    def get_addr_map():
        return setting.IMAP_ADDR

    def _set_imap_addr_auto(self, user):
        domain = user.rsplit(".", maxsplit=1)[0].split("@")[-1]
        imap_addr = self.get_addr_map().get(domain)
        if imap_addr and not self.imap_addr:
            self.imap_addr = imap_addr
        return self.imap_addr

    def get_client(self):
        """Get Imap client"""
        return self._client

    def how_many(self) -> int:
        """Return mailbox's email count"""
        _, msg_nums = self.select()
        return int(msg_nums[0] or 0)

    def _retr_num(self, msg_nums: list) -> list:
        return msg_nums[0].split()

    def select(self, mailbox="INBOX", readonly=True):
        return self._client.select(mailbox, readonly)

    def search(self, word, type_="Text", mailbox="INBOX", readonly=True):
        self.select(mailbox, readonly=readonly)
        _, msg_nums = self._client.search(None, type_, word)
        return self._retr_num(msg_nums)

    def unseen(self, readonly=True):
        self.select(readonly=readonly)
        return self.search(None, "Unseen")

    def __check_and_decode(self, mail_info: dict) -> dict:
        """Check encoding and decode mail's content"""
        content_encoding = mail_info.get("content-transfer-encoding", "").lower()

        try:
            if content_encoding == "base64":
                mail_info["content"] = base64.b64decode(mail_info["content"]).decode(errors="ignore")
            elif content_encoding == "quoted-printable":
                pass
        except Exception:
            pass

        return mail_info

    def retrieve(self, index_: int = None, mailbox="INBOX", readonly=True) -> dict:
        """Retrieve mail at index"""
        self.select(mailbox, readonly)
        index_ = index_ or self.how_many()
        lines = self._client.fetch(str(index_).encode(), "RFC822")[1][0][1]
        lines = unquote(lines.decode())
        try:
            lines, content = lines.split("\r\n\r\n", maxsplit=1)
        except ValueError:
            content = ""
        finally:
            lines = lines.encode()

        line_array = lines.split(b"\r\n")

        def __convert(x: bytes):
            k, v = x.strip().decode(errors="ignore").split(":", 1)
            if "</p>" in v:
                k = "content"

            if " " in k:
                return
            return [k.lower().strip(), v.lower().strip().lstrip("[").rstrip("]")]

        mail_info = dict(filter(lambda x: x, map(__convert, filter(lambda x: b":" in x and b"receive" not in x.lower(), line_array))))

        if "content" not in mail_info:
            mail_info.update(dict(content=content))

        return self.__check_and_decode(mail_info)

    def delete(self, index_: int):
        """Delete mail at index"""
        self.select(readonly=False)
        self._client.store(str(index_).encode(), '+FLAGS', '\\Deleted')
        self._client.expunge()
        self.select(readonly=True)

    def process(self, user=None, pwd=None, imap_addr=None, imap_port=None, ssl=False):
        """process decorator

        Args:
            user: mailbox account
            pwd: mailbox password
            imap_addr: current mailbox's Imap addr
            imap_port: current mailbox's Imap port
            ssl: use SSL, default False
        Usage:
            imap = Imap()

            @imap.process(user="xxx", pwd="xxx")
            def get_content():
                content = imap.retrieve()["content"]
                log.debug(content)
        """
        user = user or self.user
        pwd = pwd or self.pwd
        imap_addr = imap_addr or self.imap_addr
        imap_port = imap_port or self.imap_port

        assert None not in [user, pwd], \
            "You should give your info."

        def decorator(func):
            def wrapper(*args, **kwargs):
                self.login(user, pwd, imap_addr, imap_port, ssl)
                ret = func(*args, **kwargs)
                self.close()
                return ret
            return wrapper
        return decorator
