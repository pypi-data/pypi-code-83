import click


@click.command()
def hello():
    """Simple program that greets"""
    click.echo('Hello world')


if __name__ == '__main__':
    hello()
