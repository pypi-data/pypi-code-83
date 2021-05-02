import getpass
import json
from pathlib import Path

import click
import requests

session_data = {}

session_file = Path('~/.vulseek/session.json').expanduser()
session_file.parent.mkdir(exist_ok=True)

class VulseekSession():
    pass

def load_session():
    session_data = {}
    if session_file.is_file():
        session_data = json.load(session_file.open())
    return session_data


def save_session(session_data):
    with session_file.open('w') as outfile:
        outfile.write(json.dumps(session_data, indent=4))


@click.group()
@click.pass_context
def cli(ctx):

    ctx.obj = VulseekSession()
    ctx.obj.data = load_session()
    ctx.obj.requests = requests.Session()

    if ctx.obj.data:
        ctx.obj.requests.headers.update({
            'Authorization': f'Bearer {ctx.obj.data["access_token"]}'
        })


@cli.command(help='List current sessions')
@click.pass_obj
def session(session):

    if not session.data:
        click.echo('Not logged in')
        return False

    click.echo(json.dumps(dict(
        username=session.data['username'],
        endpoint=session.data['endpoint'],
    ), indent=4))


@cli.command(help='Create new session')
@click.argument('endpoint', default='http://localhost:8080')
def login(endpoint):

    username = input('Username: ')
    password = getpass.getpass(prompt='Password: ')

    save_session({})

    r = requests.post(endpoint + '/user/login', data=dict(username=username, password=password))
    if r.status_code != 200:
        click.echo('Invalid credentials', err=True)
        return False

    access_token = r.json()['access_token']

    session_data = {
        'endpoint': endpoint,
        'username': username,
        'access_token': access_token,
    }

    save_session(session_data)


@cli.command(help="Logout")
def logout():
    save_session({})


@cli.command(help='List objects')
@click.argument('object_type', type=click.Choice(['domain', 'finding', 'hostname', 'ip', 'network', 'web']))
@click.pass_obj
def ls(session, object_type):

    response = session.requests.get('{}/{}/'.format(session.data['endpoint'], object_type))
    if response.status_code != 200:
        click.echo(response.content.decode(), err=True)
        return False

    for obj in response.json():
        if 'identity' in obj:
            print(obj['identity'])
        else:
            print('{} - {}'.format(obj['score'], obj['title']))


@cli.command(help="Add object")
@click.argument('object_type', type=click.Choice(['domain', 'hostname', 'ip', 'network', 'web']))
@click.argument('identity')
@click.pass_obj
def add(session, object_type, identity):

    response = session.requests.post('{}/{}/'.format(session.data['endpoint'], object_type), json=dict(identity=identity))
    if response.status_code != 200:
        click.echo('{}: {}'.format(response.status_code, response.content.decode()), err=True)
        return False

    click.echo(json.dumps(response.json(), indent=4))


@cli.command(help="Delete object")
@click.argument('object_type', type=click.Choice(['domain', 'hostname', 'ip', 'network', 'web']))
@click.argument('identity')
@click.pass_obj
def delete(session, object_type, identity):

    response = session.requests.get('{}/{}/'.format(session.data['endpoint'], object_type))
    if response.status_code != 200:
        click.echo(response.content.decode(), err=True)
        return False

    object_id = None
    for obj in response.json():
        if obj['identity'] == identity:
            object_id = obj['id']

    if not object_id:
        click.echo('404: Not found')
        return False

    response = session.requests.delete('{}/{}/{}/'.format(session.data['endpoint'], object_type, object_id))
    if response.status_code != 200:
        click.echo(response.content.decode(), err=True)
        return False


@cli.command(help='Upload files')
@click.argument('files', nargs=-1, type=click.Path())
@click.pass_obj
def upload(session, files):

    for filename in files:

        try:
            data = open(filename).read()
        except Exception as e:
            click.echo(f'{filename}: {e}')
            continue

        response = session.requests.post(session.data['endpoint'] + '/upload/', files=dict(file_obj=data))

        if response.status_code == 200:
            click.echo(f'{filename}: OK')
        else:
            click.echo('{filename}: {error}'.format(filename=filename, error=response.content.decode()))


if __name__ == '__main__':
    cli()
