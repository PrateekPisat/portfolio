import flask
import pendulum
from configly import Config
from flask_pydantic_spec import Request, Response
from sqlalchemy.orm import Session

from portfolio.app import validator
from portfolio.auth import decode_auth_token
from portfolio.decorators import inject_config, inject_db
from portfolio.models.image import Group
from portfolio.views import spec


@inject_db()
@validator.validate(
    resp=Response(
        HTTP_200=spec.GetGroupResponse,
        HTTP_404=spec.ErrorResponse,
        HTTP_500=spec.ErrorResponse,
    ),
    tags=["Group"],
)
def get(db: Session, group_id: int):
    group: Group | None = db.query(Group).filter(Group.id == group_id).one_or_none()
    if group is None:
        return flask.jsonify({"status": "fail", "message": "Group not found."}), 404

    response = {
        "status": "success",
        "group": spec.Group.from_db_model(group).dict(by_alias=True),
    }
    return flask.jsonify(response), 200


@inject_db()
@validator.validate(
    resp=Response(
        HTTP_200=spec.ListGroupResponse,
        HTTP_404=spec.ErrorResponse,
        HTTP_500=spec.ErrorResponse,
    ),
    tags=["Group"],
)
def list(db: Session):
    response = {
        "status": "success",
        "groups": [
            spec.Group.from_db_model(group).dict(by_alias=True) for group in db.query(Group)
        ],
    }
    return flask.jsonify(response), 200


@inject_db(commit_on_success=True)
@inject_config()
@validator.validate(
    body=Request(spec.CreateGroupRequest),
    headers=spec.AuthHeader,
    resp=Response(
        HTTP_200=spec.CreateGroupResponse,
        HTTP_401=spec.ErrorResponse,
        HTTP_422=spec.ErrorResponse,
        HTTP_500=spec.ErrorResponse,
    ),
    tags=["Group"],
)
def create(db: Session, config: Config):
    request_body: spec.CreateGroupRequest = flask.request.context.body
    request_header: spec.AuthHeader = flask.request.context.headers
    auth_token = request_header.authorization.split(" ")[1]
    decode_auth_token(auth_token, config.cryptography.key)

    groups = [Group(name=group.name, id=group.id) for group in request_body.groups]
    db.add_all(groups)
    db.commit()

    response = {
        "status": "success",
        "groups": [
            spec.Group.from_db_model(group).dict(by_alias=True) for group in db.query(Group)
        ],
    }
    return flask.jsonify(response), 200


@inject_db()
@inject_config()
@validator.validate(
    body=Request(spec.UpdateGroupRequest),
    headers=spec.AuthHeader,
    resp=Response(
        HTTP_200=spec.UpdateGroupResponse,
        HTTP_401=spec.ErrorResponse,
        HTTP_404=spec.ErrorResponse,
        HTTP_422=spec.ErrorResponse,
        HTTP_500=spec.ErrorResponse,
    ),
    tags=["Group"],
)
def update(db: Session, config: Config, group_id: int):
    request_header: spec.AuthHeader = flask.request.context.headers
    auth_token = request_header.authorization.split(" ")[1]
    decode_auth_token(auth_token, config.cryptography.key)

    group: Group = db.query(Group).filter(Group.id == group_id).one_or_none()
    if group is None:
        return flask.jsonify({"status": "fail", "message": "Group not found."}), 404

    request_body: spec.UpdateGroupRequest = flask.request.context.body
    group.name = request_body.name
    group.updated_at = pendulum.now("UTC")

    response = {
        "status": "success",
        "group": spec.Group.from_db_model(group).dict(by_alias=True),
    }
    return flask.jsonify(response), 200
