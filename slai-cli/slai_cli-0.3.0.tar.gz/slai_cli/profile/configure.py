import click
import yaml
import os
import requests

from pathlib import Path
from slai_cli import log
from slai_cli.exceptions import InvalidApiKey
from slai.clients.cli import SlaiCliClient


def get_credentials(profile_name="default"):
    profile_name = click.prompt(
        "Profile name", type=str, show_default=True, default=profile_name
    )
    client_id = click.prompt("Client ID", type=str)
    client_secret = click.prompt("Client Secret", type=str)
    aws_profile = click.prompt("AWS profile", type=str)

    try:
        store_credentials(
            profile_name=profile_name,
            client_id=client_id,
            client_secret=client_secret,
            aws_profile=aws_profile,
        )
    except InvalidApiKey:
        log.warn("Invalid credentials.")
        return

    log.action("Credentials configured.")


def store_credentials(*, profile_name, client_id, client_secret, aws_profile):
    new_profile = {
        "client_id": client_id,
        "client_secret": client_secret,
        "aws_profile": aws_profile,
    }

    cli_client = SlaiCliClient(client_id=client_id, client_secret=client_secret)

    try:
        cli_client.get_user()
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == 401:
            raise InvalidApiKey("invalid_credentials")

    credentials_path = f"{Path.home()}/.slai"
    if not os.path.exists(credentials_path):
        os.makedirs(credentials_path)

    try:
        with open(f"{credentials_path}/credentials.yml", "r") as f_in:
            try:
                credentials = yaml.safe_load(f_in)
            except yaml.YAMLError:
                pass
    except:
        credentials = {}

    # save new profile
    credentials[profile_name] = new_profile

    with open(f"{credentials_path}/credentials.yml", "w") as f_out:
        yaml.dump(credentials, f_out, default_flow_style=False)
