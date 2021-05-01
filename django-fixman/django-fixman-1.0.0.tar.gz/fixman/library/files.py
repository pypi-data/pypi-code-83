# Imports

import os

# Exports

__all__ = (
    "FixtureFile",
)

# Classes


class FixtureFile(object):
    """Represents a fixture file."""

    def __init__(self, app, comment=None, copy_to=None, database=None, file_name=None, group=None, model=None,
                 natural_foreign=False, natural_primary=False, path=None, project_root=None, readonly=False,
                 settings=None):
        """Initialize a fixture file.

        :param app: The name of the app to which the fixture file belongs.
        :type app: str

        :param comment: A comment regarding the fixture file.
        :type comment: str

        :param copy_to: The path to which the fixture file should be copied.
        :type copy_to: str

        :param database: The database name into which the fixtures are installed.
        :type database: str

        :param file_name: The file name of the file.
        :type file_name: str

        :param group: The group into which the fixtures are organized.
        :type group: str

        :param model: The name of the model to which the fixtures apply.
        :type model: str

        :param natural_foreign: Indicates whether natural foreign keys are used.
        :type natural_foreign: bool

        :param natural_primary: Indicates whether natural primary keys are used.
        :type natural_primary: bool

        :param path: The path to the fixture file, excluding the file name.
        :type path: str

        :param project_root: The root (path) of the project where the fixture is used.
        :type project_root: str

        :param readonly: Indicates the fixture file may only be loaded (not dumped).
        :type readonly: bool

        :param settings: The settings to use when loading or dumping data.
        :type settings: str

        """
        self.app = app
        self.comment = comment
        self.copy_to = copy_to
        self.database = database
        self.file_name = file_name or "initial.json"
        self.group = group
        self.model = model
        self.natural_foreign = natural_foreign
        self.natural_primary = natural_primary
        self.readonly = readonly
        self.settings = settings

        if model is not None:
            self.export = "%s.%s" % (app, model)

            if file_name is None:
                self.file_name = "%s.json" % model.lower()
        else:
            self.export = app

        source = ""
        if path is not None:
            source = "source"
            self.path = path
        else:
            self.path = os.path.join("fixtures", app)

        if project_root is not None:
            self._full_path = os.path.join(project_root, source, self.path, self.file_name)
        else:
            self._full_path = os.path.join(source, self.path, self.file_name)

    def __repr__(self):
        return "<%s %s>" %  (self.__class__.__name__, self._full_path)

    def get_path(self):
        """Get the path to the fixture file (without the file).

        :rtype: str

        """
        return os.path.dirname(self._full_path)

    def get_full_path(self):
        """Get the full path to the fixture file.

        :rtype: str

        """
        return self._full_path

    @property
    def label(self):
        """Get a display name for the fixture.

        :rtype: str

        """
        if self.model is not None:
            return "%s.%s" % (self.app, self.model)

        return self.app
