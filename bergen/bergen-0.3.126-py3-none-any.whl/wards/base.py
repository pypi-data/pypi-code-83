from abc import abstractmethod
from abc import ABC
import asyncio
from bergen.schema import DataPoint
from bergen.query import  TypedGQL
from typing import TypeVar
from bergen.console import console


T = TypeVar("T")

class WardException(Exception):
    pass

class ConnectionError(Exception):
    pass




class BaseWard(ABC):

    def __init__(self, client, point: DataPoint, loop=None):
        self.loop = loop or client.loop or asyncio.get_event_loop()

        self.needs_negotiation = point.needsNegotiation
        self.host = point.outward or client.config.host
        self.port = point.port or client.config.port
        self.protocol = "https" if point.secure or client.config.secure else "http"

        self.token = client.auth.access_token
        assert self.token is not None, "Cannot create a Ward without acquiring a Token first"


    @abstractmethod
    async def connect(self):
        pass


    async def configure(self):
        try:
            await self.connect()
            if self.needs_negotiation: 
                return await self.negotiate()
        except:
            console.print_exception()
            raise ConnectionError(f"Connection to {self.host}:{self.port} on {self.port} Failed")
        


    def run(self, the_query: TypedGQL, variables: dict = {}, **kwargs):
        return self.loop.run_until_complete(self.run_async(the_query, variables=variables, **kwargs))


    @abstractmethod
    def run_async(self, gql: TypedGQL, variables: dict = {}):
        return gql.cls(**{})


    @abstractmethod
    async def disconnect(self):
        pass


    async def __aenter__(self):
        await self.configure()
        return self


    async def __aexit__(self, *args, **kwargs):
        await self.disconnect()

