from dependency_injector import containers, providers
from fastapi import FastAPI


class BaseAppContainer(containers.DeclarativeContainer):
    config: providers.Configuration
    wiring_config: containers.WiringConfiguration
    repos: providers.Container
    use_cases: providers.Container
    gateways: providers.Container


class DependencyInjectorFastApi(FastAPI):
    container: BaseAppContainer
