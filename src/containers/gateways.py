from dependency_injector import containers, providers
from motor.motor_asyncio import AsyncIOMotorClient

from src.utils.logging import setup_logging
from src.utils.uvloop import activate_uvloop


class Gateways(containers.DeclarativeContainer):
    config = providers.Configuration()
    uvloop = providers.Resource(activate_uvloop)
    logging_setup = providers.Resource(setup_logging, config=config.logger)

    mongodb_client: providers.Provider[AsyncIOMotorClient] = providers.Singleton(
        AsyncIOMotorClient,
        config.mongodb.mongodb_connection_uri,
        serverSelectionTimeoutMS=3000,
    )


