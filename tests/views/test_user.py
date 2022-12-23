import json
from typing import Dict

import pytest
from configly import Config
from flask.testing import FlaskClient
from sqlalchemy.orm import Session

from portfolio.auth import encode_auth_token
from portfolio.views import spec
from tests.factories.user import get_random_user


class Test_Auth:
    def test_it_authenticates_user(self, pg: Session, client: FlaskClient):
        user = get_random_user(username="FakeUser", password="FakeHashedPassword")
        pg.add(user)
        pg.commit()

        resp = client.post(
            "user/login", json={"username": user.username, "passwordHash": user.password}
        )
        assert resp.status_code == 200
        assert "authToken" in resp.json
        assert resp.json["status"] == "success"
        assert resp.json["message"] == "Successfully logged in."

    @pytest.mark.parametrize(
        "creds, expected_error",
        [
            (dict(username="FakeUser"), '{"passwordHash": ["field required"]}'),
            (dict(passwordHash="FakeHashedPassword"), '{"username": ["field required"]}'),
        ],
    )
    def test_it_raises_on_invalid_request_payload(
        self, pg: Session, client: FlaskClient, creds: Dict[str, str], expected_error: str
    ):
        user = get_random_user(username="FakeUser", password="FakeHashedPassword")
        pg.add(user)
        pg.commit()

        resp = client.post("user/login", json=creds)
        assert resp.status_code == 422
        assert "authToken" not in resp.json
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == expected_error

    @pytest.mark.parametrize(
        "creds",
        [
            dict(username="FakeUser", passwordHash="RandomPassword"),
            dict(username="RandomUser", passwordHash="FakeHashedPassword"),
        ],
    )
    def test_it_raises_on_invalid_user_auth(
        self, pg: Session, client: FlaskClient, creds: Dict[str, str]
    ):
        user = get_random_user(username="FakeUser", password="FakeHashedPassword")
        pg.add(user)
        pg.commit()

        resp = client.post("user/login", json=creds)
        assert resp.status_code == 400
        assert "authToken" not in resp.json
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "User not found."


class Test_Get:
    def test_it_returns_user(self, pg: Session, client: FlaskClient, config: Config):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key)

        resp = client.get(f"user/{user.id}", headers={"Authorization": f"Bearer {token}"})
        assert resp.status_code == 200
        assert resp.json["status"] == "success"
        assert resp.json["user"] == spec.User.from_db_model(user).dict(by_alias=True)

    def test_it_raises_on_missing_auth_header(self, pg: Session, client: FlaskClient):
        resp = client.get("user/1")
        assert resp.status_code == 422
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == json.dumps({"Authorization": ["field required"]})

    def test_it_raises_on_expired_auth_token(
        self, pg: Session, client: FlaskClient, config: Config
    ):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key, duration=-1)

        resp = client.get(f"user/{user.id}", headers={"Authorization": f"Bearer {token}"})
        assert resp.status_code == 401
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Signature expired. Please log in again."

    def test_it_raises_on_invalid_auth_token(self, pg: Session, client: FlaskClient):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        resp = client.get(f"user/{user.id}", headers={"Authorization": "Bearer fake_token"})
        assert resp.status_code == 401
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Invalid token. Please log in again."

    def test_it_raises_on_missing_user(self, pg: Session, client: FlaskClient, config: Config):
        user = get_random_user(id=1)
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key, duration=-1)

        resp = client.get("user/123", headers={"Authorization": f"Bearer {token}"})
        assert resp.status_code == 401
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Signature expired. Please log in again."
