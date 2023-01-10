from ast import Dict
from typing import List

import flask
from flask_pydantic_spec import Request, Response
from sqlalchemy import exc
from sqlalchemy.orm import Session
from boto3_type_annotations.s3 import Client
import PIL
from configly import Config
import blurhash


from portfolio.app import validator
from portfolio.decorators import inject_db, inject_s3, inject_config
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


@inject_db(commit_on_success=True)
@inject_s3()
@inject_config()
@validator.validate(
    body=Request(spec.CreateImageRequest),
    resp=Response(
        HTTP_200=spec.ListImageResponse, HTTP_422=spec.ErrorResponse, HTTP_500=spec.ErrorResponse
    ),
    tags=["Image"],
)
def create(db: Session, s3: Client, config: Config):
    image_files = flask.request.files.getlist("images")
    request_data: spec.CreateImageRequest = flask.request.context.body
    bucket: str = config.aws.bucket
    images_to_add: List[Image] = []

    for image_file in image_files:
        with PIL.Image.open(image_file) as image:
            full_file_path = f"full/{image.filename}"
            thumbnail_file_path = None
            blur_hash = blurhash.encode(image_file, x_components=4, y_components=3)
            s3.upload_fileobj(Fileobj=image_file, Bucket=bucket, Key=full_file_path)
            if request_data.create_thumbnails:
                thumbnail_file_path = f"thumbnails/{image.filename}"
                image.thumbnail()
                s3.upload_fileobj(Fileobj=image_file, Bucket=bucket, Key=thumbnail_file_path)

            images_to_add.append(
                Image(
                    width=image.width,
                    height=image.height,
                    blur_hash=blur_hash,
                    full_s3_url=f"https://{bucket}.s3.amazonaws.com/{full_file_path}",
                    thumbnail_s3_url=f"https://{bucket}.s3.amazonaws.com/{thumbnail_file_path}"
                    if thumbnail_file_path
                    else None,
                )
            )
    try:
        db.add_all(images_to_add)
        db.flush()

        return (
            flask.jsonify(
                {
                    "status": "success",
                    "images": [spec.Image.from_db_model(image) for image in images_to_add],
                }
            ),
            200,
        )
    except exc.SQLAlchemyError as e:
        return flask.jsonify({"status": "fail", "message": f"Bad request: {str(e)}"}), 422


@inject_db()
@validator.validate(
    body=Request(spec.UpdateImageRequest),
    resp=Response(
        HTTP_200=spec.ListImageResponse, HTTP_401=spec.ErrorResponse, HTTP_500=spec.ErrorResponse
    ),
    tags=["Image"],
)
def update(db: Session):
    request_data: spec.UpdateImageRequest = flask.request.context.body
    try:
        image_ids = [image_spec["id"] for image_spec in request_data.image_specs]
        images_to_update_by_id: Dict[int, Image] = {
            image.id: image for image in db.query(Image).filter(Image.id.in_(image_ids))
        }

        for image_spec in request_data.image_specs:
            image = images_to_update_by_id[image_spec.image_id]
            image.city = image_spec.city
            image.description = image_spec.description
            image.country - image_spec.country

        db.commit()
        return (
            flask.jsonify(
                {
                    "status": "success",
                    "images": [
                        spec.Image.from_db_model(image) for image in images_to_update_by_id.values()
                    ],
                }
            ),
            200,
        )
    except exc.SQLAlchemyError as e:
        return flask.jsonify({"status": "fail", "message": f"Bad request: {str(e)}"}), 422
