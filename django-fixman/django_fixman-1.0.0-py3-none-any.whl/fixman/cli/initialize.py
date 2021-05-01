# Imports

# Exports

# Functions


def subcommands(subparsers):
    commands = SubCommands(subparsers)
    commands.dumpdata()
    commands.init()
    commands.inspect()
    commands.list()
    commands.loaddata()
    commands.scan()

# Classes


class SubCommands(object):
    """A utility class which keeps the ``cli.py`` module clean."""

    def __init__(self, subparsers):
        self.subparsers = subparsers

    def dumpdata(self):
        """Create the dumpdata sub-command."""
        sub = self.subparsers.add_parser(
            "dumpdata",
            aliases=["dd", "dump"],
            help="Export Django fixtures."
        )

        self._add_fixture_options(sub)
        self._add_common_options(sub)

    def init(self):
        """Create the init sub-command."""
        sub = self.subparsers.add_parser(
            "init",
            help="Initialize fixture management."
        )

        sub.add_argument(
            "-b=",
            "--base=",
            default="source",
            dest="base_directory",
            help="The base directory within the project where fixture files may be located."
        )

        sub.add_argument(
            "-F",
            "--force-it",
            action="store_true",
            dest="force_enabled",
            help="Force initialization (and scanning with -S) even if an existing configuration exists. This will "
                 "overwrite your current config.ini file."
        )

        sub.add_argument(
            "-S",
            "--scan",
            action="store_true",
            dest="scan_enabled",
            help="Scan the current directory (or project root) to find fixture files to be added to the config."
        )

        self._add_common_options(sub)

    def inspect(self):
        """Create the inspect sub-command."""
        sub = self.subparsers.add_parser(
            "inspect",
            aliases=["ins"],
            help="Display Django fixtures."
        )

        self._add_fixture_options(sub)
        self._add_common_options(sub)

    def list(self):
        """Create the list sub-command."""
        # Arguments do NOT use _add_common_options() because this sub-command doesn't utilize the common options for
        # dump, load, etc. So common options such as -D and -p have to be added here.
        sub = self.subparsers.add_parser(
            "list",
            aliases=["ls"],
            help="List the configured fixtures."
        )

        self._add_fixture_options(sub)
        self._add_common_options(sub)

    def loaddata(self):
        """Create the loaddata sub-command."""
        sub = self.subparsers.add_parser(
            "loaddata",
            aliases=["ld", "load"],
            help="Load Django fixtures."
        )

        sub.add_argument(
            "-S",
            "--script",
            action="store_true",
            dest="to_script",
            help="Export to a bash script."
        )

        self._add_fixture_options(sub)
        self._add_common_options(sub)

    def scan(self):
        """Create the scan sub-command."""
        # Arguments do NOT use _add_common_options() because this sub-command doesn't utilize the common options for
        # dump, load, etc. So common options such as -D and -p have to be added here.
        sub = self.subparsers.add_parser(
            "scan",
            help="Scan for fixture files in project source."
        )

        sub.add_argument(
            "-P=",
            "--path=",
            default="deploy/fixtures/config.ini",
            dest="path",
            help="The path to the fixtures INI file. Default: deploy/fixtures/config.ini"
        )

        sub.add_argument(
            "-S=",
            "--source=",
            default="source",
            dest="base_directory",
            help="The base directory in project root from which the scan will take place."
        )

        self._add_common_options(sub)

    def _add_fixture_options(self, sub):
        """Add the common options for the fixture dump/inspect/load commands."""
        sub.add_argument(
            "-A=",
            "--app-name=",
            action="append",
            dest="app_names",
            help="Only work with this app. May be used multiple times."
        )

        sub.add_argument(
            "-G=",
            "--group-name=",
            action="append",
            dest="group_names",
            help="Only work with this group. May be used multiple times."
        )

        sub.add_argument(
            "-M=",
            "--model-name=",
            action="append",
            dest="model_names",
            help="Only work with this model. May be used multiple times."
        )

        sub.add_argument(
            "-P=",
            "--path=",
            default="deploy/fixtures/config.ini",
            dest="path",
            help="The path to the fixtures INI file. Default: deploy/fixtures/config.ini"
        )

        sub.add_argument(
            "-s=",
            "--settings=",
            dest="settings",
            help="The dotted path to the Django settings file."
        )

    # noinspection PyMethodMayBeStatic
    def _add_common_options(self, sub):
        """Add the common switches to a given sub-command instance.

        :param sub: The sub-command instance.

        """

        sub.add_argument(
            "-D",
            "--debug",
            action="store_true",
            dest="debug_enabled",
            help="Enable debug output."
        )

        sub.add_argument(
            "-p",
            "--preview",
            action="store_true",
            dest="preview_enabled",
            help="Preview the commands."
        )

        sub.add_argument(
            "-r=",
            "--project-root=",
            dest="project_root",
            help="The path to the project."
        )
