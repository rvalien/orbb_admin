from http import HTTPStatus

from starlette.responses import Response


def get_readiness() -> Response:
    return Response(content='Ok', status_code=HTTPStatus.OK)
