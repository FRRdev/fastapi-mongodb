import re
from dataclasses import dataclass

from slugify import slugify

from src.domain.products.interfaces import IProductRepo


@dataclass
class Slugifier:
    product_repo: IProductRepo

    async def generate_slug(self, source: str) -> str:
        base_slug = slugify(source)
        if not await self.product_repo.check_products_exists_by_slug(base_slug):
            return base_slug

        next_suffix = 2
        slug_regex = rf"^{re.escape(base_slug)}-(\d+)$"

        products = await self.product_repo.get_products_by_slug_regex(slug_regex)
        if products:
            max_suffix = float("-inf")

            for product in products:
                if match := re.match(slug_regex, product.slug):  # type: ignore[arg-type]
                    suffix = int(match.group(1))
                    max_suffix = max(max_suffix, suffix)

            next_suffix = max_suffix + 1  # type: ignore[assignment]

        return f"{base_slug}-{next_suffix}"
