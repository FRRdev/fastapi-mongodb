from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.domain.users.dto.input import UserInSchema
from src.domain.users.dto.output import UserOutSchema
from src.domain.users.interfaces import ICreateUser
from src.utils.exceptions.domain_exceptions import DomainException

router = APIRouter()


@router.post(
    "/",
    summary="Создание Пользователя.",
    response_model=UserOutSchema,
    status_code=status.HTTP_201_CREATED,
)
@inject
async def create_user(
    new_user: UserInSchema,
    use_case: ICreateUser = Depends(Provide["use_cases.create_user"]),
) -> UserOutSchema:
    try:
        user = await use_case(new_user)
    except DomainException as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exception.message},
        ) from exception

    return UserOutSchema.from_entity(user)
