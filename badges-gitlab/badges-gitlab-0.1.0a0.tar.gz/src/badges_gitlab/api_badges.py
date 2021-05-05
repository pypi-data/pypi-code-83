"""This VI uses the Gitlab API Functions to create json files for badges"""
import os

import gitlab  # type: ignore
import iso8601  # type: ignore

from . import badges_json

# This function calls the Gitlab API and fetches some project information
# Author: Felipe P. Silva
# E-mail: felipefoz@gmail.com


def validate_path(directory_path):
    """Validates destination path, if not found, creates it"""
    if not os.path.isdir(directory_path):
        try:
            # Create  Directory MyDirectory
            os.makedirs(directory_path)
            # print if directory created successfully...
            print("Directory ", directory_path, " created!")
        except FileExistsError:
            # print if directory already exists...
            print("Directory ", directory_path, " already exists...")


def issues(project_ref, directory_path):
    """Retrieves issues count data"""
    # Format :  {'statistics': {'counts': {'all': 30, 'closed': 13, 'opened': 7}}}
    issues_dict = project_ref.issuesstatistics.get().statistics['counts']
    badges_json.json_badge(directory_path, 'issues',
                           badges_json.print_json("Issues", str(issues_dict['all']), "blue"))
    badges_json.json_badge(directory_path, 'open_issues',
                           badges_json.print_json("Open issues", str(issues_dict['opened']), "red"))
    badges_json.json_badge(directory_path, 'closed_issues',
                           badges_json.print_json("Closed issues", str(issues_dict['closed']), "green"))


def general_data(project_ref, directory_path):
    """Retrieves General Data"""
    # Licences may not be found, therefore the Try Function
    try:
        badges_json.json_badge(directory_path, 'license_key',
                               badges_json.print_json("License", project_ref.license['key'], "yellow"))
        badges_json.json_badge(directory_path, 'license_name',
                               badges_json.print_json("License", project_ref.license['name'], "yellow"))
    except TypeError:
        print("Licenses not found, skipping...")
    finally:
        badges_json.json_badge(directory_path, 'project_id',
                               badges_json.print_json("ID", str(project_ref.id), "purple"))
        badges_json.json_badge(directory_path, 'owner',
                               badges_json.print_json("Owner", project_ref.namespace['name'], "yellow"))
        # noinspection SpellCheckingInspection
        badges_json.json_badge(directory_path, 'name',
                               badges_json.print_json("Name", project_ref.name, "yellowgreen"))
        badges_json.json_badge(directory_path, 'default_branch',
                               badges_json.print_json("Default branch", project_ref.default_branch, "green"))
        created_at = iso8601.parse_date(project_ref.created_at).strftime('%B %Y')
        # noinspection SpellCheckingInspection
        badges_json.json_badge(directory_path, 'created_at',
                               badges_json.print_json("Create at", created_at, "lightgrey"))
        last_activity_at = iso8601.parse_date(project_ref.last_activity_at).strftime('%-d %B %Y')
        # noinspection SpellCheckingInspection
        badges_json.json_badge(directory_path, 'last_activity_at',
                               badges_json.print_json("Last Activity", last_activity_at, "lightgrey"))
        badges_json.json_badge(directory_path, 'contributors',
                               badges_json.print_json("Contributors",
                                                      len(project_ref.repository_contributors()), "blue"))
        badges_json.json_badge(directory_path, 'forks_count',
                               badges_json.print_json("Forks", str(project_ref.forks_count), "orange"))
        # noinspection SpellCheckingInspection
        badges_json.json_badge(directory_path, 'star_count',
                               badges_json.print_json("Stars", str(project_ref.star_count), "yellowgreen"))


def releases_commits(project_ref, directory_path):
    """Retrieves Releases, Tags and Commits related data"""
    badges_json.json_badge(directory_path, 'commits',
                           badges_json.print_json("Commits", str(len(project_ref.commits.list())), "red"))
    last_commit_at = iso8601.parse_date(project_ref.commits.list()[0].created_at).strftime('%B %Y')
    # noinspection SpellCheckingInspection
    badges_json.json_badge(directory_path, 'last_commit',
                           badges_json.print_json("Last Commit", last_commit_at, "lightgrey"))

    # Test if releases exist
    try:
        badges_json.json_badge(directory_path, 'release',
                               badges_json.print_json("Release", project_ref.releases.list()[0].name, "green"))
        released_at = iso8601.parse_date(project_ref.releases.list()[0].released_at).strftime('%B %Y')
        # noinspection SpellCheckingInspection
        badges_json.json_badge(directory_path, 'last_release',
                               badges_json.print_json("Last Release", released_at, "lightgrey"))
        badges_json.json_badge(directory_path, 'releases',
                               badges_json.print_json("Releases", str(len(project_ref.releases.list())), "red"))
    except IndexError:
        print("No releases found, skipping...")
    # Test if tags exist
    try:
        badges_json.json_badge(directory_path, 'tag',
                               badges_json.print_json("Tag", project_ref.tags.list()[0].name, "green"))
        tag_created_at = iso8601.parse_date(project_ref.tags.list()[0].commit['created_at']).strftime('%B %Y')
        # noinspection SpellCheckingInspection
        badges_json.json_badge(directory_path, 'last_tag',
                               badges_json.print_json("Last Tag", tag_created_at, "lightgrey"))
    except IndexError:
        print("No tags found, skipping...")


def create_api_badges(directory_path, private_token: str):
    """Authenticates to API and call the json creation functions"""
    if os.environ.get('CI_SERVER_URL'):
        # Check destination directory and create if needed
        validate_path(directory_path)
        # Authentication
        try:
            gitlab_auth = gitlab.Gitlab(os.environ['CI_SERVER_URL'], private_token=private_token)
            # project id from environment
            project = gitlab_auth.projects.get(int(os.environ['CI_PROJECT_ID']), license='true')
            # Issues Data
            issues(project, directory_path)
            # General Data
            general_data(project, directory_path)
            # Releases and Commit Data
            releases_commits(project, directory_path)
        except gitlab.exceptions.GitlabGetError:
            print('Unable to authenticate, invalid credentials!')
    else:
        print("Invalid environment variables, skipping API Data step!")
