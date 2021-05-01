# Imports

from configparser import ConfigParser
import logging
import os
from commonkit import smart_cast
from .constants import LOGGER_NAME

log = logging.getLogger(LOGGER_NAME)

# Exports

__all__ = (
    "filter_fixtures",
    "load_fixtures",
    "scan_fixtures",
)

# Functions


def filter_fixtures(fixtures, apps=None, groups=None, models=None, skip_readonly=False):
    """Filter fixtures for various criteria.

    :param fixtures: The fixtures to be filtered.
    :type fixtures: list[fixman.library.files.FixtureFile]

    :param apps: Include only the provided app names.
    :type apps: list[str]

    :param groups: Include only the provided group names.
    :type groups: list[str]

    :param models: Include only the provided model names.
    :type models: list[str]

    :param skip_readonly: Skip fixtures that are marked read only.
    :type skip_readonly: bool

    :rtype: list[fixman.library.files.FixtureFile]
    :returns: The filters that match the given criteria.

    """
    _fixtures = list()
    for f in fixtures:
        if apps is not None and f.app not in apps:
            log.debug("Skipping %s app (not in apps list)." % f.app)
            continue

        # BUG: Model filter will return on a partial match; Group and Grouping.
        if models is not None and f.model is not None and f.model not in models:
            log.debug("Skipping %s model (not in models list)." % f.model)
            continue

        if groups is not None and f.group not in groups:
            log.debug("Skipping %s (not in group)." % f.label)
            continue

        if f.readonly and skip_readonly:
            log.debug("Skipping %s (read only)." % f.label)
            continue

        _fixtures.append(f)

    return _fixtures


def load_fixtures(path, **kwargs):
    """Load fixture meta data.

    :param path: The path to the fixtures INI file.
    :type path: str

    :rtype: list[FixtureFile] | None

    Remaining keyword arguments are passed to the file.

    """
    from .library.files import FixtureFile

    if not os.path.exists(path):
        log.error("Path does not exist: %s" % path)
        return None

    ini = ConfigParser()
    ini.read(path)

    fixtures = list()
    group = None
    for section in ini.sections():
        _kwargs = kwargs.copy()

        _section = section
        if ":" in section:
            _section, group = section.split(":")

        if "." in _section:
            app_label, model_name = _section.split(".")
        else:
            app_label = _section
            model_name = None

        _kwargs['group'] = group
        _kwargs['model'] = model_name

        for key, value in ini.items(section):
            if key == "db":
                key = "database"
            elif key == "nfk":
                key = "natural_foreign"
            elif key == "npk":
                key = "natural_primary"
            else:
                pass

            _kwargs[key] = smart_cast(value)

        fixtures.append(FixtureFile(app_label, **_kwargs))

    return fixtures


def scan_fixtures(path):
    """Scan for fixture files on the given path.

    :param path: The path to scan.
    :type path: str

    :rtype: list
    :returns: A list of three-element tuples; the app name, file name, and relative path.

    """
    results = list()
    for root, dirs, files in os.walk(path):
        relative_path = root.replace(path + "/", "")
        if relative_path.startswith("static") or relative_path.startswith("theme"):
            continue

        for f in files:
            if not f.endswith(".json"):
                continue

            app_name = os.path.basename(os.path.dirname(relative_path))

            results.append((app_name, f, relative_path))

    return results
