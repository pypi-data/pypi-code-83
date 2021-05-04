# coding: utf-8
"""SDC2 scoring service admin API functions."""
import os
import json
from typing import Union, List

import random
import string

from ska_sdc2_scoring_utils.api_common import (
    LOG,
    display_table,
    sdcss_get,
    sdcss_post,
    sdcss_delete,
)

USER = os.getenv("SDC2_SCORER_ADMIN_USER", None)
PASSWORD = os.getenv("SDC2_SCORER_ADMIN_PASSWORD", None)


# =============================================================================
# Utility methods
# =============================================================================


def get_group(group_identifier: str, groups: list = None) -> str:
    """Return the full group uuid and name for a specified group name or ID stub.

    Args:
        group_identifier(str): Name or ID, minimally matched.
        groups(list): Optional; Cached list of groups

    Return:
        tuple uuid and name of the group or None if not match is found.

    Raises:
        RuntimeError: More than one match found.
        ValueError: Specified group identifier is empty or does not match any group.

    """
    if not groups:
        groups = sdcss_get("/groups", username=USER, password=PASSWORD)
    matches = []
    for group in groups:
        _id = group["id"]
        _name = group["group_name"]
        if _id.startswith(group_identifier) or _name.startswith(group_identifier):
            matches.append((_id, _name))
    if not group_identifier:
        raise ValueError("Empty group identifier specified.")
    if not matches:
        raise ValueError(
            f"Unable to find group matching identifier: {group_identifier}"
        )
    if len(matches) > 1:
        LOG.debug("Group identifier: %s (matches)", group_identifier)
        for match in matches:
            LOG.debug("  %s", match)
        raise RuntimeError("Specified group has multiple matches!")
    return matches[0]


def group_exists(name: str) -> bool:
    """Check if group exists.

    Args:
        name (str): Full name of the group

    Returns:
        bool, true if the group exists, otherwise false.

    """
    groups = sdcss_get("/groups", username=USER, password=PASSWORD)
    try:
        _ = next(
            group_data["id"]
            for group_data in groups
            if group_data["group_name"] == name
        )
        return True
    except StopIteration:
        return False


# =============================================================================
# GROUP CLI methods
# =============================================================================


def group_list(show_users: bool = False, output_raw: bool = False):
    """Display list of groups.

    Args:
        show_users(bool): Show users in each group (default: False)

    """
    groups = sdcss_get("/groups", username=USER, password=PASSWORD)
    groups = sorted(groups, key=lambda k: k["group_name"].lower(), reverse=False)
    users = sdcss_get("/users", username=USER, password=PASSWORD)
    for index, group in enumerate(groups):
        group["index"] = str(index)
        group_users = [user for user in users if user["group_id"] == group["id"]]
        group["num_users"] = len(group_users)
        group["users"] = group_users
    if not groups:
        LOG.warning("No groups found!")
        return
    if output_raw:
        LOG.info(json.dumps(groups, indent=2, sort_keys=True))
    else:
        display_table(
            data=groups,
            fields=[
                ("Index", "index", 6),
                ("Name", "group_name", 30),
                ("No. users", "num_users", 12),
                ("uuid", "id", 38),
            ],
            indent=0,
        )
        if show_users:
            LOG.info("")
            for group in groups:
                if group["num_users"] > 0:
                    LOG.info(f"Group {group['index']} '{group['group_name']}' users:")
                    LOG.info("")
                    display_table(
                        group["users"],
                        fields=[
                            ("Last name", "last_name", 20),
                            ("First name", "first_name", 20),
                            ("username", "username", 20),
                            ("Id", "id", 38),
                        ],
                        indent=0,
                    )
                    LOG.info("")
    return groups


def group_add(name: Union[str, List[str]]):
    """Add a new group.

    Args:
        name (Union[str, List[str]]): Name of the group to add.

    Raises:
        ValueError: Requested group already exists.
        RuntimeError: Scoring service failed to add a group.

    """
    # If the group name is a list (ie has spaces) join it into a single str
    if isinstance(name, list):
        name = " ".join(name)
    LOG.info("Adding group: '%s'", name)
    # Checknot trying to add a group with the same name (SDCSS currently allows this)
    if group_exists(name):
        raise ValueError("Failed to add group, group already exists!")
    try:
        resp = sdcss_post(
            "/groups", params=dict(name=name), username=USER, password=PASSWORD
        )
        data = resp.json()
        LOG.info("Successfully added group '%s', uuid = %s", name, data["group_id"])
        return data
    except RuntimeError as error:
        raise error


def group_delete(identifier: Union[str, List[str]]):
    """Remove a group by name or uuid.

    Args:
        identifier(Union[str, List[str]]): Group name or id. Minimal match used.

    Raises:
        RuntimeError: If the request to delete the group could not be satisfied

    """
    # If the group name is a list (ie has spaces) join it into a single str
    if isinstance(identifier, list):
        identifier = " ".join(identifier)
    uuid, name = get_group(identifier)
    LOG.info("Deleting group: '%s' (%s)", name, uuid)
    try:
        sdcss_delete(
            "/groups", params=dict(groupId=uuid), username=USER, password=PASSWORD
        )
        LOG.info("Successfully deleted group '%s'", name)
    except RuntimeError as error:
        raise error


# =============================================================================
# USER CLI methods
# =============================================================================


def user_list(output_raw: bool = False):
    """Display list of users."""
    users = sdcss_get("/users", username=USER, password=PASSWORD)
    users = sorted(users, key=lambda k: k["last_name"].lower(), reverse=False)
    groups = sdcss_get("/groups", username=USER, password=PASSWORD)
    for index, user in enumerate(users):
        user["index"] = str(index)
        user["group_name"] = get_group(user["group_id"], groups)[1]
    if output_raw:
        LOG.info(json.dumps(users, indent=2, sort_keys=True))
    else:
        display_table(
            data=users,
            fields=[
                ("Index", "index", 6),
                ("Last name", "last_name", 15),
                ("First name", "first_name", 15),
                ("username", "username", 15),
                ("Email", "email", 35),
                ("uuid", "id", 38),
                ("Group", "group_name", 30),
            ],
        )
    return users


def user_add(
    first_name: str,
    last_name: str,
    username: str,
    email: str,
    group_identifier: str,
    password: str = None,
):
    """Add a new user.

    Args:
        first_name (str): First name of the user
        last_name (str): Last name of the user
        username (str): User name for the user
        email (str): User's email
        group_identifier (str): Group name or ID stub, minimally matched.
        password (str, Optional): User password, if not set it is autogenerated.


    Raises:
        RuntimeError: When it is not possible to add a user.
    """
    # Genereate a password if not provided.
    if not password:
        password_chars = string.ascii_letters + string.punctuation + string.digits
        password = "".join(
            random.choice(password_chars) for x in range(random.randint(8, 16))
        )

    # Get the Group UUID (and name) from the provided id or name stub.
    group_uuid, group_name = get_group(group_identifier)

    LOG.info("Adding user:")
    LOG.info("  First name : %s", first_name)
    LOG.info("  Last name  : %s", last_name)
    LOG.info("  Username   : %s", username)
    LOG.info("  Email      : %s", email)
    LOG.info("  Group      : %s (%s)", group_name, group_uuid)
    LOG.info("  Password   : %s", password)

    # Construct the request to add the user.
    try:
        resp = sdcss_post(
            "/users",
            params=dict(
                firstName=first_name,
                lastName=last_name,
                username=username,
                email=email,
                groupId=group_uuid,
                password=password,
            ),
            username=USER,
            password=PASSWORD,
        )
        data = resp.json()
        LOG.info(
            "Successfully added user. uuid = %s",
            data["user_id"],
        )
        return data
    except RuntimeError as error:
        LOG.error("Failed to add user")
        raise error


def get_uuid_for_username(username: str):
    """Return the user uuid for a specified username."""
    users = sdcss_get("/users", username=USER, password=PASSWORD)
    try:
        uuid = next(user["id"] for user in users if user["username"] == username)
        return uuid
    except StopIteration:
        return None


def get_user(user_identifier: str) -> str:
    """Return the full user uuid and name for a specified username or ID stub.

    Args:
        user_identifier(str): Name or ID, minimally matched.

    Return:
        user object matched

    Raises:
        RuntimeError: More than one match found.
        ValueError: Specified group identifier is empty or does not match any group.

    """
    users = sdcss_get("/users", username=USER, password=PASSWORD)
    matches = []
    for user in users:
        _id = user["id"]
        _username = user["username"]
        if _id.startswith(user_identifier) or _username.startswith(user_identifier):
            matches.append(user)
    if not user_identifier:
        raise ValueError("Empty user identifier specified.")
    if not matches:
        raise ValueError(f"Unable to find user matching identifier: {user_identifier}")
    if len(matches) > 1:
        LOG.debug("User identifier: %s (matches)", user_identifier)
        for match in matches:
            LOG.debug("  %s", match)
        raise RuntimeError("Specified user has multiple matches!")
    return matches[0]


def user_delete(user_identifier: Union[str, List[str]]):
    """Delete a user.

    Args:
        user_identifier: Username or uuid, minimally matched

    Raises:
        RuntimeError: If delete fails

    """
    if isinstance(user_identifier, list):
        user_identifier = " ".join(user_identifier)
    user = get_user(user_identifier)
    LOG.info("Deleting user identified by %s", user_identifier)
    LOG.info("  Last name  : %s", user["last_name"])
    LOG.info("  First name : %s", user["first_name"])
    LOG.info("  Username   : %s", user["username"])
    LOG.info("  UUID       : %s", user["id"])
    LOG.info("  Group UUID : %s", user["group_id"])
    try:
        sdcss_delete(
            "/users", params=dict(userId=user["id"]), username=USER, password=PASSWORD
        )
        LOG.info("Successfully deleted user")
    except RuntimeError as error:
        LOG.error("Failed to delete user.")
        raise error


# =============================================================================
# Submission methods
# =============================================================================


def submission_list(catalogue_version: str, limit: int = 20, output_raw: bool = False):
    """Display list of submissions.

    Args:
        catalogue_version(str): The SDC2 catalogue version (1.dev, or 1.full)
        limit(int): Optional; Maximum number of submissions to show.
        output_raw(bool): Optional; Display raw response data.

    """
    submissions = sdcss_get(
        f"/sdc2/v{catalogue_version}/submission/search",
        params=dict(limit=limit),
        username=USER,
        password=PASSWORD,
    )
    submissions = sorted(submissions, key=lambda k: k["submitted_date"], reverse=True)
    LOG.info("Latest %d submissions for catalogue '%s':", limit, catalogue_version)
    LOG.info("")

    users = sdcss_get("/users", username=USER, password=PASSWORD)
    for i, submission in enumerate(submissions):
        submission["index"] = str(i)
        submission["is_hidden"] = str(submission["is_hidden"])
        submission["score"] = str(submission["score"])
        for user in users:
            if user["id"] == submission["user_id"]:
                submission["username"] = user["username"]
                break
    if output_raw:
        LOG.info(json.dumps(submissions, indent=2))
    else:
        display_table(
            submissions,
            fields=[
                ("Index", "index", 6),
                ("Id", "submission_id", 38),
                ("date", "submitted_date", 28),
                ("Status", "status", 15),
                ("username", "username", 20),
                ("Score", "score", 15),
                ("Hidden", "is_hidden", 8),
            ],
        )


def submission_rm(identifier: str, catalogue_version: str):
    """Remove a submission.

    Args:
        identifier(str): Submission uuid, minimally matched.
        catalogue_version(str): Submission catalogue version

    Raises:
        RuntimeError: If the submission cant be removed.

    """
    LOG.info("Removing submission...")
    LOG.info("  Submission id ... : %s", identifier)
    LOG.info("  Catalogue version : %s", catalogue_version)
    submissions = sdcss_get(
        f"/sdc2/v{catalogue_version}/submission/search",
        params=dict(limit=999),
        username=USER,
        password=PASSWORD,
    )
    matches = []
    for sub in submissions:
        if sub["submission_id"].startswith(identifier):
            matches.append(sub["submission_id"])
    if not matches:
        raise RuntimeError("Submission not found.")
    if len(matches) > 1:
        raise RuntimeError(
            "Specified identifier '{}' matches {} submissions!".format(
                identifier, len(matches)
            )
        )
    uuid = matches[0]
    LOG.info("Found match to submission with UUID: %s", uuid)
    try:
        sdcss_delete(
            f"/sdc2/v{catalogue_version}/submission",
            params=dict(submissionId=uuid),
            username=USER,
            password=PASSWORD,
        )
        LOG.info("Successfully deleted submission")
    except RuntimeError as error:
        LOG.error("Failed to delete submission.")
        raise error
