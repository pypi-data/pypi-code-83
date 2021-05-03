import click, requests

url_prefix = "https://gentle-brushlands-20368.herokuapp.com/"

@click.group()
def main():
    pass

@main.command()
@click.argument("keyword")
def insert(keyword):
    res = requests.put(f"{url_prefix}insert", json={"keyword": keyword})
    click.echo(res.text)

@main.command()
@click.argument("keyword")
def delete(keyword):
    res = requests.delete(f"{url_prefix}delete?keyword={keyword}")
    click.echo(res.text)

@main.command()
@click.argument("keyword")
def search(keyword):
    res = requests.get(f"{url_prefix}search?keyword={keyword}")
    click.echo(res.text)

@main.command()
@click.argument("prefix")
def autocomplete(prefix):
    res = requests.get(f"{url_prefix}autocomplete?prefix={prefix}")
    click.echo(res.text)

@main.command()
def display():
    res = requests.get(f"{url_prefix}display")
    click.echo(res.text)
