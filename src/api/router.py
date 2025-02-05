from fastapi import APIRouter

from src.api.routers.categories import router as category_router
from src.api.routers.products import router as product_router
from src.api.routers.users import router as user_router


def include_routers() -> APIRouter:
    main_router = APIRouter()
    main_router.include_router(
        category_router,
        prefix="/categories",
        tags=["categories"],
    )
    main_router.include_router(
        product_router,
        prefix="/products",
        tags=["products"],
    )
    main_router.include_router(
        user_router,
        prefix="/users",
        tags=["users"],
    )
    return main_router
