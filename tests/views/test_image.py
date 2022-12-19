import pytest
from sqlalchemy.orm import Session
from flask.testing import FlaskClient
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

        resp = client.get(f"/images")
        assert resp.status_code == 200
        assert resp.json["images"] == [spec.Image.from_db_model(image).dict(by_alias=True)]

    def test_it_returns_multiple_image(self, pg: Session, client: FlaskClient):
        images = [get_random_image(), get_random_image()]
        pg.add_all(images)
        pg.commit()

        resp = client.get(f"/images")
        assert resp.status_code == 200
        assert resp.json["images"] == [
            spec.Image.from_db_model(image).dict(by_alias=True) for image in images
        ]
