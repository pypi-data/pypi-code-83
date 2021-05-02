
import time
from typing import Dict, Any

from atlas_engine_client.core.api import MessageTriggerRequest

from robot.api import logger


class SendKeyword:

    def __init__(self, client, **kwargs):
        self._client = client

    def send_message(self, message_name: str, payload: Dict[str, Any] = {}, **options):

        delay = options.get('delay', 0.2)

        if delay:
            logger.info(
                f"Send message {message_name} with seconds {delay} delay.")
            time.sleep(float(delay))

        request = MessageTriggerRequest(
            payload=payload
        )

        self._client.events_trigger_message(message_name, request)

    def send_signal(self, signal_name, **options):

        delay = options.get("delay", 0.2)

        if delay:
            logger.info(
                f"Send signal {signal_name} with {delay} seconds delay.")
            time.sleep(float(delay))

        self._client.events_trigger_signal(signal_name)
