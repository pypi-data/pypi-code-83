import click

from marleu_pytest.greetings.bad import bad_greeting
from marleu_pytest.greetings.good import good_greeting


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
@click.option("--intention", help="Intention of greeting, could be bad or good.")
def hello(count, name, intention):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        if intention == "bad":
            click.echo(bad_greeting())
        elif intention == "good":
            click.echo(good_greeting())
        else:
            click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    hello()
