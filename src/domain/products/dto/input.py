from decimal import Decimal

from pydantic import BaseModel, Field


class ProductInSchema(BaseModel):
    category_id: str
    name: str
    price: Decimal = Field(max_digits=5, decimal_places=2)
