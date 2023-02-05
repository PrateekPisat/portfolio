import flask
from configly import Config
from flask_pydantic_spec import Request, Response
from sqlalchemy.orm import Session

from portfolio import validator
from portfolio.auth import encode_auth_token
from portfolio.decorators import inject_config, inject_db
from portfolio.models.user import User
from portfolio.views.spec import User as IndividualUser
from portfolio.views.spec import UserAuthRequest, UserAuthResponse, UserResponse


@inject_db(commit_on_success=True)
@validator.validate(
    resp=Response(HTTP_200=UserResponse, HTTP_401=UserResponse, HTTP_500=UserResponse),
    tags=["User"],
)
def get(user_id: int, db: Session):
    user: User = db.query(User).filter_by(id=user_id).one_or_none()
    if not user:
        return (flask.jsonify({"status": "fail", "message": f"User {user_id} not found."}), 404)
    response = {
        "status": "success",
        "user": IndividualUser.from_db_model(user).dict(by_alias=True),
    }
    return flask.jsonify(response), 200


@inject_db(commit_on_success=True)
@inject_config
@validator.validate(
    body=Request(UserAuthRequest),
    resp=Response(HTTP_200=UserAuthResponse, HTTP_400=UserAuthResponse, HTTP_500=UserAuthResponse),
    tags=["UserAuth"],
)
def login(db: Session, config: Config):
    request_data: UserAuthRequest = flask.request.context.body
    user: User = (
        db.query(User)
        .filter_by(username=request_data.username, password=request_data.password_hash)
        .one_or_none()
    )
    if not user:
        return (flask.jsonify({"status": "fail", "message": "User not found."}), 400)

    auth_token: str = encode_auth_token(user.id, config.cryptography.key)
    return (
        flask.jsonify(
            {"status": "success", "message": "Successfully logged in.", "authToken": auth_token}
        ),
        200,
    )
