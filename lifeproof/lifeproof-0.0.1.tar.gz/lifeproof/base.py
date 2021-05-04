from abc import ABC, ABCMeta, abstractmethod


class ProofOfLife(ABC):
    """  Simply abstract class to deal with a proof of life. It is very simply to use:

    with ChildProofOfLife(file):
       something_to_do()

    The ChildProofOfLife is a hierarchical class if ProofOfLife that implements a given proof of life. For example,
    the class FileProofOfLife creates a file which is removed when the program stops for any problem.
    """
    __metaclass__ = ABCMeta

    def __enter__(self) -> 'ProofOfLife':
        """ Returns a closeable object.

        :return: The result of the abstract method enter().
        """
        return self.enter()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ Execute the abstract method exit(). Ignores the parameters. """
        self.exit()

    @abstractmethod
    def enter(self) -> 'ProofOfLife':
        pass

    @abstractmethod
    def exit(self) -> None:
        pass
