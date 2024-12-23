from dataclasses import asdict

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.api.queries.category import CategoryQuery
from src.domain.categories.dto.filter import CategoryFilterSchema
from src.domain.categories.dto.input import CategoryInSchema
from src.domain.categories.dto.output import CategoryListOutSchema, CategoryOutSchema
from src.domain.categories.interfaces import ICreateCategory, IListCategories
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


@router.get(
    "/",
    summary="Список Ктегорий.",
    response_model=CategoryListOutSchema,
    status_code=status.HTTP_200_OK,
)
@inject
async def list_categories(
    params: CategoryQuery = Depends(CategoryQuery),
    use_case: IListCategories = Depends(Provide["use_cases.list_categories"]),
) -> CategoryListOutSchema:
    filters = CategoryFilterSchema(**asdict(params))
    categories, count = await use_case(filters)
    return CategoryListOutSchema(
        count=count,
        next_page=count > sum(filters.pagination),
        items=[CategoryOutSchema.from_entity(category) for category in categories],
    )
