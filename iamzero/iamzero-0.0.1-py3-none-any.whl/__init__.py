from iamzero.event import Event
from iamzero.client import Client
from iamzero.instrumentation import *
import os
import atexit
from typing import Dict, Optional

# we store the iamzero client as a global to avoid initialising
# multiple clients
_IAMZERO_CLIENT: Optional[Client] = None
_INITPID = None

WARNED_UNINITIALIZED = False


def init(token="", url="https://app.iamzero.dev", block_on_send=False, debug=False):
    global _IAMZERO_CLIENT
    global _INITPID

    pid = os.getpid()
    if _IAMZERO_CLIENT:
        if pid == _INITPID:
            _IAMZERO_CLIENT.log("iamzero is already initialised, skipping init")
            return
        else:
            _IAMZERO_CLIENT.log(
                f"iamzero already initialised, but process ID has changed (previously {_INITPID}, now {pid}"
            )
            _IAMZERO_CLIENT.close()

    _IAMZERO_CLIENT = Client(
        token=token, url=url, block_on_send=block_on_send, debug=debug
    )
    _INITPID = pid


def get_client():
    return _IAMZERO_CLIENT


def send_event(data: Dict):
    event = Event(data=data)
    client = get_client()
    if client:
        client.send(event)


def get_responses_queue():
    client = get_client()
    if client:
        return client.responses()


def _flush():
    """
    Allows iamzero to be used in shorter Python scripts which exit immediately.
    We block the main thread until any pending messages have been flushed.
    """
    client = get_client()
    if client:
        client.close()


atexit.register(_flush)
