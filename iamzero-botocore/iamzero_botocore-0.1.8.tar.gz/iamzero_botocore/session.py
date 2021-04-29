from botocore import monitoring as botomonitoring
from . import monitor
from .logging import configure_root_logger
from .config import CONFIG
from botocore.session import Session as BaseSession

logger =  configure_root_logger(__name__)

class Session(BaseSession):
    def _register_components(self):
        super()._register_components()
        self._register_iamzero_monitor()

    def _register_iamzero_monitor(self):
        self._internal_components.lazy_register_component(
            "iamzero_monitor", self._create_iamzero_monitor
        )

    def _create_iamzero_monitor(self):
        # TODO: recreating an entire botocore Session here is likely hugely inefficient.
        # Is this executing in the main Python thread?
        # Need to profile impact on performance and then consider optimising this to
        # run in a background thread.
        logger.debug("Creating monitor")
        session = BaseSession()
        sts = session.create_client('sts')
        identity = sts.get_caller_identity()

        arn = identity['Arn']
        user_id = identity['UserId']
        account = identity['Account']

        logger.debug(f"Registered caller identity: {arn}")

        iamzero_url = CONFIG["URL"]

        handler = botomonitoring.Monitor(
            adapter=monitor.IAMZMonitorEventAdapter(),
            publisher=monitor.IAMZPublisher(
                url=iamzero_url,
                serializer=monitor.IAMZSerializer(
                    arn=arn, user_id=user_id, account=account
                ),
            ),
        )
        return handler

    def create_client(
        self,
        service_name,
        region_name=None,
        api_version=None,
        use_ssl=True,
        verify=None,
        endpoint_url=None,
        aws_access_key_id=None,
        aws_secret_access_key=None,
        aws_session_token=None,
        config=None,
    ):
        client = super().create_client(
            service_name,
            region_name=region_name,
            api_version=api_version,
            use_ssl=use_ssl,
            verify=verify,
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            config=config,
        )

        iamzero_monitor = self._get_internal_component("iamzero_monitor")
        if iamzero_monitor is not None:
            iamzero_monitor.register(client.meta.events)
        return client


def get_session(env_vars=None):
    """
    Return a new session object.
    """
    return Session(env_vars)