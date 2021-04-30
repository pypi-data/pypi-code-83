from flask import url_for, safe_join
from os import walk
from dataclasses import dataclass
from hashlib import md5


@dataclass(init=False)
class CKFResourceType():
    name: str
    url: str
    allowedExtensions: str
    maxSize: int
    hasChildren: bool
    hash: str
    deniedExtensions: str
    acl: int
    backend = 'default'

    def __init__(self, endpoint, directory, name, allowedExtensions, maxSize, acl=1023, deniedExtensions=''):
        self.endpoint = endpoint
        self.directory = directory
        self.name = name
        self.allowedExtensions = allowedExtensions
        self.maxSize = maxSize
        self.acl = acl
        self.deniedExtensions = deniedExtensions
        _, dirs, _ = next(walk(self.directory))
        self.hasChildren = bool(dirs)

    @property
    def url(self):
        """
        Deffered call to url_for
        """
        return url_for(self.endpoint, filename='')

    _hash = None

    @property
    def hash(self):
        if not self._hash:
            h = md5()
            h.update(self.name.encode('utf-8'))
            h.update(self.backend.encode('utf-8'))
            h.update(self.directory.encode('utf-8'))
            self._hash = h.hexdigest()
        return self._hash

    def abs_path(self, rel):
        return safe_join(self.directory, rel.strip('/'))

    def folder(self, dname):
        return dict(path=dname, url=url_for(self.endpoint, filename=dname), acl=self.acl)
