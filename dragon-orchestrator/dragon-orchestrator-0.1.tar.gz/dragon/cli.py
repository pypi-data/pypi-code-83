import logging
import os

import docker
import requests

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


def check_docker() -> bool:
    try:
        docker.from_env()
        return True
    except Exception:
        return False


def validate_instance() -> int:
    """
    Run all the checks on the instance
    """

    checks = {"Docker": check_docker}
    failed = 0

    for name, checker in checks.items():
        status = checker()
        if not status:
            logging.info(name + " X")
            failed += 1
        else:
            logging.info(name)

    return failed


def register_client():
    """
    Register this machine as a client in orchestrator server.
    """
    server_address = os.environ.get("SERVER_ADDRESS", "http://localhost:8000")
    try:
        logging.info("Registering as client on " + server_address)
        res = requests.get(f"{server_address}/api/clients/register/")
        if res.status_code == 400:
            logging.info("Client already registered")
        elif res.status_code != 201:
            raise Exception(
                "Something went wrong while trying to register this machine as a client"
            )
    except requests.exceptions.ConnectionError:
        raise Exception(
            f"Unable to connect to orchestrator server on {server_address}. Check the server address and try again."
        )


def run() -> None:
    logging.info("Running instance checks")
    failed = validate_instance()
    if failed > 0:
        logging.info(f"{failed} check(s) have failed")
    else:
        logging.info("Instance checks passed")
        from dragon.dragon_server import serve

        register_client()
        serve()


if __name__ == "__main__":
    run()
