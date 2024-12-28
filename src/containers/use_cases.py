from dependency_injector import containers, providers

from src.domain.categories.use_cases.create_category import CreateCategory
from src.domain.categories.use_cases.list_categories import ListCategories
from src.domain.products.use_cases.create_product import CreateProduct
from src.domain.products.use_cases.list_products import ListProducts


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

    create_product = providers.Factory(
        CreateProduct,
        product_repo=repositories.product_repo,
        category_repo=repositories.category_repo,
    )
    list_products = providers.Factory(
        ListProducts,
        product_repo=repositories.product_repo,
    )
