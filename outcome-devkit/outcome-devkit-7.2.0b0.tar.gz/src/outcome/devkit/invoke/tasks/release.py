from typing import Optional

from invoke import Collection, Context, task

from outcome.devkit.invoke import app
from outcome.devkit.invoke.tasks import clean


@task(clean.all)
def build(c: Context):
    """Build the python package."""
    c.run('poetry build')


@task(build)
def publish(c: Context, repository_name: Optional[str] = None, repository_url: Optional[str] = None):
    """Publish the python package."""

    info = app.get_app_info()

    if any((repository_name, repository_url)) and not all((repository_name, repository_url)):
        raise RuntimeError('You must provide both name and URL when specifying a custom package repository')

    repo_name = repository_name or info.package_repository_name
    repo_url = repository_url or info.package_repository_url

    if repo_name and repo_url:
        c.run(f'poetry config repositories.{repo_name} {repo_url}')
        c.run(f'poetry publish -n -r {repo_name}')
    else:
        c.run('poetry publish -n')


ns = Collection(build, publish)
