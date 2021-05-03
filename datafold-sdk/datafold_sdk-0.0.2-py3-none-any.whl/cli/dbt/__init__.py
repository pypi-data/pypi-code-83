import logging
import os

import click

from datafold.sdk.dbt import submit_artifacts

logger = logging.getLogger(__file__)


@click.group()
@click.pass_context
def manager(ctx):
    """DBT integration with Datafold"""


@manager.command()
@click.option('--ci-config-id',
              help="The ID of the CI config in Datafold (see CI settings screen)",
              type=int,
              required=True)
@click.option('--run-type',
              help="Submit the manifest as either 'production' or 'pull_request'",
              type=str,
              required=True)
@click.option('--target-folder',
              help="Path to the target folder of the dbt run",
              required=True,
              type=click.Path(exists=True))
@click.option('--commit-sha',
              help="Override the commit sha",
              type=str,
              required=False)
@click.pass_context
def upload(ctx, ci_config_id: int, run_type: str, target_folder, commit_sha: str = None):
    """Uploads the artefacts of a dbt run."""
    submit_artifacts(host=ctx.obj.host,
                     api_key=ctx.obj.api_key,
                     ci_config_id=ci_config_id,
                     run_type=run_type,
                     target_folder=click.format_filename(target_folder),
                     commit_sha=commit_sha)
