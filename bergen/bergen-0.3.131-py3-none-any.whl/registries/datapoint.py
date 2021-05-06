from asyncio import exceptions
from bergen.schema import DataPoint
from bergen.wards.graphql.aiohttp import AIOHttpGraphQLWard
from bergen.auths.base import BaseAuthBackend
from typing import Callable, Dict
from bergen.enums import DataPointType
from bergen.clients.base import BaseWard
import logging
import asyncio
from bergen.console import console
logger = logging.getLogger(__name__)

datapointregistry = None

class DataPointRegistry(object):


    def __init__(self) -> None:
        self.pointIDPointMap: Dict[str, DataPoint] = {}
        self.pointIDWardMap: Dict[str, BaseWard] = {}
        self.pointIDNegotiationMap: Dict[str, BaseWard] = {}
        self.builders =  {
                # Default Builders for standard
                DataPointType.GRAPHQL: AIOHttpGraphQLWard
        }


    def register_client_builder(self, type:str , builder: Callable):
        self.builders[type] = builder

    def create_ward(self, bergen, point) -> BaseWard:

        if point.app.name == bergen.application.name:
            console.log("[red] Datapoint App is the Same as this One, will not create own Ward!!!")
            return None

        if point.id in self.pointIDWardMap:
            return self.pointIDWardMap[point.id]

        logger.info(f"Creating new Ward for Datapoint {point}")

        if point.type in self.builders:
            builder = self.builders[point.type]
            self.pointIDWardMap[point.id]  = builder(bergen, point)
            self.pointIDPointMap[point.id]  = point

            return self.pointIDWardMap[point.id]
        else:
            raise NotImplementedError(f"We have no idea how to build the ward for this Datapoint {point.type}")

    async def configure_wards(self):
        wards = [ward for id, ward in self.pointIDWardMap.items()]
        names = [point.app.name for id, point in self.pointIDPointMap.items()]

        negotiation_results = await asyncio.gather(*[ward.configure() for ward in wards], return_exceptions=True)
        print(negotiation_results)
        extensions =  {name: result for name, result in zip(names, negotiation_results)}
        return extensions




def get_datapoint_registry() -> DataPointRegistry:
    global datapointregistry
    if datapointregistry is None:
        datapointregistry = DataPointRegistry()
    return datapointregistry