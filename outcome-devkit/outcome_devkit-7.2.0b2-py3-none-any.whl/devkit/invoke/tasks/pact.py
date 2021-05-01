import json
import os
from pathlib import Path

from invoke import Collection, Context, task
from outcome.utils.config import Config

from outcome.devkit.invoke import app, docker, env

defaults = {
    'PACT_BROKER_URL': 'https://pact.svc.outcome.co',
    'PACT_PROVIDERS_DIR': 'pacts',
    'PACT_FOUNDATION_CLI_IMAGE': 'pactfoundation/pact-cli:latest',
}

pact_config = Config(app.pyproject_path, defaults=defaults)

pact_broker_url = env.str_from_config('PACT_BROKER_URL', config=pact_config)
pact_providers_dir = env.str_from_config('PACT_PROVIDERS_DIR', config=pact_config)
pact_foundation_cli_image = env.str_from_config('PACT_FOUNDATION_CLI_IMAGE', config=pact_config)

pact_broker_username = env.from_os('PACT_BROKER_USERNAME')
pact_broker_password = env.from_os('PACT_BROKER_PASSWORD')
pact_github_token = env.from_os('PACT_GITHUB_TOKEN')


def pact_foundation_vars():
    return {
        'PACT_BROKER_BASE_URL': env.r(pact_broker_url),
        'PACT_BROKER_USERNAME': env.r(pact_broker_username),
        'PACT_BROKER_PASSWORD': env.r(pact_broker_password),
    }


event_pact_changed = {
    'event_type': 'pact_content_changed',
    'client_payload': {'pact_url': '${pactbroker.pactUrl}', 'consumer': '${pactbroker.consumerName}'},
}


@task
def create_webhooks_from_pacts(c: Context):  # noqa: A001, WPS125
    """Create webhooks in Pact Broker from local pact files."""
    for file in Path(env.r(pact_providers_dir)).glob('*'):
        with open(file, 'r') as handler:
            json_file = json.load(handler)
        provider_name = json_file['provider']['name']
        create_webhooks_for_provider(c, provider_name)


@task
def create_webhooks_for_provider(c: Context, provider_name: str):  # noqa: A001, WPS125
    """Create webhook in Pact Broker for a provider."""
    var_pact_github_token = env.r(pact_github_token)
    var_event_pact_changed = json.dumps(event_pact_changed)

    docker.create_container(
        c,
        f'webhook-{provider_name}',
        image=env.r(pact_foundation_cli_image),
        environment=pact_foundation_vars(),
        command='broker',
        command_args=[
            ('create-webhook', f'https://api.github.com/repos/outcome-co/{provider_name}/dispatches'),
            ('--contract-content-changed',),
            ('--provider', provider_name),
            ('-X', 'POST'),
            ('-H', 'User-Agent: PactBroker'),
            ('-H', 'Host: api.github.com'),
            ('-H', 'Content-Type: application/json'),
            ('-H', 'Accept: application/vnd.github.v3+json'),
            ('-H', f'Authorization: token ${var_pact_github_token}'),
            ('-d', f"'{var_event_pact_changed}'"),
        ],
    )


@task
def publish_as_consumer(c: Context):  # noqa: A001, WPS125
    """Publish local Pact files to Pact Broker."""
    info = app.get_app_info()
    git_info = app.get_git_info()

    if git_info is None:
        raise RuntimeError('Unable to determine version information from git')

    var_package_version = info.version
    var_pact_providers_dir = env.r(pact_providers_dir)
    var_cwd = os.getcwd()

    docker.create_container(
        c,
        f'publish-{var_package_version}',
        image=env.r(pact_foundation_cli_image),
        environment=pact_foundation_vars(),
        volumes=[(var_cwd, '/app')],
        workdir='/app',
        command='publish',
        command_args=[
            (f'/app/{var_pact_providers_dir}',),
            ('--consumer-app-version', git_info.latest_commit_hash),
            ('--tag', info.version),
            ('--tag', git_info.normalized_branch),
        ],
    )


@task
def create_version_tags(c: Context):  # noqa: A001, WPS125
    """Tag Pact with the version of the package."""
    info = app.get_app_info()
    var_cwd = os.getcwd()

    git_info = app.get_git_info()

    if git_info is None:
        raise RuntimeError('Unable to determine version information from git')

    docker.create_container(
        c,
        f'tags-{info.version}',
        image=env.r(pact_foundation_cli_image),
        environment=pact_foundation_vars(),
        volumes=[(var_cwd, '/app')],
        workdir='/app',
        command='broker',
        command_args=[
            ('create-version-tag',),
            ('--pacticipant', info.name),
            ('--version', git_info.latest_commit_hash),
            ('--tag', info.version),
            ('--tag', git_info.normalized_branch),
        ],
    )


ns = Collection(create_webhooks_from_pacts, create_webhooks_for_provider, publish_as_consumer, create_version_tags)
