# Imports

import logging
import os
from commonkit import highlight_code, read_file, truncate, write_file
from commonkit.shell import EXIT, TABLE_FORMAT, Table
from subprocess import getstatusoutput
from ..library.commands import DumpData, LoadData
from ..constants import LOGGER_NAME
from ..utils import filter_fixtures, load_fixtures, scan_fixtures

log = logging.getLogger(LOGGER_NAME)

# Functions


def dumpdata(path, apps=None, database=None, groups=None, models=None, natural_foreign=False, natural_primary=False,
             preview_enabled=False, project_root=None, settings=None):

    fixtures = load_fixtures(
        path,
        database=database,
        natural_foreign=natural_foreign,
        natural_primary=natural_primary,
        project_root=project_root,
        settings=settings
    )
    if not fixtures:
        return EXIT.ERROR

    success = list()
    _fixtures = filter_fixtures(fixtures, apps=apps, groups=groups, models=models, skip_readonly=True)
    for f in _fixtures:
        log.info("Dumping fixtures to: %s" % f.get_full_path())

        dump = DumpData(
            f.app,
            database=f.database,
            export=f.export,
            natural_foreign=f.natural_foreign,
            natural_primary=f.natural_primary,
            path=f.get_full_path(),
            settings=f.settings
        )
        if preview_enabled:
            success.append(True)
            if not os.path.exists(f.get_path()):
                print("mkdir -p %s" % f.get_path())

            print(dump.preview())

            if f.copy_to is not None:
                print("cp %s %s" % (f.get_full_path(), f.copy_to))
        else:
            if not os.path.exists(f.get_path()):
                os.makedirs(f.get_path())

            if dump.run():
                success.append(dump.run())

                if f.copy_to is not None:
                    getstatusoutput("cp %s %s" % (f.get_full_path(), f.copy_to))
            else:
                log.error(dump.get_output())
            
    if all(success):
        return EXIT.OK

    return EXIT.ERROR


def init(base_directory="source", force_enabled=False, preview_enabled=False, project_root=None, scan_enabled=False):
    # The base path is where global fixtures and the config.ini file are located.
    base_path = os.path.join(project_root, "deploy", "fixtures")

    if not os.path.exists(base_path):
        log.info("Creating fixtures directory.")
        if not preview_enabled:
            os.makedirs(base_path)

    # The path to the config.ini file.
    config_path = os.path.join(base_path, "config.ini")

    if os.path.exists(config_path) and not force_enabled:
        log.warning("A %s file already exists. Use the -F switch to force initialization (and scanning if "
                    "using -S). Alternatively, use the -p switch to copy and paste the results of the "
                    "init." % config_path)

        return EXIT.TEMP

    # Output for the config is collected in a list with or without scan_enabled.
    output = list()

    # Scan for fixture files.
    if scan_enabled:
        path = os.path.join(project_root, base_directory)
        if not os.path.exists(path):
            log.error("Path does not exist: %s" % path)
            return EXIT.ERROR

        log.info("Scanning the project for fixture files.")
        results = scan_fixtures(path)
        for app_name, file_name, relative_path in results:
            log.debug("Found fixtures for %s app: %s/%s" % (app_name, relative_path, file_name))

            output.append("[%s]" % app_name)
            output.append("file_name = %s" % file_name)
            output.append("path = %s" % relative_path)
            output.append("")

        # for root, directories, files in os.walk(path):
        #     for f in files:
        #         if not f.endswith(".json"):
        #             continue
        #
        #         relative_path = root.replace(path + "/", "")
        #         # print(root.replace(path + "/", ""), f)
        #
        #         app_name = os.path.basename(os.path.dirname(relative_path))
        #
        #         log.debug("Found fixtures for %s app: %s/%s" % (app_name, relative_path, f))
        #
        #         output.append("[%s]" % app_name)
        #         output.append("file_name = %s" % f)
        #         output.append("path = %s" % relative_path)
        #         output.append("")
    else:
        output.append(";[app_name]")
        output.append(";file_name = fixture-file-name.json")
        output.append("")

    if preview_enabled:
        print("\n".join(output))
        return EXIT.OK

    log.info("Writing config.ini file.")
    write_file(config_path, content="\n".join(output))

    if scan_enabled:
        log.warning("Fixture entries may not exist in the correct order for loading. Please double-check and change "
                    "as needed.")

    return EXIT.OK


def inspect(path, apps=None, groups=None, models=None, project_root=None):
    fixtures = load_fixtures(path, project_root=project_root)
    if not fixtures:
        return EXIT.ERROR

    exit_code = EXIT.OK
    _fixtures = filter_fixtures(fixtures, apps=apps, groups=groups, models=models)
    for f in _fixtures:
        try:
            content = read_file(f.get_full_path())
        except FileNotFoundError as e:
            exit_code = EXIT.IO
            content = str(e)

        print("")
        print(f.label)
        print("-" * 120)
        print(highlight_code(content, language="json"))
        print("-" * 120)

    return exit_code


def ls(path, apps=None, groups=None, models=None, project_root=None):
    fixtures = load_fixtures(path, project_root=project_root)
    if not fixtures:
        return EXIT.ERROR

    headings = [
        "App",
        "File Name",
        "Path",
        "Read Only",
        "Group",
        "Comment",
    ]
    table = Table(headings, output_format=TABLE_FORMAT.SIMPLE)

    _fixtures = filter_fixtures(fixtures, apps=apps, groups=groups, models=models)
    for f in _fixtures:
        readonly = "no"
        if f.readonly:
            readonly = "yes"

        comment = "None."
        if f.comment:
            comment = truncate(f.comment)

        values = [
            f.app,
            f.file_name,
            f.path,
            readonly,
            f.group,
            comment
        ]
        table.add(values)

    print("")
    print("Configured Fixtures")
    print("")
    print(table)
    print("")

    return EXIT.OK


def loaddata(path, apps=None, database=None, groups=None, models=None, preview_enabled=False, project_root=None,
             settings=None, to_script=False):

    fixtures = load_fixtures(path, database=database, project_root=project_root, settings=settings)
    if not fixtures:
        return EXIT.ERROR

    if to_script:
        script = list()
        script.append("!# /usr/bin/env bash")
        script.append("")

    success = list()
    _fixtures = filter_fixtures(fixtures, apps=apps, groups=groups, models=models)
    for f in _fixtures:
        log.info("Loading fixtures from: %s" % f.get_full_path())

        load = LoadData(
            f.app,
            database=f.database,
            path=f.get_full_path(),
            settings=f.settings
        )

        if to_script:
            # noinspection PyUnboundLocalVariable
            script.append(load.preview())
            continue

        if preview_enabled:
            success.append(True)
            print(load.preview())
        else:
            if load.run():
                success.append(load.run())
            else:
                log.error(load.get_output())

    if to_script:
        script.append("")
        print("\n".join(script))
        return EXIT.OK

    if all(success):
        return EXIT.OK

    return EXIT.ERROR


def scan(path, base_directory="source", project_root=None):
    configured_fixtures = load_fixtures(path, project_root=project_root)


    search_path = os.path.join(project_root, base_directory)
    if not os.path.exists(search_path):
        log.error("Path does not exist: %s" % search_path)
        return EXIT.ERROR

    headings = [
        "App Name",
        "File Name",
        "Path",
        "Configured",
    ]
    table = Table(headings, output_format=TABLE_FORMAT.SIMPLE)

    results = scan_fixtures(search_path)
    for values in results:
        configured = "no"
        for cf in configured_fixtures:
            conditions = [
                cf.app == values[0],
                cf.file_name == values[1],
                cf.path == values[2],
            ]
            if all(conditions):
                configured = "yes"
                break
            elif any(conditions):
                configured = "maybe"
                break
            else:
                configured = "no"

        _values = list(values)
        _values.append(configured)

        table.add(_values)

    print("")
    print("Fixtures Found in Project")
    print("")
    print(table)
    print("")

    return EXIT.OK

'''

def dumpdata(args):
    """Dump data using a fixtures.ini file."""

    # Make sure the file exists.
    path = args.path
    if not os.path.exists(path):
        logger.warning("fixtures.ini file does not exist: %s" % path)
        return EXIT_INPUT

    # Load the file.
    ini = ConfigParser()
    ini.read(path)

    # Generate the commands.
    for model in ini.sections():
        kwargs = dict()

        if args.full_preview_enabled:
            kwargs['preview'] = True

        if args.settings:
            kwargs['settings'] = args.settings

        for key, value in ini.items(model):
            kwargs[key] = value

        fixture = Fixture(model, "dumpdata", **kwargs)
        if args.app_labels and fixture.app_label not in args.app_labels:
            logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if args.model_name and fixture.model_name.lower() != args.model_name.lower():
            logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if args.groups and fixture.group not in args.groups:
            logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if fixture.is_readonly:
            logger.info("(READONLY) %s (dumpdata skipped)" % fixture.model)
            continue

        if args.preview_enabled or args.full_preview_enabled:
            logger.info("(PREVIEW) %s" % fixture.preview())

            if args.full_preview_enabled:
                fixture.run()
                print(fixture.output)
        else:
            result = fixture.run()
            if result:
                logger.info("(OK) %s" % fixture.model)
            else:
                logger.info("(FAILED) %s %s" % (fixture.model, fixture.output))
                return EXIT.UNKNOWN

    return EXIT.OK


def loaddata(args):
    """Load data using a fixtures.ini file."""

    path = args.path
    if not os.path.exists(path):
        logger.warning("fixtures.ini file does not exist: %s" % path)
        return EXIT_INPUT

    # Load the file.
    ini = ConfigParser()
    ini.read(path)

    # Generate the commands.
    for model in ini.sections():
        kwargs = dict()

        if args.settings:
            kwargs['settings'] = args.settings

        for key, value in ini.items(model):
            kwargs[key] = value

        fixture = Fixture(model, "loaddata", **kwargs)

        if args.app_labels and fixture.app_label not in args.app_labels:
            if args.preview_enabled:
                logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if args.model_name and fixture.model_name.lower() != args.model_name.lower():
            if args.preview_enabled:
                logger.info("(SKIPPED) %s" % fixture.model)

            continue

        if args.groups and fixture.group not in args.groups:
            if args.preview_enabled:
                logger.info("[SKIPPED] %s" % fixture.model)

            continue

        if args.preview_enabled:
            logger.info("(PREVIEW) %s" % fixture.preview())
        else:
            result = fixture.run()
            if result:
                logger.info("(OK) %s %s" % (fixture.model, fixture.output))
            else:
                logger.warning("(FAILED) %s %s" % (fixture.model, fixture.output))
                return EXIT.UNKNOWN

    return EXIT.OK
'''
