from invoke import Collection, Context, task
from rich.console import Console

from outcome.devkit.invoke import app

console = Console()


@task
def info(c: Context):
    """Display the current git info."""
    git_info = app.get_git_info()

    if not git_info:
        console.print('You are not in a git repo', style='bold red')
        return

    console.print(git_info)


ns = Collection(info)
