from fastapi import APIRouter, FastAPI

from api.handlers import get_readiness


def create_app() -> FastAPI:
    app = FastAPI()

    router = APIRouter()
    router.add_api_route('/readiness', get_readiness, methods=['GET'])
    app.include_router(router)

    main_router = APIRouter()
    app.include_router(main_router, prefix='/users')

    return app


if __name__ == '__main__':
    import uvicorn

    from db import DBSettings

    DBSettings().setup_db()

    app = create_app()
    uvicorn.run(app, host='0.0.0.0', port=8000, debug=True)
