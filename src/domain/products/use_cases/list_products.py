from collections.abc import Sequence
from datetime import datetime
from typing import Final

import pytz
from attr import define

from src.domain.discounts.entity import Discount
from src.domain.products.entity import Product
from src.domain.products.interfaces import IProductRepo

EVENING_DISCOUNT_START: Final = 16
EVENING_DISCOUNT_END: Final = 24


@define
class ListProducts:
    product_repo: IProductRepo

    async def __call__(self) -> Sequence[Product]:
        current_time = datetime.now(pytz.timezone("Europe/Moscow"))
        products = await self.product_repo.get_products()
        if EVENING_DISCOUNT_START <= current_time.hour <= EVENING_DISCOUNT_END:
            discount = Discount(10)
            return [product.apply_discount(discount) for product in products]
        return products
