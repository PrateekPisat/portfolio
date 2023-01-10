from unittest.mock import patch
from flask.testing import FlaskClient
from sqlalchemy.orm import Session
from boto3_type_annotations.s3 import Client
from moto import mock_s3
import boto3

from portfolio.views import spec
from tests.factories.image import get_random_image


class Test_GetImage:
    def test_it_returns_an_image(self, pg: Session, client: FlaskClient):
        image = get_random_image()
        pg.add(image)
        pg.commit()

        resp = client.get(f"/image/{image.id}")
        assert resp.status_code == 200
        assert resp.json["image"] == spec.Image.from_db_model(image).dict(by_alias=True)

    def test_it_raises_on_missing_image(self, client: FlaskClient):
        resp = client.get("/image/1")

        assert resp.status_code == 404
        assert resp.json["status"] == "fail"
        assert resp.json["message"] == "Image not found."


class Test_ListImages:
    def test_it_returns_zero_images(self, client: FlaskClient):
        resp = client.get("/images")

        assert resp.status_code == 200
        assert resp.json["status"] == "success"
        assert resp.json["images"] == []

    def test_it_returns_single_image(self, pg: Session, client: FlaskClient):
        image = get_random_image()
        pg.add(image)
        pg.commit()

        resp = client.get("/images")
        assert resp.status_code == 200
        assert resp.json["images"] == [spec.Image.from_db_model(image).dict(by_alias=True)]

    def test_it_returns_multiple_image(self, pg: Session, client: FlaskClient):
        images = [get_random_image(), get_random_image()]
        pg.add_all(images)
        pg.commit()

        resp = client.get("/images")
        assert resp.status_code == 200
        assert resp.json["images"] == [
            spec.Image.from_db_model(image).dict(by_alias=True) for image in images
        ]


class Test_CreateImage:
    @mock_s3
    def test_it_creates_images(self, pg: Session, client: FlaskClient):
        s3 = boto3.client("s3", region_name="us-east-1")
        s3.create_bucket(Bucket="test")

        with open("tests/sample_files/test_image_1.png", mode="rb") as file1, open(
            "tests/sample_files/test_image_2.jpeg", mode="rb"
        ) as file2:
            resp = client.post(
                "/images",
                data=dict(
                    images=[(file1, "test_image_1.png"), (file2, "test_image_2.png")],
                    createThumbnails=False,
                ),
            )

        import pdb

        pdb.set_trace()

        assert resp.status_code == 200
        assert sorted(resp.json["images"], key=lambda x: x["id"]) == []

    def test_it_creates_thumbnails(self, pg: Session, client: FlaskClient, s3: Client):
        with open("tests/sample_files/test_image_1.png") as file1, open(
            "tests/sample_files/test_image_2.jpeg"
        ) as file2:
            files = [
                ("images", ("test_image_1.png", file1, "image/png")),
                ("images", ("test_image_2.png", file2, "image/jpeg")),
            ]
            resp = client.post("/images", files=files, json={"create_thumbnails": True})

        assert resp.status_code == 200
        assert sorted(resp.json["images"], key=lambda x: x["id"]) == []

    def test_it_raises_on_database_error(self, pg: Session, client: FlaskClient, s3: Client):
        with open("tests/sample_files/test_image_1.png") as file1, open(
            "tests/sample_files/test_image_2.jpeg"
        ) as file2:
            files = [
                ("images", ("test_image_1.png", file1, "image/png")),
                ("images", ("test_image_2.png", file2, "image/jpeg")),
            ]
            with patch(
                "portfolio.views.image.Session.flush",
                side_effect=[Exception("something went wrong")],
            ):
                resp = client.post("/images", data=files, json={"create_thumbnails": True})

        assert resp.status_code == 422
        assert resp.json["status"] == fail
        assert resp.json["message"] == "Bad Request: something went wrong"


class Test_UpdateImage:
    def test_it_updates_images(self, pg: Session, client: FlaskClient, s3: Client):
        pass

    def test_it_raises_on_database_error(self, pg: Session, client: FlaskClient, s3: Client):
        pass
