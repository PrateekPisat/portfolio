import io
from typing import List

import blurhash
import flask
import pendulum
from boto3_type_annotations.s3 import Client
from configly import Config
from flask_pydantic_spec import Request, Response
from sqlalchemy.orm import Session

from portfolio.app import validator
from portfolio.auth import decode_auth_token
from portfolio.decorators import inject_config, inject_db, inject_s3
from portfolio.models.image import Group, Image
from portfolio.views import spec


@inject_db()
@validator.validate(
    resp=Response(
        HTTP_200=spec.GetImageResponse, HTTP_404=spec.ErrorResponse, HTTP_500=spec.ErrorResponse
    ),
    tags=["Image"],
)
def get(image_id: int, db: Session):
    image: Image = db.query(Image).filter_by(id=image_id).one_or_none()
    if not image:
        return flask.jsonify({"status": "fail", "message": "Image not found."}), 404

    response = {
        "status": "success",
        "image": spec.Image.from_db_model(image).dict(by_alias=True),
    }
    return flask.jsonify(response), 200


@inject_db()
@validator.validate(
    query=spec.ListImageQuery,
    resp=Response(HTTP_200=spec.ListImageResponse, HTTP_500=spec.ErrorResponse),
    tags=["Image"],
)
def list(db: Session):
    query_params: spec.ListImageQuery = flask.request.context.query
    images_query: List[Image] = db.query(Image)
    if query_params.group_id:
        images_query = images_query.join(Group).filter(Group.id == query_params.group_id)

    response = {
        "status": "success",
        "images": [spec.Image.from_db_model(image).dict(by_alias=True) for image in images_query.order_by(Image.id)],
    }
    return flask.jsonify(response), 200


@inject_db(commit_on_success=True)
@inject_s3()
@inject_config()
@validator.validate(
    body=Request(spec.CreateImageRequest),
    headers=spec.AuthHeader,
    resp=Response(
        HTTP_200=spec.ListImageResponse, HTTP_422=spec.ErrorResponse, HTTP_500=spec.ErrorResponse
    ),
    tags=["Image"],
)
def create(db: Session, s3: Client, config: Config):
    request_data: spec.CreateImageRequest = flask.request.context.body
    request_header: spec.AuthHeader = flask.request.context.headers

    auth_token = request_header.authorization.split(" ")[1]
    decode_auth_token(auth_token, config.cryptography.key)

    bucket: str = config.aws.bucket
    images_to_add: List[Image] = []

    for image_json in request_data.images:
        if image_json.blur_hash:
            blur_hash = image_json.blur_hash
        else:
            with io.BytesIO() as file_object:
                resp = s3.get_object(Bucket=bucket, Key=image_json.full_path)
                file_object.write(resp["Body"].read())
                file_object.seek(0)
                blur_hash = blurhash.encode(file_object, x_components=4, y_components=3)

        images_to_add.append(
            Image(
                group_id=image_json.group_id,
                width=image_json.width,
                height=image_json.height,
                blur_hash=blur_hash,
                description=image_json.description,
                city=image_json.city,
                country=image_json.country,
                full_path=image_json.full_path,
                thumbnail_path=image_json.thumbnail_path,
                created_at=pendulum.now("UTC"),
            )
        )

    db.add_all(images_to_add)
    db.flush()

    return (
        flask.jsonify(
            {
                "status": "success",
                "images": [
                    spec.Image.from_db_model(image).dict(by_alias=True) for image in images_to_add
                ],
            }
        ),
        200,
    )


@inject_db()
@inject_config()
@validator.validate(
    body=Request(spec.UpdateImageRequest),
    headers=spec.AuthHeader,
    resp=Response(
        HTTP_200=spec.UpdateImageResponse, HTTP_404=spec.ErrorResponse, HTTP_500=spec.ErrorResponse
    ),
    tags=["Image"],
)
def update(image_id: int, db: Session, config: Config):
    request_data: spec.UpdateImageRequest = flask.request.context.body
    request_header: spec.AuthHeader = flask.request.context.headers

    auth_token = request_header.authorization.split(" ")[1]
    decode_auth_token(auth_token, config.cryptography.key)

    image: Image = db.query(Image).filter(Image.id == image_id).one_or_none()
    if not image:
        return (
            flask.jsonify({"status": "fail", "message": f"Image {image_id} not found"}),
            404,
        )

    image.group_id = request_data.image.group_id
    image.width = request_data.image.width
    image.height = request_data.image.height
    image.blur_hash = request_data.image.blur_hash
    image.description = request_data.image.description
    image.city = request_data.image.city
    image.country = request_data.image.country
    image.full_path = request_data.image.full_path
    image.thumbnail_path = request_data.image.thumbnail_path
    image.updated_at = pendulum.now("UTC")
    db.commit()

    return (
        flask.jsonify(
            {"status": "success", "image": spec.Image.from_db_model(image).dict(by_alias=True)}
        ),
        200,
    )
