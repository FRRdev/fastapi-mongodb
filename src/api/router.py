from fastapi import APIRouter

from src.api.routers.categories import router as category_router


def include_routers() -> APIRouter:
    main_router = APIRouter()
    main_router.include_router(
        category_router,
        prefix="/categories",
        tags=["categories"],
    )
    return main_router
