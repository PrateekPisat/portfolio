from typing import Any

import flask_pydantic_spec
from pydantic import BaseModel


def raise_validation_error(
    req: flask_pydantic_spec.Request,
    resp: flask_pydantic_spec.Response,
    req_validation_error: Any,
    instance: BaseModel,
):
    if isinstance(req_validation_error, BaseException):
        raise req_validation_error


validator = flask_pydantic_spec.FlaskPydanticSpec(
    "flask",
    before=raise_validation_error,
    after=raise_validation_error,
    title="Portfolio API",
    path="docs",
)
