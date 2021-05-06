"""Fetch a snippet from Gitlab"""
import sys

import click
import gitlab
from gitlab import GitlabGetError


@click.command()
@click.argument('snip_id')
@click.argument('target')
@click.option('--gl-url', envvar='CI_SERVER_URL', help='URL to Gitlab server')
@click.option('--proj_id', envvar='CI_PROJECT_ID', type=int, help='Project ID')
@click.option('-t', '--token', envvar='CI_JOB_TOKEN', help='API access token')
def cli(snip_id, target, gl_url, proj_id, token):
    """

    :param snip_id: The ID of the snippet to fetch
    :param target: The filename of the target for the snippet file
    :param gl_url: The Gitlab server URL
    :param proj_id: The project ID if the snippet is in a project
    :param token: The API token
    """
    gl = gitlab.Gitlab(gl_url, private_token=token)
    gl.auth()

    try:
        if proj_id:
            proj = gl.projects.get(proj_id)
            snippet = proj.snippets.get(snip_id)
        else:
            snippet = gl.snippets.get(snip_id)
    except GitlabGetError as ex:
        print('Failed to fetch snippet {}'.format(snip_id), file=sys.stderr)
        sys.exit(-1)

    with open(target, 'wb') as fp:
        fp.write(snippet.content())

    print('Wrote snippet {} content to {}'.format(snip_id, target))
