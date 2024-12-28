from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.domain.products.dto.input import ProductInSchema
from src.domain.products.dto.output import (
    ProductFullOutSchema,
    ProductListOutSchema,
    ProductOutSchema,
)
from src.domain.products.interfaces import ICreateProduct, IListProducts
from src.utils.exceptions.domain_exceptions import DomainException

router = APIRouter()


@router.post(
    "/",
    summary="Создание продукта.",
    response_model=ProductOutSchema,
    status_code=status.HTTP_201_CREATED,
)
@inject
async def create_category(
    new_product: ProductInSchema,
    use_case: ICreateProduct = Depends(Provide["use_cases.create_product"]),
) -> ProductOutSchema:
    try:
        product = await use_case(new_product)
    except DomainException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exception.message},
        ) from exception

    return ProductOutSchema.from_entity(product)


@router.get(
    "/",
    summary="Список продуктов.",
    response_model=ProductListOutSchema,
    status_code=status.HTTP_200_OK,
)
@inject
async def list_categories(
    use_case: IListProducts = Depends(Provide["use_cases.list_products"]),
) -> ProductListOutSchema:
    products = await use_case()
    return ProductListOutSchema(
        [ProductFullOutSchema.from_entity(product) for product in products],
    )
