from os import remove

from lifeproof.base import ProofOfLife


class FileProofOfLife(ProofOfLife):
    """
    Simply class to deal with a proof of life. It is very simply to use:

    with LifeProofOfLife(file):
       something_to_do()

    The ProofOfLife creates a temporal file, if something_to_do fails, then the temporal file is removed.
    """
    @property
    def filename(self) -> str:
        return self.__file

    def __init__(self, fname: str = '/tmp/health'):
        """
        Constructor.
        :param fname: The file name to create. By default '/tmp/health'.
        """
        self.__file = fname
        open(fname, 'wt').close()

    def enter(self) -> ProofOfLife:
        """ Returns a closeable object.
        :return: This object.
        """
        return self

    def exit(self) -> None:
        """ Remove the created file. """
        remove(self.__file)
