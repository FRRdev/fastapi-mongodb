from dependency_injector import containers, providers

from src.domain.categories.use_cases.create_category import CreateCategory
from src.domain.categories.use_cases.list_categories import ListCategories


class UseCases(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    gateways = providers.DependenciesContainer()

    create_category = providers.Factory(
        CreateCategory,
        category_repo=repositories.category_repo,
    )
    list_categories = providers.Factory(
        ListCategories,
        category_repo=repositories.category_repo,
    )
