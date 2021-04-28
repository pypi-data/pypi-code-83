import asyncio
import hashlib
import itertools
import json
from typing import List, Tuple
import uuid

from aiohttp.client import ClientSession
from fastapi_websocket_pubsub import PubSubClient
from fastapi_websocket_rpc.rpc_channel import RpcChannel

from opal_client.config import opal_client_config
from opal_client.data.fetcher import DataFetcher
from opal_client.data.rpc import TenantAwareRpcEventClientMethods
from opal_client.logger import logger
from opal_client.policy_store.base_policy_store_client import \
    BasePolicyStoreClient
from opal_client.policy_store.policy_store_client_factory import \
    DEFAULT_POLICY_STORE_GETTER
from opal_common.fetcher.events import FetcherConfig
from opal_common.fetcher.providers.http_fetch_provider import HttpFetcherConfig
from opal_common.schemas.data import (DataEntryReport, DataSourceConfig,
                                      DataSourceEntry, DataUpdate,
                                      DataUpdateReport)
from opal_common.utils import get_authorization_header


class DataUpdater:
    def __init__(self, token: str = None,
                 pubsub_url: str = None,
                 data_sources_config_url: str = None,
                 fetch_on_connect: bool = True,
                 data_topics: List[str] = None,
                 policy_store: BasePolicyStoreClient = None,
                 should_send_reports=None):
        """
        Keeps policy-stores (e.g. OPA) up to date with relevant data
        Obtains data configuration on startup from OPAL-server
        Uses Pub/Sub to subscribe to data update events, and fetches (using FetchingEngine) data from sources.

        Args:
            token (str, optional): Auth token to include in connections to OPAL server. Defaults to CLIENT_TOKEN.
            pubsub_url (str, optional): URL for Pub/Sub updates for data. Defaults to OPAL_SERVER_PUBSUB_URL.
            data_sources_config_url (str, optional): URL to retrive base data configuration. Defaults to DEFAULT_DATA_SOURCES_CONFIG_URL.
            fetch_on_connect (bool, optional): Should the update fetch basic data immediately upon connection/reconnection. Defaults to True.
            data_topics (List[str], optional): Topics of data to fetch and subscribe to. Defaults to DATA_TOPICS.
            policy_store (BasePolicyStoreClient, optional): Policy store client to use to store data. Defaults to DEFAULT_POLICY_STORE.
        """
        # Defaults
        token: str = token or opal_client_config.CLIENT_TOKEN
        pubsub_url: str = pubsub_url or opal_client_config.SERVER_PUBSUB_URL
        data_sources_config_url: str = data_sources_config_url or opal_client_config.DEFAULT_DATA_SOURCES_CONFIG_URL
        # Should the client use the default data source to fetch on connect
        self._fetch_on_connect = fetch_on_connect
        # The policy store we'll save data updates into
        self._policy_store = policy_store or DEFAULT_POLICY_STORE_GETTER()
        # Pub/Sub topics we subscribe to for data updates
        self._data_topics = data_topics if data_topics is not None else opal_client_config.DATA_TOPICS
        self._should_send_reports = should_send_reports if should_send_reports is not None else opal_client_config.SHOULD_REPORT_ON_DATA_UPDATES
        # The pub/sub client for data updates
        self._client = None
        # The task running the Pub/Sub subcribing client
        self._subscriber_task = None
        # Data fetcher
        self._data_fetcher = DataFetcher()
        self._token = token
        self._server_url = pubsub_url
        self._data_sources_config_url = data_sources_config_url
        if self._token is None:
            self._extra_headers = None
        else:
            self._extra_headers = [get_authorization_header(self._token)]
        self._stopping = False

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """
        Context handler to terminate internal tasks
        """
        if not self._stopping:
            await self.stop()

    async def _update_policy_data_callback(self, data: dict = None, topic=""):
        """
        Pub/Sub callback - triggering data updates
        will run when we get notifications on the policy_data topic.
        i.e: when new roles are added, changes to permissions, etc.
        """
        if data is not None:
            reason = data.get("reason", "")
        else:
            reason = "Periodic update"
        logger.info("Updating policy data, reason: {reason}", reason=reason)
        update = DataUpdate.parse_obj(data)
        self.trigger_data_update(update)

    def trigger_data_update(self, update: DataUpdate):
        # make sure the id has a unique id for tracking
        if update.id is None:
            update.id = uuid.uuid4().hex
        logger.info("Triggering data update with id: {id}", update=update, id=update.id)
        asyncio.create_task(self.update_policy_data(
            update, policy_store=self._policy_store, data_fetcher=self._data_fetcher))

    async def get_policy_data_config(self, url: str = None) -> DataSourceConfig:
        """
        Get the configuration for
        Args:
            url: the URL to query for the config, Defaults to self._data_sources_config_url
        Returns:
            DataSourceConfig: the data sources config
        """
        if url is None:
            url = self._data_sources_config_url
        logger.info("Getting data-sources configuration from '{source}'", source=url)
        try:
            async with ClientSession(headers=self._extra_headers) as session:
                res = await session.get(url)
            return DataSourceConfig.parse_obj(await res.json())
        except:
            logger.exception(f"Failed to load data sources config")
            raise

    async def get_base_policy_data(self, config_url: str = None, data_fetch_reason="Initial load"):
        """
        Load data into the policy store according to the data source's config provided in the config URL

        Args:
            config_url (str, optional): URL to retrive data sources config from. Defaults to None ( self._data_sources_config_url).
            data_fetch_reason (str, optional): Reason to log for the update operation. Defaults to "Initial load".
        """
        logger.info("Performing data configuration, reason: {reason}", reason={data_fetch_reason})
        sources_config = await self.get_policy_data_config(url=config_url)
        # translate config to a data update
        entries = sources_config.entries
        update = DataUpdate(reason=data_fetch_reason, entries=entries)
        self.trigger_data_update(update)

    async def on_connect(self, client: PubSubClient, channel: RpcChannel):
        """
        Pub/Sub on_connect callback
        On connection to backend, whether its the first connection,
        or reconnecting after downtime, refetch the state opa needs.
        As long as the connection is alive we know we are in sync with the server,
        when the connection is lost we assume we need to start from scratch.
        """
        logger.info("Connected to server")
        if self._fetch_on_connect:
            await self.get_base_policy_data()

    async def on_disconnect(self, channel: RpcChannel):
        logger.info("Disconnected from server")

    async def start(self):
        logger.info("Launching data updater")
        if self._subscriber_task is None:
            self._subscriber_task = asyncio.create_task(self._subscriber())
            await self._data_fetcher.start()

    async def _subscriber(self):
        """
        Coroutine meant to be spunoff with create_task to listen in
        the background for data events and pass them to the data_fetcher
        """
        logger.info("Subscribing to topics: {topics}", topics=self._data_topics)
        self._client = PubSubClient(
            self._data_topics,
            self._update_policy_data_callback,
            methods_class=TenantAwareRpcEventClientMethods,
            on_connect=[self.on_connect],
            extra_headers=self._extra_headers,
            keep_alive=opal_client_config.KEEP_ALIVE_INTERVAL,
            server_uri=self._server_url
        )
        async with self._client:
            await self._client.wait_until_done()

    async def stop(self):
        self._stopping = True
        logger.info("Stopping data updater")

        # disconnect from Pub/Sub
        if self._client is not None:
            try:
                await asyncio.wait_for(self._client.disconnect(), timeout=3)
            except asyncio.TimeoutError:
                logger.debug("Timeout waiting for DataUpdater pubsub client to disconnect")

        # stop subscriber task
        if self._subscriber_task is not None:
            logger.debug("Cancelling DataUpdater subscriber task")
            self._subscriber_task.cancel()
            try:
                await self._subscriber_task
            except asyncio.CancelledError as exc:
                logger.debug("DataUpdater subscriber task was force-cancelled: {e}", exc=exc)
            self._subscriber_task = None
            logger.debug("DataUpdater subscriber task was cancelled")

        # stop the data fetcher
        logger.debug("Stopping data fetcher")
        await self._data_fetcher.stop()

    async def wait_until_done(self):
        if self._subscriber_task is not None:
            await self._subscriber_task

    @staticmethod
    def calc_hash(data):
        """
        Calculate an hash (sah256) on the given data, if data isn't a string, it will be converted to JSON.
        String are encoded as 'utf-8' prior to hash calculation.
        Returns: 
            the hash of the given data (as a a hexdigit string) or '' on failure to process. 
        """
        try:
            if not isinstance(data, str):
                data = json.dumps(data)
            return hashlib.sha256(data.encode('utf-8')).hexdigest()
        except:
            logger.exception("Failed to calculate hash for data {data}", data=data)
            return ""

    async def report_update_results(self, update: DataUpdate, reports: List[DataEntryReport], data_fetcher: DataFetcher):
        try:
            whole_report = DataUpdateReport(update_id=update.id, reports=reports)

            callbacks = update.callback.callbacks or opal_client_config.DEFAULT_UPDATE_CALLBACKS.callbacks
            urls = []
            for callback in callbacks:
                if isinstance(callback, str):
                    url = callback
                    callback_config = opal_client_config.DEFAULT_UPDATE_CALLBACK_CONFIG.copy()
                else:
                    url, callback_config = callback
                callback_config.data = whole_report.json()
                urls.append((url, callback_config))

            logger.info("Reporting the update to requested callbacks", urls=urls)
            report_results = await data_fetcher.handle_urls(urls)
            # log reports which we failed to send
            for (url, config), result in zip(urls,report_results):
                if isinstance(result, Exception):
                    logger.error("Failed to send report to {url} with config {config}", url=url, config=config, exc_info=result)
        except:
            logger.exception("Failed to excute report_update_results")

    async def update_policy_data(self, update: DataUpdate = None, policy_store: BasePolicyStoreClient = None, data_fetcher=None):
        """
        fetches policy data (policy configuration) from backend and updates it into policy-store (i.e. OPA)
        """
        policy_store = policy_store or DEFAULT_POLICY_STORE_GETTER()
        if data_fetcher is None:
            data_fetcher = DataFetcher()
        # types / defaults
        urls: List[Tuple[str, FetcherConfig]] = None
        entries: List[DataSourceEntry] = []
        # track the result of each url in order to report back
        reports: List[DataEntryReport] = []
        # if we have an actual specification for the update
        if update is not None:
            entries = update.entries
            urls = [(entry.url, entry.config) for entry in entries]

        # get the data for the update
        logger.info("Fetching policy data", urls=urls)
        # Urls may be None - handle_urls has a default for None
        policy_data_with_urls = await data_fetcher.handle_urls(urls)
        # Save the data from the update
        # We wrap our interaction with the policy store with a transaction  
        async with policy_store.transaction_context(update.id) as store_transaction:
            # for intelisense treat store_transaction as a PolicyStoreClient (which it proxies)
            store_transaction: BasePolicyStoreClient
            for (url, fetch_config, result), entry in itertools.zip_longest(policy_data_with_urls, entries):
                if not isinstance(result, Exception):
                    # get path to store the URL data (default mode (None) is as "" - i.e. as all the data at root)
                    policy_store_path = "" if entry is None else entry.dst_path
                    # None is not valid - use "" (protect from missconfig)
                    if policy_store_path is None:
                        policy_store_path = ""
                    # fix opa_path (if not empty must start with "/" to be nested under data)
                    if policy_store_path != "" and not policy_store_path.startswith("/"):
                        policy_store_path = f"/{policy_store_path}"
                    policy_data = result
                    # Create a report on the data-fetching
                    report = DataEntryReport(entry=entry, hash=self.calc_hash(policy_data), fetched=True)
                    logger.info(
                        "Saving fetched data to policy-store: source url='{url}', destination path='{path}'",
                        url=url,
                        path=policy_store_path or '/'
                    )
                    try:
                        await store_transaction.set_policy_data(policy_data, path=policy_store_path)
                        # No exception we we're able to save to the policy-store
                        report.saved = True
                        # save the report for the entry
                        reports.append(report)
                    except:
                        logger.exception("Failed to save data update to policy-store")
                        # we failed to save to policy-store
                        report.saved = False
                        # save the report for the entry
                        reports.append(report)
                        # re-raise so the context manager will be aware of the failure
                        raise
                else:
                    report = DataEntryReport(entry=entry, fetched=False, saved=False)
                    # save the report for the entry
                    reports.append(report)
        # should we send a report to defined callbackers?
        if self._should_send_reports:
            # spin off reporting (no need to wait on it)
            asyncio.create_task(self.report_update_results(update, reports, data_fetcher))
