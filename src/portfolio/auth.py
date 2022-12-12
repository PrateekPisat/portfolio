import jwt
import pendulum

from portfolio.error import InvalidAuthToken, SessionExpired


def encode_auth_token(user_id: int, secret_key: str, duration: int = 60 * 60 * 24) -> str:
    payload = {"exp": pendulum.now().add(seconds=duration), "iat": pendulum.now(), "sub": user_id}
    return jwt.encode(payload, secret_key, algorithm="HS256")


def decode_auth_token(auth_token: str, secret_key: str) -> int:
    try:
        payload = jwt.decode(auth_token, secret_key, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return SessionExpired("Signature expired. Please log in again.")
    except jwt.InvalidTokenError:
        return InvalidAuthToken("Invalid token. Please log in again.")
