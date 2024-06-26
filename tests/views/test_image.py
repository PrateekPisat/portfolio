import json

import blurhash
import boto3
import pendulum
import pytest
from boto3_type_annotations.s3 import Client
from configly import Config
from flask.testing import FlaskClient
from freezegun import freeze_time
from moto import mock_s3
from sqlalchemy.orm import Session

from portfolio.auth import encode_auth_token
from portfolio.models import image
from portfolio.views import spec
from tests.factories.image import get_random_group, get_random_image
from tests.factories.user import get_random_user


def setup_s3(bucket: str) -> Client:
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket=bucket)
    return s3


class Test_GetImage:
    def test_it_returns_an_image(self, pg: Session, client: FlaskClient, config: Config):
        image = get_random_image()
        pg.add(image)
        pg.commit()

        resp = client.get(f"/api/image/{image.id}")
        assert resp.status_code == 200
        assert resp.json["image"] == spec.Image.from_db_model(image).dict(by_alias=True)

    def test_it_raises_on_missing_image(self, client: FlaskClient):
        resp = client.get("/api/image/1")

        assert resp.status_code == 404
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Image not found."


class Test_ListImages:
    def test_it_returns_zero_images(self, client: FlaskClient):
        resp = client.get("/api/images")

        assert resp.status_code == 200
        assert resp.json["status"] == "success"
        assert resp.json["images"] == []

    def test_it_returns_single_image(self, pg: Session, client: FlaskClient):
        image = get_random_image()
        pg.add(image)
        pg.commit()

        resp = client.get("/api/images")
        assert resp.status_code == 200
        assert resp.json["images"] == [spec.Image.from_db_model(image).dict(by_alias=True)]

    def test_it_returns_multiple_image(self, pg: Session, client: FlaskClient):
        images = [get_random_image(), get_random_image()]
        pg.add_all(images)
        pg.commit()

        resp = client.get("/api/images")
        assert resp.status_code == 200
        assert resp.json["images"] == [
            spec.Image.from_db_model(image).dict(by_alias=True) for image in images
        ]

    def test_it_filters_for_groups(self, pg: Session, client: FlaskClient):
        group_1 = get_random_group()
        group_2 = get_random_group()
        image_1 = get_random_image(group=group_1)
        image_2 = get_random_image(group=group_2)
        pg.add_all([group_1, group_2, image_1, image_2])
        pg.commit()

        resp = client.get(f"/api/images?groupId={group_1.id}")
        assert resp.status_code == 200
        assert resp.json["images"] == [spec.Image.from_db_model(image_1).dict(by_alias=True)]


@freeze_time("2023-01-01T00:00:00")
class Test_CreateImage:
    @mock_s3
    @pytest.mark.parametrize("group_id", [None, 1])
    def test_it_creates_image(
        self, pg: Session, client: FlaskClient, config: Config, group_id: int | None
    ):
        s3 = setup_s3("test")
        s3.upload_file("tests/sample_files/test_image_2.jpeg", Bucket="test", Key="full/bridge.jpg")

        if group_id:
            group = get_random_group(id=group_id)
            pg.add(group)
            pg.commit()

        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key)

        image_payload = {
            "width": 1920,
            "height": 1080,
            "blurHash": "ak12j3h",
            "description": "Image of a bridge.",
            "city": "Boston",
            "country": "United States",
            "fullPath": "full/bridge.jpg",
            "thumbnailPath": "thumbnail/bridge.jpg",
        }

        resp = client.post(
            "/api/images",
            json={"images": [image_payload]},
            headers={"Authorization": f"Bearer {token}"},
        )

        assert resp.status_code == 200

        images: list[image.Image] = pg.query(image.Image).all()
        assert len(images) == 1

        assert resp.json["images"] == [spec.Image.from_db_model(images[0]).dict(by_alias=True)]

        assert images[0].height == 1080
        assert images[0].width == 1920
        assert images[0].description == "Image of a bridge."
        assert images[0].city == "Boston"
        assert images[0].country == "United States"
        assert images[0].blur_hash == "ak12j3h"
        assert images[0].full_path == "full/bridge.jpg"
        assert images[0].thumbnail_path == "thumbnail/bridge.jpg"

    @mock_s3
    def test_it_creates_image_without_blur_hash(
        self, pg: Session, client: FlaskClient, config: Config, aws_credentials
    ):
        test_file_path = "tests/sample_files/test_image_2.jpeg"
        s3 = setup_s3("test")
        s3.upload_file(test_file_path, Bucket="test", Key="full/bridge.jpg")
        blur_hash = blurhash.encode(test_file_path, x_components=4, y_components=3)

        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key)

        image_payload = {
            "width": 1920,
            "height": 1080,
            "blurHash": None,
            "description": "Image of a bridge.",
            "city": "Boston",
            "country": "United States",
            "fullPath": "full/bridge.jpg",
            "thumbnailPath": "thumbnail/bridge.jpg",
        }

        resp = client.post(
            "/api/images",
            json={"images": [image_payload]},
            headers={"Authorization": f"Bearer {token}"},
        )

        assert resp.status_code == 200

        images: list[image.Image] = pg.query(image.Image).all()
        assert len(images) == 1

        assert resp.json["images"] == [spec.Image.from_db_model(images[0]).dict(by_alias=True)]

        assert images[0].height == 1080
        assert images[0].width == 1920
        assert images[0].description == "Image of a bridge."
        assert images[0].city == "Boston"
        assert images[0].country == "United States"
        assert images[0].full_path == "full/bridge.jpg"
        assert images[0].thumbnail_path == "thumbnail/bridge.jpg"
        assert images[0].blur_hash == blur_hash

    @mock_s3
    def test_it_raises_on_missing_auth_header(self, pg: Session, client: FlaskClient):
        s3 = setup_s3("test")
        s3.upload_file("tests/sample_files/test_image_2.jpeg", Bucket="test", Key="full/bridge.jpg")

        image_payload = {
            "width": 1920,
            "height": 1080,
            "blurHash": "ak12j3h",
            "description": "Image of a bridge.",
            "city": "Boston",
            "country": "United States",
            "fullPath": "full/bridge.jpg",
            "thumbnailPath": "thumbnail/bridge.jpg",
        }

        resp = client.post("/api/images", json={"images": [image_payload]})
        assert resp.status_code == 422
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == json.dumps({"Authorization": ["field required"]})

    @mock_s3
    def test_it_raises_on_expired_auth_token(
        self, pg: Session, client: FlaskClient, config: Config
    ):
        s3 = setup_s3("test")
        s3.upload_file("tests/sample_files/test_image_2.jpeg", Bucket="test", Key="full/bridge.jpg")

        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key, duration=-1)

        image_payload = {
            "width": 1920,
            "height": 1080,
            "blurHash": "ak12j3h",
            "description": "Image of a bridge.",
            "city": "Boston",
            "country": "United States",
            "fullPath": "full/bridge.jpg",
            "thumbnailPath": "thumbnail/bridge.jpg",
        }

        resp = client.post(
            "/api/images",
            json={"images": [image_payload]},
            headers={"Authorization": f"Bearer {token}"},
        )

        assert resp.status_code == 401
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Signature expired. Please log in again."


@freeze_time("2023-01-01T00:00:00")
class Test_UpdateImage:
    def test_it_updates_images(self, pg: Session, client: FlaskClient, config: Config):
        pg.add(get_random_image(id=1))
        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key)

        image_payload = {
            "width": 1920,
            "height": 1080,
            "blurHash": "ak12j3h",
            "description": "Image of a bridge.",
            "city": "Boston",
            "country": "United States",
            "fullPath": "full/bridge.jpg",
            "thumbnailPath": "thumbnail/bridge.jpg",
        }

        resp = client.patch(
            "/api/images/1",
            json={"image": image_payload},
            headers={"Authorization": f"Bearer {token}"},
        )

        images: list[image.Image] = pg.query(image.Image).all()
        assert len(images) == 1

        assert resp.status_code == 200
        assert resp.json["image"] == {
            **image_payload,
            "groupId": None,
            "groupName": None,
            "updatedAt": pendulum.now("UTC").isoformat(),
            "createdAt": images[0].created_at.isoformat(),
            "id": images[0].id,
        }

        assert images[0].height == 1080
        assert images[0].width == 1920
        assert images[0].description == "Image of a bridge."
        assert images[0].city == "Boston"
        assert images[0].country == "United States"
        assert images[0].blur_hash == "ak12j3h"
        assert images[0].full_path == "full/bridge.jpg"
        assert images[0].thumbnail_path == "thumbnail/bridge.jpg"
        assert images[0].updated_at.isoformat() == pendulum.now("UTC").isoformat()

    def test_it_raises_on_missing_image(self, pg: Session, client: FlaskClient, config: Config):
        user = get_random_user()
        pg.add(user)
        pg.commit()

        token = encode_auth_token(user.id, config.cryptography.key)

        image_payload = {
            "width": 1920,
            "height": 1080,
            "blurHash": "ak12j3h",
            "description": "Image of a bridge.",
            "city": "Boston",
            "country": "United States",
            "fullPath": "full/bridge.jpg",
            "thumbnailPath": "thumbnail/bridge.jpg",
        }

        resp = client.patch(
            "/api/images/1",
            json={"image": image_payload},
            headers={"Authorization": f"Bearer {token}"},
        )
        assert resp.status_code == 404
        assert resp.json["message"] == "Image 1 not found"

    def test_it_raises_on_missing_auth_header(self, pg: Session, client: FlaskClient):
        pg.add_all([get_random_user()])
        pg.commit()

        image_payload = {
            "width": 1920,
            "height": 1080,
            "blurHash": "ak12j3h",
            "description": "Image of a bridge.",
            "city": "Boston",
            "country": "United States",
            "fullPath": "full/bridge.jpg",
            "thumbnailPath": "thumbnail/bridge.jpg",
        }

        resp = client.patch("/api/images/1", json={"image": image_payload})
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

        image_payload = {
            "width": 1920,
            "height": 1080,
            "blurHash": "ak12j3h",
            "description": "Image of a bridge.",
            "city": "Boston",
            "country": "United States",
            "fullPath": "full/bridge.jpg",
            "thumbnailPath": "thumbnail/bridge.jpg",
        }

        image_payload = {
            "width": 1920,
            "height": 1080,
            "blurHash": "ak12j3h",
            "description": "Image of a bridge.",
            "city": "Boston",
            "country": "United States",
            "fullPath": "full/bridge.jpg",
            "thumbnailPath": "thumbnail/bridge.jpg",
        }

        resp = client.patch(
            "/api/images/1",
            json={"image": image_payload},
            headers={"Authorization": f"Bearer {token}"},
        )

        assert resp.status_code == 401
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Signature expired. Please log in again."
