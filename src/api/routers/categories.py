from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.domain.categories.dto.input import CategoryInSchema
from src.domain.categories.dto.output import CategoryOutSchema
from src.domain.categories.interfaces import ICreateCategory
from src.utils.exceptions.domain_exceptions import DomainException

router = APIRouter()


@router.post(
    "/",
    summary="Создание Категории.",
    response_model=CategoryOutSchema,
    status_code=status.HTTP_201_CREATED,
)
@inject
async def create_category(
    new_category: CategoryInSchema,
    use_case: ICreateCategory = Depends(Provide["use_cases.create_category"]),
) -> CategoryOutSchema:
    try:
        category = await use_case(new_category)
    except DomainException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exception.message},
        ) from exception

    return CategoryOutSchema.from_entity(category)

