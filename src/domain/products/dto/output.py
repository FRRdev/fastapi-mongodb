from decimal import Decimal

from pydantic import BaseModel, Field

from src.domain.products.entity import Product


class ProductOutSchema(BaseModel):
    oid: str
    name: str
    price: Decimal = Field(max_digits=5, decimal_places=2)
    category_id: str

    @classmethod
    def from_entity(cls, product: Product) -> "ProductOutSchema":
        return ProductOutSchema(
            oid=product.oid,
            name=product.name,
            price=product.price,
            category_id=product.category_id,
        )
