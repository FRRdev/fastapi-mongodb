from dependency_injector import containers, providers

from src.domain.categories.use_cases.create_category import CreateCategory
from src.domain.categories.use_cases.list_categories import ListCategories
from src.domain.notifications.use_cases.consume_and_create_notifications import (
    ConsumeAndCreateNotifications,
)
from src.domain.products.use_cases.create_product import CreateProduct
from src.domain.products.use_cases.list_products import ListProducts
from src.domain.users.use_cases.create_user import CreateUser


class UseCases(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    gateways = providers.DependenciesContainer()

    # categories
    create_category = providers.Factory(
        CreateCategory,
        category_repo=repositories.category_repo,
    )
    list_categories = providers.Factory(
        ListCategories,
        category_repo=repositories.category_repo,
    )

    # products
    create_product = providers.Factory(
        CreateProduct,
        product_repo=repositories.product_repo,
        category_repo=repositories.category_repo,
        slugifier=repositories.slugifier,
        message_broker=gateways.message_broker,
    )
    list_products = providers.Factory(
        ListProducts,
        product_repo=repositories.product_repo,
    )

    # users
    create_user = providers.Factory(
        CreateUser,
        user_repo=repositories.user_repo,
    )

    # notifications
    consume_and_create_notifications = providers.Factory(
        ConsumeAndCreateNotifications,
        message_broker=gateways.message_broker,
    )
