from uuid import uuid4

import orjson
from attr import define

from src.domain.categories.exceptions import (
    CategoryDoesNotExistsException,
)
from src.domain.categories.interfaces import ICategoryRepo
from src.domain.notifications.dto.input import NotificationManager
from src.domain.notifications.enums import NotificationType
from src.domain.products.dto.input import ProductInSchema
from src.domain.products.entity import Product
from src.domain.products.interfaces import IMessageBroker, IProductRepo, ISlugifier


@define
class CreateProduct:
    product_repo: IProductRepo
    category_repo: ICategoryRepo
    slugifier: ISlugifier
    message_broker: IMessageBroker

    async def __call__(self, schema: ProductInSchema) -> Product:
        if not await self.category_repo.check_category_exists_by_oid(
            schema.category_id,
        ):
            raise CategoryDoesNotExistsException(schema.category_id)

        slug = await self.slugifier.generate_slug(schema.name)
        product = Product(
            name=schema.name,
            slug=slug,
            price=schema.price,
            category_id=schema.category_id,
        )
        notification = NotificationManager(
            notification_type=NotificationType.create_product,  # type: ignore[call-arg]
            product_name=product.name,
        )
        await self.message_broker.send_message(
            key=str(uuid4()).encode(),
            value=orjson.dumps(notification.model_dump()),
            topic="products",
        )
        await self.product_repo.add_product(product)
        return product
