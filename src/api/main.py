from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from src.containers import container
from src.utils.exceptions import BaseHTTPException, NotFoundException
from src.utils.fastapi_dependency_injector import DependencyInjectorFastApi


def create_app() -> DependencyInjectorFastApi:
    application = DependencyInjectorFastApi(
        title=container.config.app.name(),
        root_path=container.config.app.root_path(),
        debug=container.config.app.debug(),
    )
    container.gateways.logging_setup.init()  # type: ignore[attr-defined]
    container.gateways.uvloop.init()  # type: ignore[attr-defined]
    application.add_middleware(
        CORSMiddleware,
        allow_origins=container.config.app.cors_origins(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.container = container
    return application


app = create_app()


@app.exception_handler(BaseHTTPException)
async def unicorn_exception_handler(
    request: Request,
    exc: BaseHTTPException,
) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status,
        content={"message": exc.message},
    )


@app.exception_handler(NotFoundException)
async def repository_not_found_exception_handler(
    request: Request,
    exc: NotFoundException,
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"message": "Not found"},
    )


@app.on_event("startup")
async def startup_event() -> None:
    app.container.init_resources()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    app.container.shutdown_resources()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", port=8001, log_level="info")  # noqa: S104
