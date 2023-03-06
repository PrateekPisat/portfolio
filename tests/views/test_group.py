import json
from typing import List

import pendulum
from configly import Config
from flask.testing import FlaskClient
from freezegun import freeze_time
from moto import mock_s3
from sqlalchemy.orm import Session

from portfolio.auth import encode_auth_token
from portfolio.models import image
from portfolio.views import spec
from tests.factories.image import get_random_group
from tests.factories.user import get_random_user


class Test_GetGroup:
    def test_it_returns_a_group(self, pg: Session, client: FlaskClient, config: Config):
        group = get_random_group()
        pg.add(group)
        pg.commit()

        resp = client.get(f"/api/group/{group.id}")
        assert resp.status_code == 200
        assert resp.json["group"] == spec.Group.from_db_model(group).dict(by_alias=True)

    def test_it_raises_on_missing_group(self, client: FlaskClient):
        resp = client.get("/api/group/1")

        assert resp.status_code == 404
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Group not found."


class Test_ListGroups:
    def test_it_returns_zero_groups(self, client: FlaskClient):
        resp = client.get("/api/groups")

        assert resp.status_code == 200
        assert resp.json["status"] == "success"
        assert resp.json["groups"] == []

    def test_it_returns_single_group(self, pg: Session, client: FlaskClient):
        group = get_random_group()
        pg.add(group)
        pg.commit()

        resp = client.get("/api/groups")
        assert resp.status_code == 200
        assert resp.json["groups"] == [spec.Group.from_db_model(group).dict(by_alias=True)]

    def test_it_returns_multiple_group(self, pg: Session, client: FlaskClient):
        groups = [get_random_group(), get_random_group()]
        pg.add_all(groups)
        pg.commit()

        resp = client.get("/api/groups")
        assert resp.status_code == 200
        assert resp.json["groups"] == [
            spec.Group.from_db_model(group).dict(by_alias=True) for group in groups
        ]


@freeze_time("2023-01-01T00:00:00")
class Test_CreateGroup:
    payload = {"groups": [{"name": "Landscape"}]}

    @mock_s3
    def test_it_creates_group(self, pg: Session, client: FlaskClient, config: Config):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key)
        resp = client.post(
            "/api/groups", json=self.payload, headers={"Authorization": f"Bearer {token}"}
        )

        assert resp.status_code == 200

        groups: List[image.Group] = pg.query(image.Group).all()
        assert len(groups) == 1

        assert resp.json["groups"] == [spec.Group.from_db_model(groups[0]).dict(by_alias=True)]
        assert groups[0].name == "Landscape"

    @mock_s3
    def test_it_raises_on_missing_auth_header(self, pg: Session, client: FlaskClient):
        resp = client.post("/api/groups", json=self.payload)
        assert resp.status_code == 422
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == json.dumps({"Authorization": ["field required"]})

    @mock_s3
    def test_it_raises_on_expired_auth_token(
        self, pg: Session, client: FlaskClient, config: Config
    ):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key, duration=-1)

        resp = client.post(
            "/api/groups", json=self.payload, headers={"Authorization": f"Bearer {token}"}
        )

        assert resp.status_code == 401
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Signature expired. Please log in again."


@freeze_time("2023-01-01T00:00:00-05:00")
class Test_UpdateGroup:
    def test_it_updates_groups(self, pg: Session, client: FlaskClient, config: Config):
        group = get_random_group()
        pg.add(group)
        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key)

        resp = client.patch(
            f"/api/group/{group.id}",
            json={"name": "Landscape", "id": group.id},
            headers={"Authorization": f"Bearer {token}"},
        )

        assert resp.status_code == 200
        assert resp.json["group"] == {
            **{"name": "Landscape", "id": group.id},
            "updatedAt": pendulum.now("UTC").isoformat(),
            "createdAt": group.created_at.isoformat(),
            "id": group.id,
        }

    def test_it_raises_on_missing_group(self, pg: Session, client: FlaskClient, config: Config):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key)

        resp = client.patch(
            "/api/group/1",
            json={"name": "Landscape", "id": 1},
            headers={"Authorization": f"Bearer {token}"},
        )
        assert resp.status_code == 404
        assert resp.json["message"] == "Group not found."

    def test_it_raises_on_missing_auth_header(self, client: FlaskClient):
        resp = client.patch("/api/group/1", json={"name": "Landscape", "id": 1})
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

        resp = client.patch(
            "/api/group/1",
            json={"name": "Landscape", "id": 1},
            headers={"Authorization": f"Bearer {token}"},
        )

        assert resp.status_code == 401
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Signature expired. Please log in again."
