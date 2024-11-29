from dependency_injector import containers, providers


class Repositories(containers.DeclarativeContainer):
    config = providers.Configuration()
    gateways = providers.DependenciesContainer()
