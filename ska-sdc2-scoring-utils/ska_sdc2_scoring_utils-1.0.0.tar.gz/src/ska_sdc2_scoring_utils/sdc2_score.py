# coding: utf-8
"""sdc2-score.

A command line interface client for the SKA Science Data Challenge scoring service.

Usage:
    sdc2-score leaderboard [--sub-info] [--score-info] [--raw] [-c VERSION]
    sdc2-score create CATALOGUE_FILE [-u USERNAME] [-p PASSWORD] [-c VERSION] [--hidden]
    sdc2-score info SUBMISSION_ID [-c VERSION] [--raw]
    sdc2-score ls [-u USERNAME] [-p PASSWORD] [-n LIMIT] [--score-info] [--raw] [-c VERSION]
    sdc2-score -h | --help | --version

Options:
    --sub-info           Display additional submission information.
    --score-info         Display additional score information.
    --raw                Display the raw response from the SDC scoring service.
    --hidden             If passed, submission will be hidden from leaderboards
    -c VERSION           Set the catalogue version (1.dev, 1.ldev, 1.full) [default: 1.full].
    -n LIMIT             Maximum number of submissions to list [default: 20].
    -u USER              Scoring service username.
    -p PASSWORD          Scoring service user password.
    -h, --help           Show this screen.
    --version            Show the version.

Arguments
    CATALOGUE_FILE      Path to catalogue file to submit.
    SUBMISSION_ID       Submission ID, minimally matched.

"""
import sys
import os
import logging

from docopt import docopt

from ska_sdc2_scoring_utils import user_api
from ska_sdc2_scoring_utils.logs import init_logger
from ska_sdc2_scoring_utils.api_common import LOG, SDC_SCORE_VERBOSE
from ska_sdc2_scoring_utils.__version__ import __version__


# coding: utf-8
def process_commands(args):
    """Process commands."""
    # print(args)
    if args["leaderboard"]:
        return user_api.display_leaderboard(
            catalogue_version=args["-c"],
            sub_info=args["--sub-info"],
            score_info=args["--score-info"],
            output_raw=args["--raw"],
        )

    elif args["create"]:
        username, password = get_login_credentials(args)
        return user_api.create_submission(
            username, password, args["CATALOGUE_FILE"], args["-c"], args["--hidden"]
        )

    elif args["ls"]:
        username, password = get_login_credentials(args)
        return user_api.submission_list(
            username,
            password,
            limit=args["-n"],
            score_info=args["--score-info"],
            catalogue_version=args["-c"],
            output_raw=args["--raw"],
        )

    elif args["info"]:
        return user_api.submission_info(
            args["SUBMISSION_ID"],
            catalogue_version=args["-c"],
            output_raw=args["--raw"],
        )


def get_login_credentials(args):
    """Get log-in credentials.

    Returns username and password either from arguments or environment variables.
    An error message is displayed if either one of these is not resolved.

    Args:
        args (argparse.args): Command line parser args object
    """
    username = args["-u"]
    password = args["-p"]
    if not username:
        username = os.getenv("SDC2_SCORER_USER", None)
    if not password:
        password = os.getenv("SDC2_SCORER_PASSWORD", None)
    if not username:
        LOG.error(
            "User not specified. Please see CLI arguments [-h] or set "
            "env variable 'SDC2_SCORER_USER'"
        )
    if not password:
        LOG.error(
            "Password not specified. Please see CLI arguments [-h] or set "
            "env variable 'SDC2_SCORER_PASSWORD'"
        )
    if not password or not username:
        sys.exit(1)
    return username, password


def main():
    """."""
    args = docopt(__doc__, version=__version__)

    # SDC_SCORE_VERBOSE = True
    init_logger(
        logging.DEBUG if SDC_SCORE_VERBOSE else logging.INFO,
        SDC_SCORE_VERBOSE,
        SDC_SCORE_VERBOSE,
    )

    try:
        process_commands(args)
    except (ValueError, RuntimeError) as error:
        LOG.error("ERROR: %s", error)


if __name__ == "__main__":
    main()
