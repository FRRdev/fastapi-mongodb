from dependency_injector import containers, providers


class UseCases(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    gateways = providers.DependenciesContainer()
