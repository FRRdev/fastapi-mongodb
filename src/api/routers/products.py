from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.domain.products.dto.input import ProductInSchema
from src.domain.products.dto.output import ProductOutSchema
from src.domain.products.interfaces import ICreateProduct
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
