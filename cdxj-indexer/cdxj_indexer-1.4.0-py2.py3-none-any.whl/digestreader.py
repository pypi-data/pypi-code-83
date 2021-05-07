import hashlib

from warcio.archiveiterator import UnseekableYetTellable


class DigestReader(UnseekableYetTellable):
    def __init__(self, fh):
        super().__init__(fh)
        self.hash = hashlib.sha256()
        self.digest_size = 0

    def read(self, size=-1):
        res = super().read(size)
        self.hash.update(res)
        self.digest_size += len(res)
        return res

    def get_digest(self):
        digest = self.hash.hexdigest()
        self.hash = hashlib.sha256()
        self.digest_size = 0
        return digest

    def get_digest_length(self):
        return self.digest_size






