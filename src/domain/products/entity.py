from dataclasses import dataclass
from decimal import Decimal
from typing import Self

from src.domain.categories.entity import Category
from src.domain.discounts.entity import Discount
from src.utils.entity import BaseEntity


@dataclass
class Product(BaseEntity):
    name: str
    price: Decimal
    slug: str | None = None
    category_id: str | None = None
    category: Category | None = None
    discount_price: Decimal | None = None

    def apply_discount(self, discount: Discount) -> Self:
        discount_amount = self.price * Decimal(discount.percent) / Decimal("100")
        discount_amount = discount_amount.quantize(Decimal("0.01"))
        self.discount_price = (self.price - discount_amount).quantize(Decimal("0.01"))
        return self
