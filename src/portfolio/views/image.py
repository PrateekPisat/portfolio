from typing import List

import flask
from flask_pydantic_spec import Response
from sqlalchemy import exc
from sqlalchemy.orm import Session

from portfolio.app import validator
from portfolio.decorators import inject_db
from portfolio.models.image import Image
from portfolio.views import spec


@inject_db()
@validator.validate(
    resp=Response(
        HTTP_200=spec.GetImageResponse, HTTP_401=spec.ErrorResponse, HTTP_500=spec.ErrorResponse
    ),
    tags=["Image"],
)
def get(image_id: int, db: Session):
    try:
        image: Image = db.query(Image).filter_by(id=image_id).one()
        response = {
            "status": "success",
            "image": spec.Image.from_db_model(image).dict(by_alias=True),
        }
        return flask.jsonify(response), 200
    except exc.SQLAlchemyError:
        return flask.jsonify({"status": "fail", "message": "Image not found."}), 404


@inject_db()
@validator.validate(
    resp=Response(
        HTTP_200=spec.ListImageResponse, HTTP_401=spec.ErrorResponse, HTTP_500=spec.ErrorResponse
    ),
    tags=["Image"],
)
def list(db: Session):
    images: List[Image] = db.query(Image).all()
    response = {
        "status": "success",
        "images": [spec.Image.from_db_model(image).dict(by_alias=True) for image in images],
    }
    return flask.jsonify(response), 200
