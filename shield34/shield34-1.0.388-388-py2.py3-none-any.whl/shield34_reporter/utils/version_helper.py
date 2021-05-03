import pkg_resources


class VersionHelper(object):
    def get_version(self):
        return pkg_resources.get_distribution('shield34').version