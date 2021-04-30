from os.path import isfile, join
from hashlib import md5
from PIL import Image
from os import stat, unlink, walk
from os.path import join
from random import random
from heapq import heappop, heappush


class Thumbnail:

    def __init__(self, source, width, height, mapper=None):
        self.source = source
        self.width = width
        self.height = height
        self.mapper = mapper

    _filename = None

    @property
    def filename(self):
        if self._filename is None:
            hash = md5(self.source.encode('utf-8')).hexdigest()
            self._filename = '{}_{}x{}.jpg'.format(hash, self.width, self.height)
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    @property
    def absfilename(self):
        if self.mapper:
            return join(self.mapper.cache_dir, self.filename)
        else:
            return self.filename

    def make(self):
        if self.mapper:
            self.mapper.gc()
        img = Image.open(self.source)
        img.thumbnail((self.width, self.height))
        img.save(self.absfilename, 'JPEG', quality=80)


class ThumbnailMapper:

    def __init__(self, cache_dir, maxfiles, threshlod):
        self.cache_dir = cache_dir
        self.maxfiles = maxfiles
        self.threshold = threshlod

    def create_thumbnail(self, source, width, height):
        """
        Thumbnail factory
        """
        return Thumbnail(source, width, height, mapper=self)

    def has(self, name):
        return isfile(join(self.cache_dir, name))

    def gc(self):
        if random() < self.threshold:
            self.prune()

    def prune(self):
        """
        Efface les fichiers les plus anciens du cache.
        Conserve les 3/4 de maxfiles.
        """
        _, _, files = next(walk(self.cache_dir))
        nb_files = len(files)
        if nb_files < self.maxfiles:
            return
        heap = list()
        for item in files:
            st = stat(join(self.cache_dir, item))
            heappush(heap, (st.st_mtime, item))
        for x in range(nb_files - self.maxfiles + self.maxfiles // 4):
            item = heappop(heap)[1]
            unlink(join(self.cache_dir, item))
