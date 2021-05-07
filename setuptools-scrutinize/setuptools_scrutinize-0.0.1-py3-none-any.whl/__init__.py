""" Base for Scrutinizers """
import logging

class ScrutinizerError(Exception):
    """ The root of all Scrutinizer evil. """
    pass


class ScrutinizerConfigError(ScrutinizerError):
    """ Error in config. """
    pass


class ScrutinizerRunError(ScrutinizerError):
    """ Error during running. """
    pass


class Scrutinizer:
    """ Scrutinizer """

    # Subclasses must define:
    #   initialize_options()
    #     provide default values for all options; may be customized by
    #     setup script, by options from config file(s), or by command-line
    #     options
    #   finalize_options()
    #     decide on the final values for all options; this is called
    #     after all possible intervention from the outside world
    #     (command-line, option file, etc.) has been processed
    #   run()
    #     run the command: do whatever it is we're here to do,
    #     controlled by the command's various option values

    name = 'Base'


    def __init__(self, command):
    # def __init__(self):
        """Create and initialize a new Command object.  Most importantly,
        invokes the 'initialize_options()' method, which is the real
        initializer and depends on the actual command being
        instantiated.
        """
        # logging.error("301")
        # late import because of mutual dependence between these classes
        # from distutils.dist import Distribution
        from setuptools_scrutinize.setuptools_command import Scrutinize

        # logging.error("302")
        if not isinstance(command, Scrutinize):
            raise TypeError("command must be a Scrutinize instance")
        # logging.error("303")
        # if not isinstance(dist, Distribution):
        #     raise TypeError("dist must be a Distribution instance")
        # if self.__class__ is Command:
        #     raise RuntimeError("Command is an abstract class")
        if self.__class__ is Scrutinizer:
            raise RuntimeError("Scrutinizer is an abstract class")

        # self.distribution = command.distrib
        self.command = command
        self.initialize_options()

        self._dry_run = None

        # self.verbose = dist.verbose

        # Some commands define a 'self.force' option to ignore file
        # timestamps, but methods defined *here* assume that
        # 'self.force' exists for all commands.  So define it here
        # just to be safe.
        self.force = None

        # The 'help' flag is just used for command-line parsing, so
        # none of that complicated bureaucracy is needed.
        self.help = 0

        # 'finalized' records whether or not 'finalize_options()' has been
        # called.  'finalize_options()' itself should not pay attention to
        # this flag: it is the business of 'ensure_finalized()', which
        # always calls 'finalize_options()', to respect/update it.
        self.finalized = 0

        self.config = None


    def initialize_options(self):
        """Set default values for all the options that this command
        supports.  Note that these defaults may be overridden by other
        commands, by the setup script, by config files, or by the
        command-line.  Thus, this is not the place to code dependencies
        between options; generally, 'initialize_options()' implementations
        are just a bunch of "self.foo = None" assignments.

        This method must be implemented by all command classes.
        """
        raise RuntimeError("abstract method -- subclass %s must override"
                           % self.__class__)


    def finalize_options(self):
        """Set final values for all the options that this command supports.
        This is always called as late as possible, ie.  after any option
        assignments from the command-line or from other commands have been
        done.  Thus, this is the place to code option dependencies: if
        'foo' depends on 'bar', then it is safe to set 'foo' from 'bar' as
        long as 'foo' still has the same value it was assigned in
        'initialize_options()'.

        This method must be implemented by all command classes.
        """
        raise RuntimeError("abstract method -- subclass %s must override"
                           % self.__class__)


    def run(self):
        """A command's raison d'etre: carry out the action it exists to
        perform, controlled by the options initialized in
        'initialize_options()', customized by other commands, the setup
        script, the command-line, and config files, and finalized in
        'finalize_options()'.  All terminal output and filesystem
        interaction should be done by 'run()'.

        This method must be implemented by all command classes.
        """
        raise RuntimeError("abstract method -- subclass %s must override"
                           % self.__class__)

