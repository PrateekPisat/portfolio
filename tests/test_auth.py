import pytest
from configly import Config
from sqlalchemy.orm import Session

from portfolio.auth import decode_auth_token, encode_auth_token
from portfolio.error import InvalidAuthToken, SessionExpired
from tests.factories.user import get_random_user


class Test_Auth:
    def test_roundtrip(self, pg: Session, config: Config):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        secret_key = "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0"
        assert user.id == decode_auth_token(encode_auth_token(user.id, secret_key), secret_key)

    def test_it_raises_on_token_expiry(self, pg: Session, config: Config):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        secret_key = "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0"
        token = encode_auth_token(user.id, secret_key, duration=-1)

        with pytest.raises(SessionExpired):
            decode_auth_token(token, secret_key)

    def test_it_raises_on_invalid_token(self, pg: Session, config: Config):
        secret_key = "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0"

        with pytest.raises(InvalidAuthToken):
            decode_auth_token("random_token", secret_key)
