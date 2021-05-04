"""Discovery."""

import os
import sys
import click
from loguru import logger

import escape_cli.utils.coverage as coverage
from escape_cli.utils.sdk import EscapeIntelligenceSDK
from escape_cli.static.constants import CONFIG_FILENAME, COVERAGE_NAMESPACE, DISCOVER_NAMESPACE, PROJECT_NAMESPACE
from escape_cli.utils.config import get_config, patch_and_run


@click.command()
@click.argument('entrypoint', nargs=-1, required=True, type=str)
@logger.catch
def discover(entrypoint: str) -> None:
    """Start a Discovery."""

    config = get_config(os.environ.get('ESCAPE_CUSTOM_CONFIG_PATH', CONFIG_FILENAME), DISCOVER_NAMESPACE)
    if not config:
        return

    project_uri = config[PROJECT_NAMESPACE]['key']
    coverage_config = config[DISCOVER_NAMESPACE].get(COVERAGE_NAMESPACE, {})

    # Create run
    logger.info('Creating run')
    client = EscapeIntelligenceSDK(project_uri)
    run = client.create_run()  # pylint: disable=no-member
    logger.info(f'Run created with uuid {run["uuid"]}')

    try:
        result = patch_and_run(' '.join(entrypoint), config)
        if not result:
            return

        coverage_data = coverage.run_coverage(result['transactions'], result['endpoints'], coverage_config)
        filtered_coverage, coverage_stats, enriched_endpoints = coverage_data

        # Send the transactions to the backend
        logger.info('Saving HTTP messages into the DB')
        client.add_transactions_to_run(run['uuid'], transactions=result['transactions'])

        logger.info('Generating OpenAPI specification')
        client.generate_run_openapi_spec(run['uuid'])

        logger.info('Saving the endpoints in the DB')
        client.add_endpoints_to_run(run['uuid'], endpoints=enriched_endpoints)

        logger.info('Saving run metadata')
        client.update_run(run['uuid'], {'status': 'success:discovery', **coverage_stats})
        coverage.display_coverage_reports(filtered_coverage, coverage_stats, coverage_config)

    # Exit nicely if coverage is failed
    except Exception as err:
        logger.error(err)
        client.update_run(run['uuid'], {'status': 'failed:discovery'})
        sys.exit(1)
