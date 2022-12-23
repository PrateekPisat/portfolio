import json
from collections import defaultdict

from flask import Response
from pydantic import ValidationError


class AuthError(Exception):
    """Base class for all Authentication Errors."""


class InvalidAuthToken(AuthError):
    """Raise when jwt.InvalidTokenError is encountered."""


class SessionExpired(AuthError):
    """Raise when jwt.ExpiredSignatureError is encountered."""


def generate_error_handler():
    def _generate_handler(error):
        body = {"status": "fail", "message": str(error)}

        if isinstance(error, InvalidAuthToken) or isinstance(error, SessionExpired):
            status_code = 401

        elif isinstance(error, ValidationError):
            status_code = 422
            message = defaultdict(list)
            for e in error.errors():
                message[".".join([str(loc) for loc in e["loc"]])].append(e["msg"])
            body["message"] = json.dumps(message)

        else:
            status_code = 500

        return Response(json.dumps(body), status=status_code, mimetype="application/json")

    return _generate_handler


error_handlers = [
    # 401
    (InvalidAuthToken, generate_error_handler()),
    (SessionExpired, generate_error_handler()),
    # 422
    (ValidationError, generate_error_handler()),
    # 500
    (Exception, generate_error_handler()),
]
