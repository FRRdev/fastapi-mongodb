import pydantic
from dependency_injector import containers, providers
from pydantic_settings import BaseSettings

from src.config.settings import Settings
from src.containers.gateways import Gateways
from src.containers.repositories import Repositories
from src.containers.use_cases import UseCases
from src.utils.fastapi_dependency_injector import BaseAppContainer

pydantic.BaseSettings = BaseSettings


class Container(BaseAppContainer):
    config = providers.Configuration(pydantic_settings=[Settings()])
    wiring_config = containers.WiringConfiguration(packages=["src.api.routers"])
    gateways = providers.Container(Gateways, config=config)
    repositories = providers.Container(Repositories, gateways=gateways, config=config)
    use_cases = providers.Container(
        UseCases,
        repositories=repositories,
        gateways=gateways,
    )


container = Container()
