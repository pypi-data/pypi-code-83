import argparse
import json
import logging.config
from argparse import ArgumentTypeError
from pathlib import Path

from gs_to_csv.exporter import GoogleSpreadSheetsToCSV

logger = logging.getLogger(__name__)


class DirectoryType:
    def __call__(self, string):
        # the special argument "-" means sys.std{in,out}
        if string == "-":
            raise ValueError("Argument `-` (std{in,out}) is not supported")
        # all other arguments are used as file names
        directory = Path(string)
        if not directory.is_dir():
            raise ArgumentTypeError(f"{string} is not a valid directory.")
        return directory


class FileType:
    def __call__(self, string):
        # the special argument "-" means sys.std{in,out}
        if string == "-":
            raise ValueError("Argument `-` (std{in,out}) is not supported")
        # all other arguments are used as file names
        file_ = Path(string)
        if not file_.is_file():
            raise ArgumentTypeError(f"{string} is not a valid file.")
        return file_


def logging_params(parser):
    logging_group = parser.add_argument_group("Logging params")
    logging_group.add_argument(
        "--logging-file",
        type=argparse.FileType("r"),
        help="Logging configuration file, (logging-level and logging-format "
        "are ignored if provide)",
    )
    logging_group.add_argument("--logging-level", default="INFO")
    logging_group.add_argument(
        "--logging-format",
        default="%(asctime)s - %(levelname)s (%(module)s%(funcName)s): " "%(message)s",
    )


def logging_configuration(arguments):

    logging.basicConfig(
        level=getattr(logging, arguments.logging_level.upper()),
        format=arguments.logging_format,
    )
    if arguments.logging_file:
        try:
            json_config = json.loads(arguments.logging_file.read())
            logging.config.dictConfig(json_config)
        except json.JSONDecodeError:
            logging.config.fileConfig(arguments.logging_file.name)


def main():
    parser = argparse.ArgumentParser(
        description="Convert google spreadsheet sheets to csv",
        epilog="This will create a .csv file per sheet with title match with the regex expression.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    converter_group = parser.add_argument_group("Converter options")
    converter_group.add_argument(
        "--service-account-credential-file",
        dest="service_account",
        # use custom FileType, not the argparse.FileType as
        # we want a PathLike object
        type=FileType(),
        help="If you want to use this command in a script without user "
        "interractions, you can create a service account from google console: "
        "https://developers.google.com/workspace/guides/create-credentials#create_a_service_account "
        "and share read access sheets you want to export.",
    )
    converter_group.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Tell this app tp overwrite existing files if present.",
    )
    converter_group.add_argument(
        "-b",
        "--buffer-lines",
        type=int,
        dest="buffer_lines",
        default=500,
        help="Maximum number of lines to retreive by http calls.",
    )
    converter_group.add_argument(
        "spreadsheet",
        type=str,
        help="Id of the spreadsheet you want to export to csv. "
        "Spreadsheet id is the weird data present in the uri just after `d/`: "
        "https://docs.google.com/spreadsheets/d/<the spreadsheet id is here>/",
    )
    converter_group.add_argument(
        "selector",
        type=str,
        help="Sheet selector is a regex expression to match sheets titles.\n"
        "Some examples:\n"
        " - `.*`: would export all sheets\n"
        " - `(abcd)|(efgh)`: would export abcd and efgh sheets",
    )
    converter_group.add_argument(
        "directory",
        type=DirectoryType(),
        help="Output directory with write access where csv files will be" "written.",
    )
    logging_params(parser)
    arguments = parser.parse_args()
    logging_configuration(arguments)
    exported = GoogleSpreadSheetsToCSV(
        arguments.directory,
        arguments.spreadsheet,
        arguments.selector,
        service_account=arguments.service_account,
        force=arguments.force,
        buffer_lines=arguments.buffer_lines,
    ).export()
    if len(exported) == 0:
        logging.error("No sheets match given regex %", arguments.selector)
        exit(1)
    print("\n".join(exported))


if __name__ == "__main__":
    main()
