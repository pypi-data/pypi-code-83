import typer

from sitez import __version__

app = typer.Typer(name="sitez", no_args_is_help=True)


@app.command("version")
def describe_version() -> None:
    typer.echo(f"Sitez version: {__version__}")


@app.command("init")
def init(path: str) -> None:
    typer.echo(f"Init sitez project at {path}")


def run():
    app()
