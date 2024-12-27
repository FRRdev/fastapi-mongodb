from dependency_injector import containers, providers

from src.infrastructure.repositories.categories.mongo import MongoDBCategoriesRepository
from src.infrastructure.repositories.products.mongo import MongoDBProductsRepository


class Repositories(containers.DeclarativeContainer):
    config = providers.Configuration()
    gateways = providers.DependenciesContainer()

    category_repo = providers.Factory(
        MongoDBCategoriesRepository,
        mongo_db_client=gateways.mongodb_client,
        mongo_db_name=config.mongodb.mongodb_product_database,
        mongo_db_collection_name=config.mongodb.mongodb_category_collection,
    )
    product_repo = providers.Factory(
        MongoDBProductsRepository,
        mongo_db_client=gateways.mongodb_client,
        mongo_db_name=config.mongodb.mongodb_product_database,
        mongo_db_collection_name=config.mongodb.mongodb_product_collection,
    )
