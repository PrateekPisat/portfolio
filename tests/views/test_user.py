
import pytest
from flask.testing import FlaskClient
from sqlalchemy.orm import Session

from portfolio.views import spec
from tests.factories.user import get_random_user


class Test_Auth:
    def test_it_authenticates_user(self, pg: Session, client: FlaskClient):
        user = get_random_user(username="FakeUser", password="FakeHashedPassword")
        pg.add(user)
        pg.commit()

        resp = client.post(
            "api/user/login",
            json={"username": user.username, "passwordHash": user.password},
        )
        assert resp.status_code == 200
        assert "authToken" in resp.json
        assert resp.json["status"] == "success"
        assert resp.json["message"] == "Successfully logged in."

    @pytest.mark.parametrize(
        "creds, expected_error",
        [
            (dict(username="FakeUser"), '{"passwordHash": ["field required"]}'),
            (
                dict(passwordHash="FakeHashedPassword"),
                '{"username": ["field required"]}',
            ),
        ],
    )
    def test_it_raises_on_invalid_request_payload(
        self,
        pg: Session,
        client: FlaskClient,
        creds: dict[str, str],
        expected_error: str,
    ):
        user = get_random_user(username="FakeUser", password="FakeHashedPassword")
        pg.add(user)
        pg.commit()

        resp = client.post("api/user/login", json=creds)
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
        self, pg: Session, client: FlaskClient, creds: dict[str, str]
    ):
        user = get_random_user(username="FakeUser", password="FakeHashedPassword")
        pg.add(user)
        pg.commit()

        resp = client.post("api/user/login", json=creds)
        assert resp.status_code == 400
        assert "authToken" not in resp.json
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "User not found."


class Test_Get:
    def test_it_returns_user(self, pg: Session, client: FlaskClient):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        resp = client.get(f"api/user/{user.id}")
        assert resp.status_code == 200
        assert resp.json["status"] == "success"
        assert resp.json["user"] == spec.User.from_db_model(user).dict(by_alias=True)

    def test_it_raises_on_missing_user(self, client: FlaskClient):
        resp = client.get("api/user/123")
        assert resp.status_code == 404
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "User 123 not found."
