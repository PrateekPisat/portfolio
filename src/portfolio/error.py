class AuthError(Exception):
    """Base class for all Authentication Errors."""


class InvalidAuthToken(AuthError):
    """Raise when jwt.InvalidTokenError is encountered."""


class SessionExpired(AuthError):
    """Raise when jwt.ExpiredSignatureError is encountered"""
