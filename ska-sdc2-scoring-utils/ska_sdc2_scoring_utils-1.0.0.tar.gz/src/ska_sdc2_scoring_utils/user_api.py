# coding: utf-8
"""SDC2 scoring service API functions."""
import urllib.parse
from http import HTTPStatus
import json

import requests

from ska_sdc2_scoring_utils.api_common import (
    LOG,
    SDC_SCORE_API_URL,
    display_table,
    get_token,
    sdcss_get,
)


def display_leaderboard(
    catalogue_version: str,
    sub_info: bool = False,
    score_info: bool = False,
    output_raw: bool = False,
):
    """Display the leaderboard.

    Args:
        catalogue_version(str): Catalogue version (1.full or 1.dev)
        sub_info (bool): Optional; Show additional submission details.
        score_info (bool): Optional; Show additional score details.
        output_raw (bool): Optional; Display the raw SDCSS leaderboard data.

    Raises:
        RuntimeError: If unable to display the leaderboard.
    """
    # Get the leaderboard from the SDCSS API
    try:
        leaderboard = sdcss_get(f"/sdc2/v{catalogue_version}/leaderboard")
    except RuntimeError as error:
        LOG.error(
            "Unable to display the leaderboard for catalogue version %s",
            catalogue_version,
        )
        raise error
    # If the leaderboard is empty return
    if not leaderboard:
        LOG.warning(
            "Leaderboard is empty for SDC2 catalogue version: %s", catalogue_version
        )
        return
    # Prepare the leaderboard data for display.
    for i, entry in enumerate(leaderboard):
        entry["index"] = i
        if score_info:
            if entry["contents"]:
                for key, value in entry["contents"].items():
                    entry["contents" + key] = value
            else:
                for key in ["n_det", "n_match", "n_bad", "n_false"]:
                    entry["contents_" + key] = None
    # Display the leaderboard.
    if output_raw:
        LOG.info(json.dumps(leaderboard, indent=2))
    else:
        fields = [
            ("Rank", "index", 6),
            ("Score", "score", 15),
            ("Group", "group_name", 30),
        ]
        if score_info:
            fields.append(("Detected", "contents_n_det", 10))
            fields.append(("Matched", "contents_n_match", 10))
            fields.append(("Bad", "contents_n_bad", 10))
            fields.append(("False", "contents_n_false", 10))
        if sub_info:
            fields.append(("Submission ID", "submission_id", 38))
            fields.append(("Submitted Date", "submitted_date", 28))
            fields.append(("Username", "username", 25))
        display_table(leaderboard, fields=fields)
    return leaderboard


def create_submission(
    username: str,
    password: str,
    catalogue_file: str,
    catalogue_version: str,
    hidden: bool = False,
):
    """Create submision.

    Args:
        username (str): Username for the submission
        password (str): Password for the submission
        catalogue_file (str): Path to the catalogue file to submit
        catalogue_version (str): Catalogue version being submitted against
        hidden (bool): Optional; Submission is hidden from leaderboards

    Raises:
        RuntimeError: If unable to create the submission.

    """
    auth_token = get_token(username, password)
    LOG.info("Creating submission:")
    LOG.info("  Catalogue file .. : %s", catalogue_file)
    LOG.info("  Catalogue version : %s", catalogue_version)
    LOG.info("  Username ........ : %s", username)
    LOG.info("  Hidden? ......... : %s", hidden)
    headers = {"Authorization": "Bearer " + auth_token["access_token"]}
    files = {
        "submissionFile": (
            catalogue_file,
            open(catalogue_file, "rb"),
            "text/plain",
        )
    }
    params = urllib.parse.urlencode(
        {
            "version": catalogue_version,
            "subSkipRows": 0,
            "truthSkipRows": 0,
            "hidden": hidden
        }
    )
    url = SDC_SCORE_API_URL + f"/sdc2/v{catalogue_version}/submission" + "?" + params
    LOG.debug(url)
    resp = requests.post(url, files=files, headers=headers, timeout=10)
    data = resp.json()
    if resp.status_code == HTTPStatus.OK.value:
        LOG.info("Submission successful!")
        LOG.info("  Submission ID: %s", data["submission_id"])
    else:
        raise RuntimeError(
            "Failed to create submission. code: {}, data: {}".format(
                resp.status_code, data
            )
        )
    return data


def submission_list(
    username,
    password,
    limit: int,
    catalogue_version: str,
    score_info: bool = False,
    output_raw: bool = False,
):
    """List submissions."""
    LOG.debug("Authenticating as user: %s", username)
    submissions = sdcss_get(
        f"/sdc2/v{catalogue_version}/submission/search",
        params=dict(limit=limit),
        username=username,
        password=password,
    )
    submissions = sorted(submissions, key=lambda k: k["submitted_date"], reverse=True)
    for i, submission in enumerate(submissions):
        submission["index"] = i
        submission["catalogue"] = catalogue_version
        if score_info:
            if submission["contents"]:
                for key, value in submission["contents"].items():
                    submission["contents" + key] = value
            else:
                for key in ["n_det", "n_match", "n_bad", "n_false"]:
                    submission["contents_" + key] = None

    if output_raw:
        print(json.dumps(submissions, indent=2, sort_keys=True))
    else:
        fields = [
            ("Index", "index", 6),
            ("ID", "submission_id", 38),
            ("Status", "status", 15),
            ("Score", "score", 10),
        ]
        if score_info:
            fields.append(("Detected", "contents_n_det", 10))
            fields.append(("Matched", "contents_n_match", 10))
            fields.append(("Bad", "contents_n_bad", 10))
            fields.append(("False", "contents_n_false", 10))
        fields.append(("Submitted Date", "submitted_date", 28))
        fields.append(("Hidden", "is_hidden", 8))
        fields.append(("Catalogue", "catalogue", 11))
        display_table(submissions, fields)


def submission_info(uuid: str, catalogue_version: str, output_raw: bool = False):
    """Get the submission information."""
    try:
        submission = sdcss_get(
            f"/sdc2/v{catalogue_version}/submission", params=dict(submissionId=uuid)
        )
    except RuntimeError as error:
        LOG.error(
            "Failed to get submission information for submission with uuid: %s", uuid
        )
        raise error
    if output_raw:
        print(json.dumps(submission, indent=2, sort_keys=True))
    else:
        LOG.info("{:20.20s} | {:40.40s}".format("Key", "Value"))
        LOG.info("{:21.21s}|{:41.41s}".format("-" * 40, "-" * 40))
        LOG.info("{:20.20s} | {}".format("Id", uuid))
        LOG.info("{:20.20s} | {}".format("Status", submission["submission_status"]))
        LOG.info(
            "{:20.20s} | {}".format("Submitted date", submission["submitted_date"])
        )
        LOG.info("{:20.20s} | {}".format("User Id", submission["user_id"]))
        LOG.info("{:20.20s} | {}".format("Catalogue version", catalogue_version))
        LOG.info("{:20.20s} | {}".format("Hidden", submission["is_hidden"]))
        result = submission["result_contents"]
        if result is not None:
            LOG.info("{:20.20s} | {}".format("Result - Score", result["_value"]))
            LOG.info("{:20.20s} | {}".format("Result - Detected", result["_n_det"]))
            LOG.info("{:20.20s} | {}".format("Result - Matches", result["_n_match"]))
            LOG.info("{:20.20s} | {}".format("Result - Bad", result["_n_bad"]))
            LOG.info("{:20.20s} | {}".format("Result - False", result["_n_false"]))
        else:
            LOG.info("{:20.20s} | {}".format("Result", "Not available, try later"))
    return submission
