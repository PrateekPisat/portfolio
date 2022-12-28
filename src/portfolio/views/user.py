import flask
from configly import Config
from flask_pydantic_spec import Request, Response
from setuplog import log
from sqlalchemy import exc
from sqlalchemy.orm import Session

from portfolio import validator
from portfolio.auth import decode_auth_token, encode_auth_token
from portfolio.decorators import inject_config, inject_db
from portfolio.models.user import User
from portfolio.views.spec import User as IndividualUser
from portfolio.views.spec import UserAuthHeader, UserAuthRequest, UserAuthResponse, UserResponse


@inject_db(commit_on_success=True)
@inject_config
@validator.validate(
    headers=UserAuthHeader,
    resp=Response(HTTP_200=UserResponse, HTTP_401=UserResponse, HTTP_500=UserResponse),
    tags=["User"],
)
def get(user_id: int, db: Session, config: Config):
    request_header: UserAuthHeader = flask.request.context.headers

    auth_token = request_header.authorization.split(" ")[1]
    decode_auth_token(auth_token, config.cryptography.key)

    try:
        user: User = db.query(User).filter_by(id=user_id).one()
        response = {
            "status": "success",
            "user": IndividualUser.from_db_model(user).dict(by_alias=True),
        }
        return flask.jsonify(response), 200
    except exc.SQLAlchemyError:
        return (flask.jsonify({"status": "fail", "message": "User not found."}), 401)


@inject_db(commit_on_success=True)
@inject_config
@validator.validate(
    body=Request(UserAuthRequest),
    resp=Response(HTTP_200=UserAuthResponse, HTTP_400=UserAuthResponse, HTTP_500=UserAuthResponse),
    tags=["UserAuth"],
)
def login(db: Session, config: Config):
    request_data: UserAuthRequest = flask.request.context.body
    try:
        user: User = (
            db.query(User)
            .filter_by(username=request_data.username, password=request_data.password_hash)
            .one()
        )
        log.info(f"{user.id} {config.cryptography.key}")
        auth_token: str = encode_auth_token(user.id, config.cryptography.key)
        return (
            flask.jsonify(
                {"status": "success", "message": "Successfully logged in.", "authToken": auth_token}
            ),
            200,
        )
    except exc.SQLAlchemyError:
        return (flask.jsonify({"status": "fail", "message": "User not found."}), 400)
