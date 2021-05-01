from applauncher.applauncher import Configuration
from dependency_injector import providers, containers
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, validator


class MotorConfig(BaseModel):
    uri: str

    @validator('uri')
    def uri_validator(cls, v):
        if not v.startswith('mongodb'):
            raise ValueError('Uri should starts with mongodb')
        return v


class MotorContainer(containers.DeclarativeContainer):
    config = providers.Dependency(instance_of=MotorConfig)
    configuration = Configuration()
    client = providers.Singleton(
        AsyncIOMotorClient,
        configuration.provided.motor.uri
    )


class MotorBundle:
    def __init__(self):
        self.config_mapping = {
            "motor": MotorConfig
        }

        self.injection_bindings = {
            'motor': MotorContainer
        }
