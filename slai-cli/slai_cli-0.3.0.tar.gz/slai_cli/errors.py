from slai_cli import log

ERROR_MAP = {
    "existing_deployments_processing": "There are existing deployments processing, please try again in a few minutes."
}


def handle_error(*, error_msg):
    log.warn(
        f"ERROR: {ERROR_MAP.get(error_msg, f'Unknown error occured: {error_msg}')}"
    )
