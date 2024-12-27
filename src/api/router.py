from fastapi import APIRouter

from src.api.routers.categories import router as category_router
from src.api.routers.products import router as product_router


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
    return main_router
