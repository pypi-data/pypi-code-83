from iamzero.identity import Identity, IdentityFetcher
from iamzero.event import Event

from iamzero.publisher import Publisher


class Client(object):
    """
    An iamzero client which is used to dispatch authentication errors to an iamzero collector
    """

    def __init__(
        self,
        token="",
        url="https://app.iamzero.dev",
        max_batch_size=100,
        send_frequency=0.25,
        block_on_send=False,
        block_on_response=False,
        transmission_impl=None,
        user_agent_addition="",
        debug=False,
    ):

        self.identity = Identity()
        self.identity_fetcher = IdentityFetcher(identity=self.identity, debug=debug)
        self.identity_fetcher.start()

        self.publisher = transmission_impl
        if self.publisher is None:
            self.publisher = Publisher(
                url=url,
                token=token,
                identity=self.identity,
                block_on_send=block_on_send,
                send_frequency=send_frequency,
                max_batch_size=max_batch_size,
                block_on_response=block_on_response,
                user_agent_addition=user_agent_addition,
                debug=debug,
            )

        self.publisher.start()
        self.token = token
        self.url = url
        self._responses = self.publisher.get_response_queue()
        self.block_on_response = block_on_response

        self.debug = debug
        if debug:
            self._init_logger()

        self.log("initialized iamzero client: token=%s, url=%s", token, url)
        if not token:
            self.log("token not set! set the token if you want to send data to iamzero")

    def _init_logger(self):
        import logging  # pylint: disable=bad-option-value,import-outside-toplevel

        self._logger = logging.getLogger("iamzero-client")
        self._logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        self._logger.addHandler(ch)

    def log(self, msg, *args, **kwargs):
        if self.debug:
            self._logger.debug(msg, *args, **kwargs)

    def responses(self):
        """Returns a queue from which you can read a record of response info from
        each event sent. Responses will be dicts with the following keys:

        - `status_code` - the HTTP response from the api (eg. 200 or 503)
        - `duration` - how long it took to POST this event to the api, in ms
        - `metadata` - pass through the metadata you added on the initial event
        - `body` - the content returned by API (will be empty on success)
        - `error` - in an error condition, this is filled with the error message

        When the Client's `close` method is called, a None will be inserted on
        the queue, indicating that no further responses will be written.
        """
        return self._responses

    def send(self, event: Event):
        """
        Enqueues the given event to be sent
        """
        if self.publisher is None:
            self.log(
                "tried to send on a closed or uninitialized iamzero client,"
                " event = %s",
                event,
            )
            return

        self.log("send enqueuing event, event = %s", event)
        self.publisher.send(event)

    def close(self):
        """Wait for in-flight events to be transmitted then shut down cleanly.
        Optional (will be called automatically at exit) unless your
        application is consuming from the responses queue and needs to know
        when all responses have been received."""

        if self.publisher:
            self.publisher.close()

        if self.identity_fetcher:
            self.identity_fetcher.close()

        # set to None so that any future sends throw errors
        self.publisher = None
        self.identity_fetcher = None

    def flush(self):
        """Closes and restarts the transmission, sending all events. Use this
        if you want to perform a blocking send of all events in your
        application.
        """
        if self.publisher and isinstance(self.publisher, Publisher):
            self.publisher.close()
            self.publisher.start()
