#!/usr/bin/env python3
"""
Really, relentlessly and repeatedly remove files and all of their copies.

LICENSE
   MIT (https://mit-license.org/)

COPYRIGHT
   © 2021 Steffen Brinkmann <s-b@mailbox.org>
"""

__author__ = "Steffen Brinkmann"
__version__ = "0.1.0"
__license__ = "MIT"


import argparse
import csv
import logging
import os
import sys
from hashlib import (
    blake2b,
    blake2s,
    md5,
    sha1,
    sha3_224,
    sha3_256,
    sha3_384,
    sha3_512,
    sha224,
    sha256,
    sha384,
    sha512,
    shake_128,
    shake_256,
)
from time import process_time, sleep, time
from typing import Callable

LOG_FORMAT = "rrm: %(levelname)-9s: %(message)s"
logging.basicConfig(format=LOG_FORMAT)

db_fieldnames = ["basename", "abspath", "size", "hash_1000", "hash", "hashname"]

hash_algo: dict[str, Callable] = {
    "sha1": sha1,
    "sha224": sha224,
    "sha256": sha256,
    "sha384": sha384,
    "sha512": sha512,
    "blake2b": blake2b,
    "blake2s": blake2s,
    "md5": md5,
    "sha3_224": sha3_224,
    "sha3_256": sha3_256,
    "sha3_384": sha3_384,
    "sha3_512": sha3_512,
    "shake_128": shake_128,
    "shake_256": shake_256,
}

_DEBUG_MODE = False
_QUIET_MODE = False


def _set_logging_level(
    quiet: bool, verbose: bool, debug: bool
) -> None:  # pragma: no cover
    """set reasonable logging levels"""
    if debug is True:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.info("debug mode engaged")
    if verbose is True:
        logging.getLogger().setLevel(logging.INFO)
    if quiet is True:
        logging.getLogger().setLevel(logging.ERROR)


def _parse_arguments(argv=None) -> argparse.Namespace:
    """parse the command line options"""
    parser = argparse.ArgumentParser(
        description="Really, relentlessly and repeatedly remove files and all of their copies.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "paths",
        metavar="PATH",
        type=str,
        nargs="+",
        help="each PATH is checked whether it is a regular file or a directory. "
        "If it is a regular file it will be deleted or moved to DIR (see -m option), unless -n is used, "
        "and added the the database. "
        "If it is a directory, the directory is scanned for matches to the files in the database (not implemented yet). "
        "Note that there is a huge difference between 'some_directory/' and 'some_directory/*'!!",
    )
    parser.add_argument(
        "-m",
        "--move",
        type=str,
        metavar="DIR",
        default=argparse.SUPPRESS,
        nargs="?",
        help="move to a directory instead of deleting the files permanently. "
        "If DIR is not set (but the option is used), $HOME/.config/rrm/deleted_files/ is used. "
        "The directory will be created if ",
    )
    parser.add_argument(
        "-d",
        "--db-file",
        type=str,
        metavar="DB",
        default="$HOME/.config/rrm/rrmdb.csv",
        help="the name of the database file. If DB does not exist, it will be created, "
        "otherwise rrm will append to the file. "
        "If DB is a directory, rrm will look for 'DB/.rrmdb.csv' and create the file if it does not exist. "
        "If this option is omitted, rrm will use (and create if inexistent) $HOME/.config/rrm/rrmdb.csv",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="check for files to be deleted recursively. (not implemented yet)",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="gather the files to be deleted, display them and ask once to delete all of them."
        "The files are only added to the database if the deletion is confirmed",
    )
    parser.add_argument(
        "-I",
        "--very-interactive",
        action="store_true",
        help="gather the files to be deleted, display them and ask for every file before deleting it."
        "The files are only added to the database if the deletion is confirmed",
    )
    parser.add_argument(
        "-n",
        "--no-action",
        action="store_true",
        help="gather the files to be processed, and only add them to the database without "
        "actually deleting or moving them.",
    )
    parser.add_argument(
        "-H",
        "--hash-algorithm",
        type=str,
        metavar="HASH",
        default="sha1",
        help=f"which hash algorithm to use. Currently supported are: {', '.join(hash_algo.keys())}",
    )
    parser.add_argument(
        "-l",
        "--follow-symlinks",
        action="store_true",
        help="whether to follow symlinks",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="show the version of this software",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="switch off text output except for error messages. This will overwrite -v.",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="more verbose text output"
    )
    parser.add_argument(
        "-D",
        "--debug",
        action="store_true",
        help="switch on debug mode. This will show a lot of debugging information.",
    )
    return parser.parse_args(argv)


def process_files(mode: str, files: list[str], move_dir=None) -> int:
    """processes files according to mode
    mode: str, one of "delete", "move"
    files: list[str], list of paths
    move_dir: str, path of target directory, mandatory if mode == "move"
    returns the number of successfully moved files
    """

    result = 0
    if mode == "delete":
        # better save than sorry:
        logging.warning(
            "The following files are going to be removed. Hit Ctrl-C to abort!"
        )
        print("\n".join(files))
        input()
        for p in files:
            os.remove(p)
            result += 1
    elif mode == "move":
        assert move_dir
        assert os.path.isdir(move_dir)
        for p in files:
            os.replace(p, os.path.join(move_dir, os.path.basename(p)))
            result += 1

    return result


def main(argv: list = None) -> None:
    """The command line tool. Please use the ``--help`` option to get help."""

    global _QUIET_MODE
    global _DEBUG_MODE

    # parse the command line options
    args = _parse_arguments(argv)

    # set quiet mode
    _QUIET_MODE = args.quiet

    # set debug mode
    _DEBUG_MODE = args.debug

    # print the version
    if _DEBUG_MODE:  # pragma: no cover
        print(f"version: {__version__}")

    # get time for later
    if not _QUIET_MODE:  # pragma: no cover
        t_start = time()

    # set verbosity level
    _set_logging_level(args.quiet, args.verbose, args.debug)

    logging.debug(args)

    # setting the hash algorithm
    hash_algo_name = args.hash_algorithm

    # set the data base file
    db_filename = os.path.abspath(os.path.expandvars(os.path.expanduser(args.db_file)))
    if not os.path.exists(os.path.dirname(db_filename)):
        os.makedirs(os.path.dirname(db_filename), exist_ok=True)
        logging.debug(f"created directory {os.path.dirname(db_filename)}")
    if os.path.isdir(db_filename):
        db_filename = os.path.join(db_filename, ".rrmdb.csv")
    logging.info(f"using database file {db_filename}")

    # set the mode (one of "move", "delete")
    mode = "delete"
    move_dir = None
    if "move" in args:
        mode = "move"
        move_dir = args.move or os.path.join(
            os.environ["HOME"], ".config/rrm/deleted_files/"
        )
        os.makedirs(move_dir, exist_ok=True)

    # get files and directories from the command line arguments
    file_paths = [os.path.abspath(p) for p in args.paths if os.path.isfile(p)]
    dir_paths = [os.path.abspath(p) for p in args.paths if os.path.isdir(p)]
    if not args.follow_symlinks:
        file_paths = [p for p in file_paths if not os.path.islink(p)]
        dir_paths = [p for p in dir_paths if not os.path.islink(p)]

    # ask for user confirmation
    if args.very_interactive:
        files_to_be_processed = [
            p for p in file_paths if input(f"process {p} (y/[n])? ") == "y"
        ]
    elif args.interactive:
        print("Process these files?\n", "\n".join(file_paths), "", sep="\n")
        files_to_be_processed = file_paths if input(f"(y/[n]) ") == "y" else []
    else:
        files_to_be_processed = file_paths

    # read database into a dict
    files_in_db = {}
    if os.path.isfile(db_filename):
        with open(db_filename, "r") as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                files_in_db[row["hash"]] = row
    else:
        with open(db_filename, "w", newline="") as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=db_fieldnames)
            csvwriter.writeheader()

    # gather information of each file, only if it is not already in the database
    files_to_be_processed_info = []
    for p in files_to_be_processed:
        file_content = open(p, "rb").read()
        _hash = hash_algo[hash_algo_name](file_content).hexdigest()
        if (
            _hash in files_in_db
            and files_in_db[_hash]["hashname"] == hash_algo_name
            and files_in_db[_hash]["abspath"] == os.path.abspath(p)
        ):
            # skip files with the same hash and absolute path
            logging.info(f"file {os.path.abspath(p)} was already in the database.")
        else:
            _hash_1000 = hash_algo[hash_algo_name](file_content[:1000]).hexdigest()
            files_to_be_processed_info.append(
                {
                    "basename": os.path.basename(p),
                    "abspath": os.path.abspath(p),
                    "size": os.path.getsize(p),
                    "hash_1000": _hash_1000,
                    "hash": _hash,
                    "hashname": hash_algo_name,
                }
            )

    # append to database
    with open(db_filename, "a", newline="") as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=db_fieldnames)
        csvwriter.writerows(files_to_be_processed_info)

    # process files
    if not args.no_action:
        n_files_processed = process_files(mode, files_to_be_processed, move_dir)
        if n_files_processed != len(files_to_be_processed):
            logging.warning(
                f"Only {n_files_processed} of {len(files_to_be_processed)} files have been processed."
            )

    # output time measurement
    if _DEBUG_MODE:  # pragma: no cover
        logging.debug("all done.")
        logging.debug(
            f"this took {process_time():.4f} s = {round(process_time()/60, 2)} min of process time"
        )
        logging.debug(
            f"and {(time()-t_start):.4f} s = {round((time()-t_start)/60, 2)} min of wallclock time"
        )


if __name__ == "__main__":
    main()
