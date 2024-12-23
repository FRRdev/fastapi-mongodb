from dependency_injector import containers, providers

from src.domain.categories.use_cases.create_category import CreateCategory


class UseCases(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    gateways = providers.DependenciesContainer()

    create_category = providers.Factory(
        CreateCategory,
        category_repo=repositories.category_repo,
    )
