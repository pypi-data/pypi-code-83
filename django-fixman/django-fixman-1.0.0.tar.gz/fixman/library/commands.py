# Imports

import logging
import os
from subprocess import getstatusoutput
from commonkit.shell import EXIT
from ..constants import LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)

# Classes


class DumpData(object):
    """A command for dumping fixture data."""

    def __init__(self, app, database=None, export=None, natural_foreign=False, natural_primary=False, path=None,
                 settings=None):
        """Initialize the command.

        :param app: The name of the app to which the fixture file belongs.
        :type app: str

        :param database: The database name into which the fixtures are installed.
        :type database: str

        :param export: ???

        :param natural_foreign: Indicates whether natural foreign keys are used.
        :type natural_foreign: bool

        :param natural_primary: Indicates whether natural primary keys are used.
        :type natural_primary: bool

        :param path: The full path to the fixture file, including the file name.
        :type path: str

        :param settings: The settings to use when loading or dumping data.
        :type settings: str

        """
        self.app = app
        self.database = database
        self.export = export or app
        self.natural_foreign = natural_foreign
        self.natural_primary = natural_primary
        self.path = path or os.path.join("../fixtures", app, "initial.json")
        self.settings = settings
        self._output = None
        self._status = None

    def get_command(self):
        """Get the command.

        :rtype: str

        """
        a = list()

        a.append("(cd source && ./manage.py dumpdata")

        if self.database is not None:
            a.append("--database=%s" % self.database)

        a.append("--indent=4")

        if self.natural_foreign:
            a.append("--natural-foreign")

        if self.natural_primary:
            a.append("--natural-primary")

        if self.settings is not None:
            a.append("--settings=%s" % self.settings)

        # if self.copy_to is not None:
        #     a.append("%s > %s && cp %s %s" % (
        #         self.export,
        #         self.path,
        #         self.path,
        #         self.copy_to
        #     ))
        # else:
        a.append("%s > %s)" % (self.export, self.path))

        return " ".join(a)

    def get_output(self):
        """Get the output of the command.

        :rtype: str

        """
        return self._output

    def preview(self):
        """Preview the command statement.

        :rtype: str

        """
        return self.get_command()

    def run(self):
        """Run the command.

        :rtype: bool

        """
        command = self.get_command()

        self._status, self._output = getstatusoutput(command)

        if self._status > EXIT.OK:
            return False

        return True


class LoadData(object):
    """A command for loading fixture data."""

    def __init__(self, app, database=None, path=None, settings=None):
        """Initialize the command.

        :param app: The name of the app to which the fixture file belongs.
        :type app: str

        :param database: The database name into which the fixtures are installed.
        :type database: str

        :param path: The full path to the fixture file, including the file name.
        :type path: str

        :param settings: The settings to use when loading or dumping data.
        :type settings: str

        """
        self.app = app
        self.database = database
        self.path = path or os.path.join("../fixtures", app, "initial.json")
        self.settings = settings
        self._output = None
        self._status = None

    def get_command(self):
        """Get the command.

        :rtype: str

        """
        a = list()

        a.append("(cd source && ./manage.py loaddata")

        if self.database is not None:
            a.append("--database=%s" % self.database)

        if self.settings is not None:
            a.append("--settings=%s" % self.settings)

        a.append("%s)" % self.path)

        return " ".join(a)

    def get_output(self):
        """Get the output of the command.

        :rtype: str

        """
        return self._output

    def preview(self):
        """Preview the command.

        :rtype: str

        """
        return self.get_command()

    def run(self):
        """Run the command.

        :rtype: str

        """
        command = self.get_command()

        self._status, self._output = getstatusoutput(command)

        if self._status > EXIT.OK:
            return False

        return True

'''
class Fixture(object):

    def __init__(self, model, operation, **kwargs):
        self.app_label, self.model_name = model.split(".")
        self.database = kwargs.pop("database", None)
        self.group = kwargs.pop("group", "defaults")
        self.is_readonly = kwargs.pop("readonly", False)
        self.model = model
        self.operation = operation
        self.output = None
        self.settings = kwargs.pop("settings", None)
        self.status = None
        self._preview = kwargs.pop("preview", False)

        default_path = os.path.join(self.app_label, "fixtures", self.model_name.lower())
        self.path = kwargs.pop("path", default_path)

    def __repr__(self):
        return "<%s %s.%s>" % (self.__class__.__name__, self.app_label, self.model_name)

    def get_command(self):
        if self.operation == "dumpdata":
            return self._get_dumpdata_command()
        elif self.operation == "loaddata":
            return self._get_loaddata_command()
        else:
            raise ValueError("Invalid fixture operation: %s" % self.operation)

    def preview(self):
        return self.get_command()

    def run(self):
        command = self.get_command()
        status, output = getstatusoutput(command)

        self.output = output
        self.status = status

        if status > EXIT.OK:
            return False

        return True

    def _get_dumpdata_command(self):
        a = list()

        a.append("(cd source && ./manage.py dumpdata")

        if self.settings is not None:
            a.append("--settings=%s" % self.settings)

        if self.database is not None:
            a.append("--database=%s" % self.database)

        # args.full_preview_enabled = True
        if self._preview:
            a.append("--indent=4 %s)" % self.model)
        else:
            a.append("--indent=4 %s > %s)" % (self.model, self.path))

        return " ".join(a)

    def _get_loaddata_command(self):
        a = list()
        a.append("(cd source && ./manage.py loaddata")

        if self.settings is not None:
            a.append("--settings=%s" % self.settings)

        if self.database is not None:
            a.append("--database=%s" % self.database)

        a.append("%s)" % self.path)

        return " ".join(a)
'''
