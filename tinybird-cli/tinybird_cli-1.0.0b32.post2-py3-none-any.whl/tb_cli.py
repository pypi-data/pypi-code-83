import logging
import json
import glob
import os.path
import click
import re
import pprint
from pathlib import Path
from urllib.parse import urlencode, urlparse, quote
from toposort import toposort
from collections import defaultdict
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import humanfriendly
import humanfriendly.tables
from tinybird.client import TinyB, AuthException, AuthNoTokenException, CanNotBeDeletedException, DoesNotExistException
from tinybird.check_pypi import CheckPypi
from sys import version_info
from tinybird.datafile import (
    folder_push,
    get_name_tag_version,
    parse_pipe,
    parse_datasource,
    ParseException,
    get_project_filenames,
    build_graph)

from tinybird import __cli__
from .feedback_manager import FeedbackManager

import asyncio
from functools import wraps
from tinybird.connectors import create_connector, UNINSTALLED_CONNECTORS

from tinybird.config import get_config, write_config

create_connector_fn = create_connector


def create_connector(connector, options):
    if connector in UNINSTALLED_CONNECTORS:
        raise click.ClickException(FeedbackManager.error_connector_not_installed(connector=connector))
    return create_connector_fn(connector, options)


try:
    from tinybird.__cli__ import __revision__
except Exception:
    __revision__ = None

CURRENT_VERSION = f"{__cli__.__version__}"
VERSION = f"{__cli__.__version__} (rev {__revision__})"
DEFAULT_HOST = 'https://api.tinybird.co'
DEFAULT_UI_HOST = 'https://ui.tinybird.co'
SUPPORTED_CONNECTORS = ['bigquery', 'snowflake']
PROJECT_PATHS = [
    'datasources',
    'datasources/fixtures',
    'endpoints',
    'explorations',
    'pipes'
]
MIN_WORKSPACE_ID_LENGTH = 36

check_pypi = CheckPypi()


class TablesHelper:
    def __init__(self, host, token):
        self.host = host
        self.token = token
        self._session = None

    @property
    def session(self):
        if not self._session:
            self._session = requests.Session()
            retries = Retry(total=5, backoff_factor=0.2)
            self._session.mount('http://', HTTPAdapter(max_retries=retries))
            self._session.mount('https://', HTTPAdapter(max_retries=retries))
        return self._session

    def _request(self, path, params):
        try:
            headers = {'Authorization': f"Bearer {self.token}"}
            response = self.session.post(url=f"{self.host}{path}", params=params, headers=headers)
            result = response.json()
            if 'error' in result:
                raise ValueError(result['error'])
            return result
        except Exception as e:
            raise e

    def sql_get_used_tables(self, sql, raising=False):
        params = {
            'q': sql,
            'raising': 'true' if raising else 'false'
        }
        result = self._request('/v0/sql_tables', params)
        return [tuple(t) for t in result['tables']]

    def replace_tables(self, q, replacements):
        params = {
            'q': q,
            'replacements': json.dumps({k[1] if isinstance(k, tuple) else k: v
                                       for k, v in replacements.items()})
        }
        result = self._request('/v0/sql_replace', params)
        return result['query']


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if version_info[1] >= 7:  # FIXME drop python 3.6 support
            return asyncio.run(f(*args, **kwargs))
        else:
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(f(*args, **kwargs))
    return wrapper


def print_data_table(res):
    if not res['data']:
        click.echo(FeedbackManager.info_no_rows())
        return

    dd = []
    for d in res['data']:
        dd.append(d.values())
    click.echo(humanfriendly.tables.format_smart_table(dd, column_names=res['data'][0].keys()))


def normalize_datasource_name(s):
    s = re.sub(r'[^0-9a-zA-Z_]', '_', s)
    if s[0] in '0123456789':
        return "c_" + s
    return s


def generate_datafile(datafile, filename, csv_data, force):
    p = Path(filename)
    base = Path('datasources')
    if not base.exists():
        base = Path()
    f = base / (normalize_datasource_name(p.stem) + ".datasource")
    if not f.exists() or force:
        open(f'{f}', 'w').write(datafile)
        click.echo(FeedbackManager.success_generated_file(file=f, stem=p.stem, filename=filename))

        if csv_data:
            # generate fixture
            if (base / 'fixtures').exists():
                f = base / 'fixtures' / (p.stem + ".csv")
                newline = '\n'  # TODO: guess
                open(f, 'w').write(csv_data[:csv_data.rindex(newline)])
                click.echo(FeedbackManager.success_generated_fixture(fixture=f))
    else:
        click.echo(FeedbackManager.error_file_already_exists(file=f))


class CatchAuthExceptions(click.Group):
    """utility class to get all the auth exceptions"""
    def __call__(self, *args, **kwargs):
        try:
            return self.main(*args, **kwargs)
        except AuthNoTokenException:
            click.echo(FeedbackManager.error_notoken())
        except AuthException as exc:
            click.echo(FeedbackManager.error_exception(error=exc))


def load_connector_config(ctx, connector, debug, check_uninstalled=False):
    config_file = Path(os.getcwd()) / f".tinyb_{connector}"
    try:
        if connector not in ctx.obj:
            config = json.loads(open(config_file).read())
            if check_uninstalled and connector in UNINSTALLED_CONNECTORS:
                click.echo(FeedbackManager.warning_connector_not_installed(connector=connector))
                return
            ctx.obj[connector] = create_connector(connector, config)
    except IOError:
        if debug:
            click.echo(f"** {connector} connector not configured")
        pass


@click.group(cls=CatchAuthExceptions)  # noqa: C901
@click.option('--debug/--no-debug', default=False, help="Print internal representation")
@click.option('--token', envvar='TB_TOKEN', help="Use auth token, defaults to TB_TOKEN envvar, then to the .tinyb file")
@click.option('--host', envvar='TB_HOST', help="Use custom host, defaults to TB_HOST envvar, then to https://api.tinybird.co")
@click.option('--gcp-project-id', help="The Google Cloud project ID")
@click.option('--gcs-bucket', help="The Google Cloud Storage bucket to write temp files when using the connectors")
@click.option('--google-application-credentials', envvar='GOOGLE_APPLICATION_CREDENTIALS', help="Set GOOGLE_APPLICATION_CREDENTIALS")
@click.option('--sf-account', help="The Snowflake Account (e.g. your-domain.west-europe.azure)")
@click.option('--sf-warehouse', help="The Snowflake warehouse name")
@click.option('--sf-database', help="The Snowflake database name")
@click.option('--sf-schema', help="The Snowflake schema name")
@click.option('--sf-role', help="The Snowflake role name")
@click.option('--sf-user', help="The Snowflake user name")
@click.option('--sf-password', help="The Snowflake password")
@click.option('--sf-storage-integration', help="The Snowflake GCS storage integration name (leave empty to auto-generate one)")
@click.option('--sf-stage', help="The Snowflake GCS stage name (leave empty to auto-generate one)")
@click.version_option(version=VERSION)
@click.pass_context
@coro
async def cli(ctx, debug, token, host, gcp_project_id, gcs_bucket, google_application_credentials, sf_account, sf_warehouse, sf_database, sf_schema, sf_role, sf_user, sf_password, sf_storage_integration, sf_stage):  # noqa: C901
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below
    latest_version = await check_pypi.get_latest_version()

    if latest_version != CURRENT_VERSION and not os.environ.get("PYTEST", None):
        click.echo(FeedbackManager.warning_update_version(latest_version=latest_version))
        click.echo(FeedbackManager.warning_current_version(current_version=CURRENT_VERSION))

    ctx.ensure_object(dict)

    if debug:
        logging.basicConfig(level=logging.DEBUG)

    config = await get_config(host, token)
    ctx.obj['config'] = config

    if ctx.invoked_subcommand == 'auth':
        return

    if gcp_project_id and gcs_bucket and google_application_credentials and not sf_account:
        bq_config = {
            'project_id': gcp_project_id,
            'bucket_name': gcs_bucket,
            'service_account': google_application_credentials,
        }
        ctx.obj['bigquery'] = create_connector('bigquery', bq_config)
    if sf_account and sf_warehouse and sf_database and sf_schema and sf_role and sf_user and sf_password and gcs_bucket and google_application_credentials and gcp_project_id:
        sf_config = {
            'account': sf_account,
            'warehouse': sf_warehouse,
            'database': sf_database,
            'schema': sf_schema,
            'role': sf_role,
            'user': sf_user,
            'password': sf_password,
            'storage_integration': sf_storage_integration,
            'stage': sf_stage,
            'bucket_name': gcs_bucket,
            'service_account': google_application_credentials,
            'project_id': gcp_project_id,
        }
        ctx.obj['snowflake'] = create_connector('snowflake', sf_config)

    logging.debug("debug enabled")

    ctx.obj['client'] = TinyB(config['token'], config['host'], version=VERSION)

    for connector in SUPPORTED_CONNECTORS:
        load_connector_config(ctx, connector, debug, check_uninstalled=True)


async def folder_init(client, folder, generate_datasources=False, type_guessing=True):
    for x in PROJECT_PATHS:
        try:
            f = Path(folder) / x
            f.mkdir()
            click.echo(FeedbackManager.info_path_created(path=x))
        except FileExistsError:
            click.echo(FeedbackManager.info_path_already_exists(path=x))
            pass

    if generate_datasources:
        for filename in glob.glob('*.csv'):
            try:
                data = open(filename).read(1024 * 1024)
            except UnicodeDecodeError:
                try:
                    data = open(filename, encoding="ISO-8859-1").read(1024 * 1024)
                except UnicodeDecodeError:
                    raise Exception("can't guess charset for {filename}, convert it to UTF8")
            meta = await client.datasource_analyze_file(data.encode(), type_guessing=type_guessing)
            schema = meta['sql_schema'].replace(', ', ',\n    ')
            datafile = f"""DESCRIPTION generated from {filename}\n\nSCHEMA >\n    {schema}"""
            generate_datafile(datafile, filename, data, False)
    return


@cli.command()
@click.option('--generate-datasources', is_flag=True, default=False, help="Generate datasources based on csv files in this folder")
@click.option('--type-guessing', is_flag=True, default=True, help="When using ``false`` all columns are created as ``String`` otherwise it tries to guess the column types based on the CSV contents")
@click.option('--folder', default=None, type=click.Path(exists=True, file_okay=False), help="Folder where files will be placed")
@click.pass_context
@coro
async def init(ctx, generate_datasources, type_guessing, folder):
    """Initialize folder layout"""
    client = ctx.obj['client']
    folder = folder if folder else os.getcwd()
    await folder_init(client, folder, generate_datasources, type_guessing=type_guessing)
    return


@cli.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--debug', is_flag=True, default=False, help="Print internal representation")
def check(filename, debug):
    """Check file syntax"""
    click.echo(FeedbackManager.info_processing_file(filename=filename))

    try:
        if '.pipe' in filename:
            doc = parse_pipe(filename)
        else:
            doc = parse_datasource(filename)

        click.echo(FeedbackManager.success_processing_file(filename=filename))

    except ParseException as e:
        raise click.ClickException(FeedbackManager.error_exception(error=e))

    if debug:
        pp = pprint.PrettyPrinter()
        for x in doc.nodes:
            pp.pprint(x)


@cli.command()
@click.option('--prefix', default='', help="Use prefix for all the resources")
@click.option('--dry-run', is_flag=True, default=False, help="Run the command without creating resources on the Tinybird account or any side effect")
@click.option('--check/--no-check', is_flag=True, default=True, help="Enable/Disable output checking, enabled by default")
@click.option('--push-deps', is_flag=True, default=False, help="Push dependencies, disabled by default")
@click.option('--debug', is_flag=True, default=False, help="Print internal representation")
@click.option('--force', is_flag=True, default=False, help="Override pipes when they already exist")
@click.option('--populate', is_flag=True, default=False, help="Populate materialized nodes when pushing them")
@click.option('--fixtures', is_flag=True, default=False, help="Append fixtures to data sources")
@click.option('--wait', is_flag=True, default=False, help="Wait for populate job to finish, disabled by default")
@click.option('--skip-table-checks', is_flag=True, default=False, help="Skip materialized views checks, disabled by default")
@click.option('--ignore-sql-errors', is_flag=True, default=False, help="Does not validate the node SQL. Use it at your own risk")
@click.option('--yes', is_flag=True, default=False, help="Do not ask for confirmation")
@click.argument('filenames', type=click.Path(exists=True), nargs=-1, default=None)
@click.pass_context
@coro
async def push(ctx, prefix, filenames, dry_run, check, push_deps, debug, force, populate, fixtures, wait, skip_table_checks, ignore_sql_errors, yes):
    """Push files to Tinybird
    """
    token = ctx.obj['config'].get('token')
    host = ctx.obj['config'].get('host', DEFAULT_HOST)

    tables_helper = TablesHelper(host, token)

    await folder_push(
        token,
        host,
        prefix,
        filenames,
        dry_run,
        check,
        push_deps,
        debug,
        force,
        populate=populate,
        upload_fixtures=fixtures,
        wait=wait,
        skip_table_checks=skip_table_checks,
        ignore_sql_errors=ignore_sql_errors,
        tables_helper=tables_helper,
        skip_confirmation=yes
    )
    return


@cli.command()  # noqa: C901
@click.option('--folder', default=None, type=click.Path(exists=True, file_okay=False), help="Folder where files will be placed")
@click.option('--match', default=None, help='Retrieve any resourcing matching the pattern. eg --match _test')
@click.option('--prefix', default=None, help="Download only resources with this prefix")
@click.option('--force', is_flag=True, default=False, help="Override existing files")
@click.pass_context
@coro
async def pull(ctx, folder, match, prefix, force):
    """Retrieve latest versions for project files from Tinybird"""
    client = ctx.obj['client']
    folder = folder if folder else os.getcwd()

    await folder_pull(client, folder, match, prefix, force)
    return


async def folder_pull(client, folder, match, tag, force):  # noqa: C901
    pattern = re.compile(match) if match else None

    def _get_latest_versions(resources):
        versions = {}

        for x in resources:
            t = get_name_tag_version(x)
            t['original_name'] = x
            if t['version'] is None:
                t['version'] = -1
            name = t['name']

            if not tag:
                versions[name] = t
            elif t['tag'] == tag:
                if name in versions:
                    if versions[name]['version'] < t['version']:
                        versions[name] = t
                else:
                    versions[name] = t
        return versions

    async def write_files(versions, extension, get_resource_function, file_folder=None):
        values = versions.values()

        for k in values:
            name = f"{k['name']}.{extension}"

            f = Path(folder)
            if file_folder:
                f = Path(folder) / file_folder
            f = f / name
            if pattern and not pattern.search(name):
                click.echo(FeedbackManager.info_skipping_resource(resource=f))
                continue

            prefix_info = ''

            if not tag:
                if k['tag']:
                    prefix_info = f"({k['tag']})"
            else:
                prefix_info = f"({tag})"

            click.echo(FeedbackManager.info_writing_resource(resource=f, prefix=prefix_info))

            try:
                b = await getattr(client, get_resource_function)(k['original_name'])

                if not f.exists() or force:
                    with open(f, 'w') as fd:
                        # versions are a client only thing so
                        # datafiles from the server do not contains information about versions
                        if k['version'] >= 0:
                            b = f"VERSION {k['version']}\n" + b
                        if b:
                            fd.write(b)
                else:
                    click.echo(FeedbackManager.info_skip_already_exists())
            except Exception as e:
                raise Exception(FeedbackManager.error_exception(error=e))
        return

    try:
        datasources = await client.datasources()
        remote_datasources = sorted([x['name'] for x in datasources])
        versions = _get_latest_versions(remote_datasources)

        await write_files(versions, 'datasource', 'datasource_file')

        pipes = await client.pipes()
        remote_pipes = sorted([x['name'] for x in pipes])
        versions = _get_latest_versions(remote_pipes)

        await write_files(versions, 'pipe', 'pipe_file')

        return

    except Exception as e:
        raise click.ClickException(FeedbackManager.error_pull(error=str(e)))


@cli.command()
@click.option('--no-deps', is_flag=True, default=False, help="Print only data sources with no pipes using them")
@click.option('--match', default=None, help='Retrieve any resource matching the pattern')
@click.option('--pipe', default=None, help='Retrieve any resource used by pipe')
@click.pass_context
@coro
async def dependencies(ctx, no_deps, match, pipe):
    """
    Print all data sources dependencies
    """
    client = ctx.obj['client']
    datasources = await client.datasources()
    pipes = await client.pipes()
    pattern = re.compile(match) if match else None

    ds = defaultdict(set)
    if pipe:
        pipes = [x for x in pipes if pipe in x['name']]
    for p in pipes:
        for node in p['nodes']:
            for t in node['dependencies']:
                ds[t].add(p['name'])

    for x in datasources:
        if not pattern or pattern.search(x['name']):
            deps = [p for p in ds[x['name']]]
            if no_deps:
                if len(deps) == 0:
                    click.echo(FeedbackManager.info_dependency_list(dependency=x['name']))
            else:
                click.echo(FeedbackManager.info_dependency_list(dependency=x['name']))
                deps.sort()
                for d in deps:
                    click.echo(FeedbackManager.info_dependency_list_item(dependency=d))


def configure_connector(connector):
    if connector not in SUPPORTED_CONNECTORS:
        click.echo(FeedbackManager.error_invalid_connector(connectors=', '.join(SUPPORTED_CONNECTORS)))
        return

    file_name = f".tinyb_{connector}"
    config_file = Path(os.getcwd()) / file_name
    if connector == 'bigquery':
        project = click.prompt("BigQuery project ID")
        service_account = click.prompt("Path to a JSON service account file with permissions to export from BigQuery, write in Storage and sign URLs (leave empty to use GOOGLE_APPLICATION_CREDENTIALS environment variable)", default=os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', ''))
        bucket_name = click.prompt("Name of a Google Cloud Storage bucket to store temporary exported files")

        try:
            config = {
                'project_id': project,
                'service_account': service_account,
                'bucket_name': bucket_name
            }
            open(config_file, 'w').write(json.dumps(config))
        except Exception:
            raise click.ClickException(FeedbackManager.error_file_config(config_file=config_file))
    elif connector == 'snowflake':
        sf_account = click.prompt("Snowflake Account (e.g. your-domain.west-europe.azure)")
        sf_warehouse = click.prompt("Snowflake warehouse name")
        sf_database = click.prompt("Snowflake database name")
        sf_schema = click.prompt("Snowflake schema name")
        sf_role = click.prompt("Snowflake role name")
        sf_user = click.prompt("Snowflake user name")
        sf_password = click.prompt("Snowflake password")
        sf_storage_integration = click.prompt("Snowflake GCS storage integration name (leave empty to auto-generate one)", default='')
        sf_stage = click.prompt("Snowflake GCS stage name (leave empty to auto-generate one)", default='')
        project = click.prompt("Google Cloud project ID to store temporary files")
        service_account = click.prompt("Path to a JSON service account file with permissions to write in Storagem, sign URLs and IAM (leave empty to use GOOGLE_APPLICATION_CREDENTIALS environment variable)", default=os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', ''))
        bucket_name = click.prompt("Name of a Google Cloud Storage bucket to store temporary exported files")

        try:
            config = {
                'account': sf_account,
                'warehouse': sf_warehouse,
                'database': sf_database,
                'schema': sf_schema,
                'role': sf_role,
                'user': sf_user,
                'password': sf_password,
                'storage_integration': sf_storage_integration,
                'stage': sf_stage,
                'service_account': service_account,
                'bucket_name': bucket_name,
                'project_id': project,
            }
            open(config_file, 'w').write(json.dumps(config))
        except Exception:
            raise click.ClickException(FeedbackManager.error_file_config(config_file=config_file))

        click.echo(FeedbackManager.success_connector_config(connector=connector, file_name=file_name))


@cli.group(invoke_without_command=True)
@click.option('--host', envvar='TB_HOST', help="Set custom host if it's different than https://api.tinybird.co")
@click.option('--connector', type=click.Choice(['bigquery', 'snowflake'], case_sensitive=True), help="Set credentials for one of the supported connectors")
@click.pass_context
@coro
async def auth(ctx, host, connector):
    """Configure auth"""
    if connector:
        configure_connector(connector)
        return

    # only run when doing 'tb auth'
    if not ctx.invoked_subcommand:
        host = host or ctx.obj['config'].get('host', DEFAULT_HOST)
        ui_host = DEFAULT_UI_HOST if host == DEFAULT_HOST else host
        token = click.prompt(f"Copy the admin token from {ui_host}/tokens and paste it here", hide_input=True)

        client = TinyB(token, host, version=VERSION)

        try:
            response = await client.workspaces()
        except Exception:
            click.echo(FeedbackManager.error_invalid_token(host=host))
            return

        try:
            config_file = Path(os.getcwd()) / ".tinyb"
            config = json.loads(open(config_file).read())
        except Exception:
            config = {
                'host': host,
                'token': token,
                'workspaces': []
            }

        try:
            for workspace in response['workspaces']:
                if response['id'] == workspace['id']:
                    config['id'] = workspace['id']
                    config['name'] = workspace['name']
                    config['token'] = token
                    config['host'] = host

                    workspaces = config['workspaces'] if 'workspaces' in config else []
                    workspaces = [w for w in workspaces if w['id'] != workspace['id']]

                    workspaces.append({
                        'id': workspace['id'],
                        'name': workspace['name'],
                        'token': token,
                        'host': host
                    })

                    config['workspaces'] = workspaces

            if 'id' in config:
                await write_config(config)
                ctx.obj['client'] = TinyB(config['token'], config.get('host', DEFAULT_HOST), version=VERSION)
                ctx.obj['config'] = config
            else:
                click.echo(FeedbackManager.error_not_personal_auth())
                return

        except Exception as e:
            click.echo(FeedbackManager.error_exception(error=str(e)))
            return

        click.echo(FeedbackManager.success_auth())
    else:
        config = None
        try:
            config_file = Path(os.getcwd()) / ".tinyb"
            config = json.loads(open(config_file).read())
            ctx.obj['client'] = TinyB(config['token'], config.get('host', DEFAULT_HOST), version=VERSION)
            ctx.obj['config'] = config
        except Exception:
            pass

        if not config or not config['token']:
            click.echo(FeedbackManager.error_wrong_config_file(config_file=config_file))
            return


@auth.command(name="ls")
@click.option('--workspace', '--ws', default='all', help="Optional. Filter by workspace id, or use 'current' to list the workspace your currently logged in")
@click.pass_context
def auth_ls(ctx, workspace):
    """Prints your local config:\n
        - tb auth ls\n
        - tb auth ls --workspace all\n
        - tb auth ls --workspace current\n
        - tb auth ls --workspace <workspace_id>\n
    """
    config_file = Path(os.getcwd()) / ".tinyb"

    try:
        config = json.loads(open(config_file).read())
        workspaces = config['workspaces'] if 'workspaces' in config else []
        columns = ['idx', 'name', 'id', 'host', 'is_current']

        if workspace == 'current':
            try:
                idx, current_workspace = next((idx, w) for idx, w in enumerate(workspaces) if w['id'] == config['id'])
            except Exception:
                click.echo(FeedbackManager.error_auth())
                return

            table = [(
                idx,
                current_workspace['name'],
                current_workspace['id'],
                current_workspace['host'],
                True,  # is_current
            )]

            click.echo(humanfriendly.tables.format_smart_table(table, column_names=columns))
            return

        if workspace == 'all':
            table = []

            for idx, workspace in enumerate(workspaces):
                table.append((
                    idx,
                    workspace['name'],
                    workspace['id'],
                    workspace['host'],
                    workspace['token'] == config['token']
                ))
            click.echo(humanfriendly.tables.format_smart_table(table, column_names=columns))
            return

        if len(workspace) >= MIN_WORKSPACE_ID_LENGTH:
            try:
                idx, workspace = next((idx, w) for idx, w in enumerate(workspaces) if w['id'] == workspace)
            except Exception:
                click.echo(FeedbackManager.error_workspace_not_in_local_config(workspace=workspace))
                return
        else:
            idx = int(workspace)
            workspace = workspaces[idx]
        if workspace:
            table = [(
                idx,
                workspace['name'],
                workspace['id'],
                workspace['host'],
                workspace['token'] == config['token']
            )]
            click.echo(humanfriendly.tables.format_smart_table(table, column_names=columns))
            return

        click.echo(FeedbackManager.error_workspace_not_in_local_config(workspace=workspace))
    except Exception as e:
        click.echo(FeedbackManager.error_exception(error=str(e)))


@auth.command(name="add")
@click.option('--workspace', '--ws', help="Workspace id to be added to your local config")
@click.option('--host', envvar='TB_HOST', help="Optional. Set custom host if it's different than https://api.tinybird.co")
@click.option('--token', help="Optional. Set custom token to this workspace if it's different than the one you're using in your current config")
@click.pass_context
@coro
async def auth_add(ctx, workspace, host, token):
    """Add the authentication config of a particular workspace to be able to switch between workspaces
    """

    host = host or ctx.obj['config']['host']
    token = token or ctx.obj['config']['token']
    client = TinyB(token, host, version=VERSION)
    new_workspace = None

    try:
        new_workspace = await client.workspace(workspace_id=workspace, with_token=True)
    except Exception as e:
        click.echo(FeedbackManager.error_exception(error=str(e)))
        return

    config_file = Path(os.getcwd()) / ".tinyb"

    try:
        config = json.loads(open(config_file).read()) or {}
        workspaces = config['workspaces'] if 'workspaces' in config else []
        workspaces = [w for w in workspaces if w['id'] != new_workspace['id']]

        workspaces.append({
            'id': new_workspace['id'],
            'name': new_workspace['name'],
            'token': new_workspace['token'],
            'host': host
        })

        config['workspaces'] = workspaces

        open(config_file, 'w').write(json.dumps(config))
    except Exception:
        click.echo(FeedbackManager.error_file_config(config_file=config_file))
        return

    click.echo(FeedbackManager.success_auth_added())


@auth.command(name="rm")
@click.option('--workspace', '--ws', help="Workspace id to be removed from your local config")
@click.pass_context
def auth_rm(ctx, workspace):
    """Removes a workspace from your local config
    """

    config_file = Path(os.getcwd()) / ".tinyb"
    config = {}

    try:
        config = json.loads(open(config_file).read())
        workspaces = config['workspaces'] if 'workspaces' in config else []

        if len(workspace) >= MIN_WORKSPACE_ID_LENGTH:
            config['workspaces'] = [w for w in workspaces if w['id'] != workspace]
        else:
            idx = int(workspace)
            del workspaces[idx]
            config['workspaces'] = workspaces

        open(config_file, 'w').write(json.dumps(config))
        click.echo(FeedbackManager.success_auth_removed())

    except Exception as e:
        click.echo(FeedbackManager.error_exception(error=str(e)))


@auth.command(name="use")
@click.option('--workspace', '--ws', help="Workspace id to be authenticated against")
@click.pass_context
@coro
async def auth_use(ctx, workspace):
    """Authenticates to a workspace from your local config. Use 'tb workspaces show all' to list the workspaces you've added
    """

    config_file = Path(os.getcwd()) / ".tinyb"
    config = {}

    try:
        config = json.loads(open(config_file).read())
        workspaces = config['workspaces'] if 'workspaces' in config else []

        if len(workspace) >= MIN_WORKSPACE_ID_LENGTH:
            try:
                idx, workspace_config = next((idx, w) for idx, w in enumerate(workspaces) if w['id'] == workspace)
            except Exception:
                click.echo(FeedbackManager.error_workspace_not_in_local_config(workspace=workspace))
                return
        else:
            idx = int(workspace)
            workspace_config = workspaces[idx]

        if workspace_config:
            client = TinyB(workspace_config['token'], workspace_config['host'], version=VERSION)
            use_workspace = await client.workspace(workspace_id=workspace_config['id'], with_token=True)

            config['id'] = use_workspace['id']
            config['name'] = use_workspace['name']
            config['token'] = use_workspace['token']
            config['host'] = workspace_config['host']

            ctx.obj['client'] = client
            ctx.obj['config'] = config

            open(config_file, 'w').write(json.dumps(config))
            click.echo(FeedbackManager.success_now_using_config(name=config['name'], id=config['id']))
        else:
            click.echo(FeedbackManager.error_workspace_not_in_local_config(workspace=workspace))
    except Exception as e:
        click.echo(FeedbackManager.error_exception(error=str(e)))
        return


@cli.group()
@click.pass_context
def workspace(ctx):
    '''Workspace commands'''


@workspace.command(name="ls")
@click.pass_context
@coro
async def workspace_ls(ctx):
    """List all the workspaces you have access to in the account you're currently authenticated to
    """

    client = ctx.obj['client']
    response = await client.workspaces()

    columns = ['name', 'id', 'role', 'plan']
    table = []

    for workspace in response['workspaces']:
        table.append([workspace['name'], workspace['id'], workspace['role'], workspace['plan']])

    print(humanfriendly.tables.format_smart_table(table, column_names=columns))


@cli.group()
@click.pass_context
def datasource(ctx):
    '''Data sources commands'''


@datasource.command(name="ls")
@click.option('--prefix', default=None, help="Show only resources with this prefix")
@click.option('--match', default=None, help='Retrieve any resources matching the pattern. eg --match _test')
@click.pass_context
@coro
async def datasource_ls(ctx, prefix, match):
    """List data sources"""
    client = ctx.obj['client']
    ds = await client.datasources()
    columns = ['prefix', 'version', 'name', 'row_count', 'size', 'created at', 'updated at']
    click.echo(FeedbackManager.info_datasources())
    table = []
    pattern = re.compile(match) if match else None
    for t in ds:
        stats = t.get('stats', None)
        if not stats:
            stats = t.get('statistics', {'bytes': ''})
            if not stats:
                stats = {'bytes': ''}

        tk = get_name_tag_version(t['name'])
        if (prefix and tk['tag'] != prefix) or (pattern and not pattern.search(tk['name'])):
            continue
        table.append((
            tk['tag'] or '',
            tk['version'] if tk['version'] is not None else '',
            tk['name'],
            humanfriendly.format_number(stats.get('row_count')) if 'row_count' in stats else '-',
            humanfriendly.format_size(int(stats.get('bytes'))) if stats.get('bytes', None) else '-',
            t['created_at'][:-7],
            t['updated_at'][:-7])
        )

    click.echo(humanfriendly.tables.format_smart_table(table, column_names=columns))
    click.echo('\n')


async def push_data(ctx, datasource_name, url, connector, sql, mode='append', sql_condition=None):
    if url and type(url) is tuple:
        url = url[0]
    client = ctx.obj['client']

    if connector:
        load_connector_config(ctx, connector, False, check_uninstalled=False)
        if connector not in ctx.obj:
            click.echo(FeedbackManager.error_connector_not_configured(connector=connector))
            return
        else:
            _connector = ctx.obj[connector]
            click.echo(FeedbackManager.info_starting_export_process(connector=connector))
            url = _connector.export_to_gcs(sql, datasource_name)

    def cb(res):
        if cb.First:
            blocks_to_process = len([x for x in res['block_log'] if x['status'] == 'idle'])
            if blocks_to_process:
                cb.bar = click.progressbar(label=FeedbackManager.info_progress_blocks(), length=blocks_to_process)
                cb.bar.update(0)
                cb.First = False
                cb.blocks_to_process = blocks_to_process
        else:
            done = len([x for x in res['block_log'] if x['status'] == 'done'])
            if done * 2 > cb.blocks_to_process:
                cb.bar.label = FeedbackManager.info_progress_current_blocks()
            cb.bar.update(done - cb.prev_done)
            cb.prev_done = done
    cb.First = True
    cb.prev_done = 0

    try:
        click.echo(FeedbackManager.info_starting_import_process())
        parsed = urlparse(url)
        if parsed.scheme in ('http', 'https'):
            url = quote(url)
            res = await client.datasource_create_from_url(datasource_name, url, mode=mode, status_callback=cb, sql_condition=sql_condition)
        else:
            res = await client.datasource_append_data(datasource_name, open(url, mode='rb'), mode=mode, sql_condition=sql_condition)

        total_rows = (res.get('datasource', {}).get('statistics', {}) or {}).get('row_count', 0)
        appended_rows = 0
        datasource_name = res['datasource']['name']
        parser = None

        if 'error' in res and res['error']:
            click.echo(FeedbackManager.error_exception(error=res['error']))
        if 'errors' in res and res['errors']:
            click.echo(FeedbackManager.error_exception(error=res['errors']))
        if 'blocks' in res and res['blocks']:
            for block in res['blocks']:
                process_return = block['process_return'][0]
                parser = process_return['parser'] if 'parser' in process_return and process_return['parser'] else parser
                if parser and parser != 'clickhouse':
                    parser = process_return['parser']
                    appended_rows += process_return['lines']

        click.echo(FeedbackManager.success_progress_blocks())

        if mode == 'append':
            if parser != 'clickhouse':
                click.echo(FeedbackManager.success_appended_rows(appended_rows=appended_rows))

        click.echo(FeedbackManager.success_total_rows(datasource=datasource_name, total_rows=total_rows))

        if mode == 'replace':
            click.echo(FeedbackManager.success_replaced_datasource(datasource=datasource_name))
        else:
            click.echo(FeedbackManager.success_appended_datasource(datasource=datasource_name))
        click.echo(FeedbackManager.info_data_pushed(datasource=datasource_name))
    except Exception as e:
        click.echo(FeedbackManager.error_exception(error=e))


@datasource.command(name="append")
@click.argument('datasource_name')
@click.argument('url', nargs=-1)
@click.option('--connector', type=click.Choice(['bigquery', 'snowflake'], case_sensitive=True), help="Import from one of the selected connectors")
@click.option('--sql', default=None, help='Query to extract data from one of the SQL connectors')
@click.option('--incremental', default=None, help='It does an incremental append, taking the max value for the date column name provided as a parameter. It only works when the `connector` parameter is passed.')
@click.pass_context
@coro
async def datasource_append(ctx, datasource_name, url, connector, sql, incremental):
    """
        Create a data source from a URL, local file or a connector

        - Load from URL `tb datasource append [datasource_name] https://url_to_csv`

        - Load from local file `tb datasource append [datasource_name] /path/to/local/file`

        - Load from connector `tb datasource append [datasource_name] --connector [connector_name] --sql [the_sql_to_extract_from]`
    """
    if incremental and not connector:
        click.echo(FeedbackManager.error_incremental_not_supported())
        return

    if incremental:
        date = None
        source_column = incremental.split(':')[0]
        dest_column = incremental.split(':')[-1]
        result = await ctx.obj['client'].query(f'SELECT max({dest_column}) as inc from {datasource_name} FORMAT JSON')
        try:
            date = result['data'][0]['inc']
        except Exception as e:
            raise click.ClickException(f'{str(e)}')
        if date:
            sql = f"{sql} WHERE {source_column} > '{date}'"
    await push_data(ctx, datasource_name, url, connector, sql, mode='append')


@datasource.command(name="replace")
@click.argument('datasource_name')
@click.argument('url', nargs=-1)
@click.option('--connector', type=click.Choice(['bigquery', 'snowflake'], case_sensitive=True), help="Import from one of the selected connectors")
@click.option('--sql', default=None, help='Query to extract data from one of the SQL connectors')
@click.option('--sql-condition', default=None, help='SQL WHERE condition to replace data')
@click.pass_context
@coro
async def datasource_replace(ctx, datasource_name, url, connector, sql, sql_condition):
    """
        Replaces the data in a data source from a URL, local file or a connector

        - Replace from URL `tb datasource replace [datasource_name] https://url_to_csv --sql_condition "country='ES'"`

        - Replace from local file `tb datasource replace [datasource_name] /path/to/local/file --sql_condition "country='ES'"`

        - Replace from connector `tb datasource replace [datasource_name] --connector [connector_name] --sql [the_sql_to_extract_from] --sql_condition "country='ES'"`
    """
    await push_data(ctx, datasource_name, url, connector, sql, mode='replace', sql_condition=sql_condition)


@datasource.command(name='analyze')
@click.argument('url_or_file')
@click.pass_context
@coro
async def datasource_analyze(ctx, url_or_file):
    '''Analyze a URL or a file before creating a new data source'''
    client = ctx.obj['client']

    def _table(title, columns, data):
        row_format = "{:<25}" * len(columns)
        click.echo(FeedbackManager.info_datasource_title(title=title))
        click.echo(FeedbackManager.info_datasource_row(row=row_format.format(*columns)))
        for t in data:
            click.echo(FeedbackManager.info_datasource_row(row=row_format.format(*t)))

    parsed = urlparse(url_or_file)

    if parsed.scheme in ('http', 'https'):
        analysis = await client.datasource_analyze(url_or_file)
    else:
        data = open(url_or_file).read(1024 * 1024)
        analysis = await client.datasource_analyze_file(data.encode())

    columns = ('name', 'type', 'nullable')
    _table('columns', columns, [(t['name'], t['type'], 'true' if t['nullable'] else 'false') for t in analysis['schema']])

    click.echo(FeedbackManager.info_datasource_title(title='SQL Schema'))
    click.echo(analysis['sql_schema'])

    values = []

    for x in analysis['dialect'].items():
        click.echo(x)
        if x[1] == ' ':
            values.append((x[0], '" "'))
        elif type(x[1]) == str and ('\n' in x[1] or '\r' in x[1]):
            values.append((x[0], x[1].replace('\n', '\\n'). replace('\r', '\\r')))
        else:
            values.append(x)

    _table('dialect', ('name', 'value'), values)


@datasource.command(name="rm")
@click.argument('datasource_name')
@click.option('--yes', is_flag=True, default=False, help="Do not ask for confirmation")
@click.pass_context
@coro
async def datasource_delete(ctx, datasource_name, yes):
    """Delete a data source"""
    client = ctx.obj['client']
    if yes or click.confirm(FeedbackManager.warning_confirm_delete_datasource(datasource=datasource_name)):
        try:
            await client.datasource_delete(datasource_name)
        except DoesNotExistException:
            raise click.ClickException(FeedbackManager.error_datasource_does_not_exist(datasource=datasource_name))
        except CanNotBeDeletedException as e:
            raise click.ClickException(FeedbackManager.error_datasource_can_not_be_deleted(datasource=datasource_name, error=e))
        except Exception as e:
            raise click.ClickException(FeedbackManager.error_exception(error=e))

        click.echo(FeedbackManager.success_delete_datasource(datasource=datasource_name))


@datasource.command(name="truncate")
@click.argument('datasource_name')
@click.option('--yes', is_flag=True, default=False, help="Do not ask for confirmation")
@click.pass_context
@coro
async def datasource_truncate(ctx, datasource_name, yes):
    """Truncate a data source"""

    client = ctx.obj['client']
    if yes or click.confirm(FeedbackManager.warning_confirm_truncate_datasource(datasource=datasource_name)):
        try:
            await client.datasource_truncate(datasource_name)
        except DoesNotExistException:
            raise click.ClickException(FeedbackManager.error_datasource_does_not_exist(datasource=datasource_name))
        except Exception as e:
            raise click.ClickException(FeedbackManager.error_exception(error=e))

        click.echo(FeedbackManager.success_truncate_datasource(datasource=datasource_name))


@datasource.command(name="generate", short_help="Generates a data source file based on a sample CSV file from local disk or url")
@click.argument('filenames', nargs=-1, default=None)
@click.option('--type-guessing', is_flag=True, default=True, help="When using ``false`` all columns are created as ``String`` otherwise it tries to guess the column types based on the CSV contents")
@click.option('--force', is_flag=True, default=False, help="Override existing files")
@click.pass_context
@coro
async def generate_datasource(ctx, filenames, type_guessing, force):
    """Generate a data source file based on a sample CSV file from local disk or url"""
    client = ctx.obj['client']

    for filename in filenames:
        data = None
        parsed = urlparse(filename)
        if parsed.scheme in ('http', 'https'):
            meta = await client.datasource_analyze(filename, type_guessing=type_guessing)
        else:
            data = open(filename).read(1024 * 1024)
            meta = await client.datasource_analyze_file(data.encode(), type_guessing=type_guessing)
        schema = meta['sql_schema'].replace(', ', ',\n    ')
        datafile = f"""DESCRIPTION generated from {filename}\n\nSCHEMA >\n    {schema}"""
        generate_datafile(datafile, filename, data, force)


@cli.command()
@click.argument('query')
@click.option('--rows_limit', default=100, help="Max number of rows retrieved")
@click.option('--format', 'format_', type=click.Choice(['json', 'csv', 'human'], case_sensitive=False), default='human', help="Output format")
@click.option('--stats/--no-stats', default=False, help="Show query stats")
@click.pass_context
@coro
async def sql(ctx, query, rows_limit, format_, stats):
    """Run SQL query over data sources and pipes"""
    client = ctx.obj['client']
    q = query.lower().strip()
    if q.startswith('insert'):
        click.echo(FeedbackManager.error_invalid_query())
        click.echo(FeedbackManager.info_append_data())
        return
    if q.startswith('delete'):
        click.echo(FeedbackManager.error_invalid_query())
        return

    req_format = 'CSVWithNames' if format_ == 'csv' else 'JSON'
    try:
        res = await client.query(f'SELECT * FROM ({query}) LIMIT {rows_limit} FORMAT {req_format}')
    except Exception as e:
        click.echo(FeedbackManager.error_exception(error=str(e)))
        return
    req_format = 'CSVWithNames' if format_ == 'csv' else 'JSON'
    parsed_query = f'SELECT * FROM ({query}) LIMIT {rows_limit} FORMAT {req_format}'
    res = await client.query(parsed_query)

    if 'error' in res:
        click.echo(FeedbackManager.error_exception(error=res['error']))
        return

    if stats:
        stats_query = f'SELECT * FROM ({query}) LIMIT {rows_limit} FORMAT JSON'
        stats_res = await client.query(stats_query)
        stats = stats_res['statistics']
        seconds = stats['elapsed']
        rows_read = humanfriendly.format_number(stats['rows_read'])
        bytes_read = humanfriendly.format_size(stats['bytes_read'])
        click.echo(FeedbackManager.info_query_stats(seconds=seconds, rows=rows_read, bytes=bytes_read))

    if format_ == 'csv':
        print(res)
    elif 'data' in res and res['data']:
        if format_ == 'json':
            print(json.dumps(res, indent=8))
        else:
            dd = []
            for d in res['data']:
                dd.append(d.values())
            click.echo(humanfriendly.tables.format_smart_table(dd, column_names=res['data'][0].keys()))
    else:
        click.echo(FeedbackManager.info_no_rows())


@cli.group()
@click.pass_context
def pipe(ctx):
    '''Pipes commands'''


@pipe.command(name="generate", short_help="Generates a pipe file based on a sql query")
@click.argument('name')
@click.argument('query')
@click.option('--force', is_flag=True, default=False, help="Override existing files")
@click.pass_context
def generate_pipe(ctx, name, query, force):
    pipefile = f"""
NODE endpoint
DESCRIPTION >
    Generated from the command line
SQL >
    {query}

    """
    base = Path('endpoints')
    if not base.exists():
        base = Path()
    f = base / (f"{name}.pipe")
    if not f.exists() or force:
        open(f'{f}', 'w').write(pipefile)
        click.echo(FeedbackManager.success_generated_pipe(file=f))
    else:
        click.echo(FeedbackManager.error_exception(file=f))


@pipe.command(name="stats")
@click.argument('pipe', nargs=-1)
@click.pass_context
@coro
async def pipe_stats(ctx, pipe):
    """Print pipe stats"""
    client = ctx.obj['client']
    pipes = await client.pipes()
    pipes_to_get_stats = []
    pipes_ids = {}
    for pipe in pipes:
        name_tag = get_name_tag_version(pipe['name'])
        if name_tag['name'] in pipe['name']:
            pipes_to_get_stats.append(f"'{pipe['id']}'")
            pipes_ids[pipe['id']] = name_tag

    if not pipes_to_get_stats:
        click.echo(FeedbackManager.info_no_pipes_stats())
        return

    sql = f"""
        SELECT
            pipe_id id,
            sumIf(view_count, date > now() - interval 7 day) requests,
            sumIf(view_count, date > now() - interval 14 day and date < now() - interval 7 day) prev_requests,
            sumIf(error_count, date > now() - interval 7 day) errors,
            sumIf(error_count, date > now() - interval 14 day and date < now() - interval 7 day) prev_errors,
            avgMergeIf(avg_duration_state, date > now() - interval 7 day) latency,
            avgMergeIf(avg_duration_state, date > now() - interval 14 day and date < now() - interval 7 day) prev_latency
        FROM tinybird.pipe_stats
        where pipe_id in ({','.join(pipes_to_get_stats)})
        GROUP BY pipe_id
        ORDER BY requests DESC
        FORMAT JSON
    """

    columns = ['prefix', 'version', 'name', 'request count', 'error count', 'avg latency']
    res = await client.query(sql)
    table = []

    if res and 'error' in res:
        click.echo(FeedbackManager.error_exception(error=str(res['error'])))
        return

    if res and 'data' in res:
        for x in res['data']:
            tk = pipes_ids[x['id']]
            table.append((
                tk['tag'] or '',
                tk['version'] if tk['version'] is not None else '',
                tk['name'],
                x['requests'],
                x['errors'],
                x['latency']
            ))

        table.sort(key=lambda x: (x[2], x[1]))
        click.echo(humanfriendly.tables.format_smart_table(table, column_names=columns))


@pipe.command(name="ls")
@click.option('--prefix', default=None, help="Show only resources with this prefix")
@click.option('--match', default=None, help='Retrieve any resourcing matching the pattern. eg --match _test')
@click.pass_context
@coro
async def pipe_ls(ctx, prefix, match):
    """List pipes"""
    client = ctx.obj['client']
    ds = await client.pipes()
    columns = ['prefix', 'version', 'name', 'published date', 'nodes']
    click.echo(FeedbackManager.info_pipes())
    table = []
    pattern = re.compile(match) if match else None
    for t in ds:
        tk = get_name_tag_version(t['name'])
        click.echo(FeedbackManager.info_pipe_name(pipe=t['name']))
        if (prefix and tk['tag'] != prefix) or (pattern and not pattern.search(tk['name'])):
            continue
        table.append((
            tk['tag'] or '',
            tk['version'] if tk['version'] is not None else '',
            tk['name'],
            t['created_at'][:-7],
            len(t['nodes'])
        ))

    click.echo(humanfriendly.tables.format_smart_table(table, column_names=columns))
    click.echo('\n')


@pipe.command(name="new")
@click.argument('pipe_name')
@click.argument('sql')
@click.pass_context
@coro
async def pipe_create(ctx, pipe_name, sql):
    """Create a new pipe"""
    client = ctx.obj['client']
    host = ctx.obj['config'].get('host', DEFAULT_HOST)
    res = await client.pipe_create(pipe_name, sql)
    click.echo(FeedbackManager.success_created_pipe(pipe=pipe_name, node_id=res['nodes'][0]['id'], host=host))


@pipe.command(name="append")
@click.argument('pipe_name_or_uid')
@click.argument('sql')
@click.pass_context
@coro
async def pipe_append_node(ctx, pipe_name_or_uid, sql):
    """Append a node to a pipe"""
    client = ctx.obj['client']
    res = await client.pipe_append_node(pipe_name_or_uid, sql)
    click.echo(FeedbackManager.success_node_changed(node_id=res['id']))


@pipe.command(name="set_endpoint")
@click.argument('pipe_name_or_id')
@click.argument('node_uid', default=None, required=False)
@click.pass_context
@coro
async def pipe_published_node(ctx, pipe_name_or_id, node_uid=None):
    """Change the published node of a pipe"""
    client = ctx.obj['client']
    host = ctx.obj['config'].get('host', DEFAULT_HOST)

    try:
        pipe = await client.pipe(pipe_name_or_id)
        if not node_uid:
            node = pipe['nodes'][-1]['name']
            click.echo(FeedbackManager.info_using_node(node=node))
        else:
            node = node_uid

        res = await client.pipe_set_endpoint(pipe_name_or_id, node)
        click.echo(FeedbackManager.success_node_published(node_id=res['id'], pipe=pipe_name_or_id, host=host))
    except DoesNotExistException:
        raise click.ClickException(FeedbackManager.error_pipe_does_not_exist(pipe=pipe_name_or_id))


@pipe.command(name="rm")
@click.argument('pipe_name_or_id')
@click.option('--yes', is_flag=True, default=False, help="Do not ask for confirmation")
@click.pass_context
@coro
async def pipe_delete(ctx, pipe_name_or_id, yes):
    """Delete a pipe"""

    client = ctx.obj['client']

    if yes or click.confirm(FeedbackManager.warning_confirm_delete_pipe(pipe=pipe_name_or_id)):
        try:
            await client.pipe_delete(pipe_name_or_id)
        except DoesNotExistException:
            raise click.ClickException(FeedbackManager.error_pipe_does_not_exist(pipe=pipe_name_or_id))

        click.echo(FeedbackManager.success_delete_pipe(pipe=pipe_name_or_id))


@pipe.command(name="token_read")
@click.argument('pipe_name')
@click.pass_context
@coro
async def pipe_token_read(ctx, pipe_name):
    """Retrieve a token to read a pipe"""
    client = ctx.obj['client']

    try:
        await client.pipe_file(pipe_name)
    except DoesNotExistException:
        raise click.ClickException(FeedbackManager.error_pipe_does_not_exist(pipe=pipe_name))

    tokens = await client.tokens()
    token = None

    for t in tokens:
        for scope in t['scopes']:
            if scope['type'] == 'PIPES:READ' and scope['resource'] == pipe_name:
                token = t['token']
    if token:
        click.echo(token)
    else:
        click.echo(FeedbackManager.warning_token_pipe(pipe=pipe_name))


@pipe.command(name="data", context_settings=dict(
    allow_extra_args=True,
    ignore_unknown_options=True,
))
@click.argument('pipe')
@click.option('--query', default=None, help="Run SQL over pipe results")
@click.option('--format', 'format_', type=click.Choice(['json', 'csv'], case_sensitive=False), default='json', help="Return format (CSV, JSON)")
@click.pass_context
def print_pipe(ctx, pipe, query, format_):
    """Print data returned by a pipe"""

    token = ctx.obj['config'].get('token')
    host = ctx.obj['config'].get('host', DEFAULT_HOST)
    params = {ctx.args[i][2:]: ctx.args[i + 1] for i in range(0, len(ctx.args), 2)}
    headers = {'Authorization': f'Bearer {token}'}
    req_format = 'json' if not format_ else format_.lower()
    if query:
        params['q'] = query
    params['cli_version'] = VERSION
    r = requests.get(f"{host}/v0/pipes/{pipe}.{req_format}?{urlencode(params)}", headers=headers)
    if r.status_code != 200:
        click.echo(FeedbackManager.error_exception(error=r.json()['error']))
        return
    if not format_:
        res = r.json()

        stats = res['statistics']
        seconds = stats['elapsed']
        rows_read = humanfriendly.format_number(stats['rows_read'])
        bytes_read = humanfriendly.format_size(stats['bytes_read'])

        click.echo(FeedbackManager.success_print_pipe(pipe=pipe))
        click.echo(FeedbackManager.info_query_stats(seconds=seconds, rows=rows_read, bytes=bytes_read))
        print_data_table(res)
        click.echo('\n')
    else:
        click.echo(r.content.decode())


@cli.command(short_help="Drop all the resources inside a project with prefix. This command is dangerous because it removes everything, use with care")  # noqa: C901
@click.argument('prefix')
@click.option('--yes', is_flag=True, default=False, help="Do not ask for confirmation")
@click.option('--dry-run', is_flag=True, default=False, help="Run the command without removing anything")
@click.pass_context
@coro
async def drop_prefix(ctx, prefix, yes, dry_run):  # noqa: C901
    """Drop all the resources inside a project with prefix. This command is dangerous because it removes everything, use with care"""

    if yes or click.confirm(FeedbackManager.warning_confirm_drop_prefix(prefix=prefix)):
        host = ctx.obj['config'].get('host', DEFAULT_HOST)
        token = ctx.obj['config'].get('token')
        tables_helper = TablesHelper(host, token)

        filenames = get_project_filenames(os.getcwd())
        resources, dep_map = build_graph(filenames, process_dependencies=True, tables_helper=tables_helper)
        names = [r['resource_name'] for r in resources.values()]
        res = {}
        client = ctx.obj['client']

        ds = await client.pipes()
        for t in ds:
            tk = get_name_tag_version(t['name'])
            if tk['tag'] == prefix and tk['name'] in names:
                res[tk['name']] = t['name']

        for group in reversed(list(toposort(dep_map))):
            for name in group:
                if name in res:
                    if resources[name]['resource'] == 'datasources':
                        if not dry_run:
                            click.echo(FeedbackManager.info_removing_datasource(datasource=res[name]))
                            try:
                                await client.datasource_delete(res[name])
                            except DoesNotExistException:
                                click.echo(FeedbackManager.info_removing_datasource_not_found(datasource=res[name]))
                            except CanNotBeDeletedException as e:
                                click.echo(FeedbackManager.error_datasource_can_not_be_deleted(datasource=res[name], error=e))
                            except Exception as e:
                                raise click.ClickException(FeedbackManager.error_exception(error=e))
                        else:
                            click.echo(FeedbackManager.info_dry_removing_datasource(datasource=res[name]))
                    else:
                        if not dry_run:
                            click.echo(FeedbackManager.info_removing_pipe(pipe=res[name]))
                            try:
                                await client.pipe_delete(res[name])
                            except DoesNotExistException:
                                click.echo(FeedbackManager.info_removing_pipe_not_found(pipe=res[name]))
                        else:
                            click.echo(FeedbackManager.info_dry_removing_pipe(pipe=res[name]))

        ds = await client.datasources()
        for t in ds:
            tk = get_name_tag_version(t['name'])
            if tk['tag'] == prefix and tk['name'] in names:
                res[tk['name']] = t['name']
                if not dry_run:
                    click.echo(FeedbackManager.info_removing_datasource(datasource=t['name']))
                    try:
                        await client.datasource_delete(t['name'])
                    except DoesNotExistException:
                        click.echo(FeedbackManager.info_removing_datasource_not_found(datasource=t['name']))
                    except CanNotBeDeletedException as e:
                        click.echo(FeedbackManager.error_datasource_can_not_be_deleted(datasource=t['name'], error=e))
                    except Exception as e:
                        raise click.ClickException(FeedbackManager.error_exception(error=e))
                else:
                    click.echo(FeedbackManager.info_dry_removing_datasource(datasource=t['name']))


@cli.group()
@click.pass_context
def job(ctx):
    '''Jobs commands'''


@job.command(name="ls")
@click.option('-s', '--status', help="Show only jobs with this status",
              type=click.Choice(['waiting', 'working', 'done', 'error'], case_sensitive=False),
              multiple=True, default=None)
@click.pass_context
@coro
async def jobs_ls(ctx, status):
    """List jobs"""
    client = ctx.obj['client']
    jobs = await client.jobs(status=status)
    columns = ['id', 'kind', 'status', 'created at', 'updated at', 'job url']
    click.echo(FeedbackManager.info_jobs())
    table = []
    for j in jobs:
        table.append([j[c.replace(' ', '_')] for c in columns])
    click.echo(humanfriendly.tables.format_smart_table(table, column_names=columns))
    click.echo('\n')


@job.command(name="details")
@click.argument('job_id')
@click.pass_context
@coro
async def job_details(ctx, job_id):
    """Get details for a job"""
    client = ctx.obj['client']
    job = await client.job(job_id)
    columns = []
    click.echo(FeedbackManager.info_job(job=job_id))
    table = []
    columns = job.keys()
    table = [job.values()]
    click.echo(humanfriendly.tables.format_smart_table(table, column_names=columns))
    click.echo('\n')


@job.command(name="cancel")
@click.argument('job_id')
@click.pass_context
@coro
async def job_cancel(ctx, job_id):
    """Try to cancel a Job"""
    client = ctx.obj['client']
    try:
        result = await client.job_cancel(job_id)
    except DoesNotExistException:
        click.echo(FeedbackManager.error_job_does_not_exist(job_id=job_id))
    except Exception as e:
        click.echo(FeedbackManager.error_exception(error=e))
    else:
        current_job_status = result['status']
        if current_job_status == 'cancelling':
            click.echo(FeedbackManager.success_job_cancellation_cancelling(job_id=job_id))
        elif current_job_status == 'cancelled':
            click.echo(FeedbackManager.success_job_cancellation_cancelled(job_id=job_id))
        else:
            click.echo(FeedbackManager.error_job_cancelled_but_status_unknown(job_id=job_id))
    click.echo('\n')


if __name__ == '__main__':
    cli()
