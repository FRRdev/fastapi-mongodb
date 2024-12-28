from collections.abc import Sequence

from attr import define

from src.domain.products.entity import Product
from src.domain.products.interfaces import IProductRepo


@define
class ListProducts:
    product_repo: IProductRepo

    async def __call__(self) -> Sequence[Product]:
        return await self.product_repo.get_products()
