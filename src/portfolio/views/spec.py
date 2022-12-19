import pendulum
from pydantic import BaseModel, Field

from portfolio.models import user


class UserAuthHeader(BaseModel):
    authorization: str = Field(..., alias="Authorization", min_length=1)


class UserAuthRequest(BaseModel):
    username: str = Field(..., alias="username", min_length=1)
    password_hash: str = Field(..., alias="passwordHash", min_length=1)

    class Config:
        schema_extra = {
            "example": {
                "username": "mclovin",
                "passwordHash": "\xda9\xa3\xee^kK\r2U\xbf\xef\x95`\x18\x90\xaf\xd8\x07\t",
            }
        }


class UserAuthResponse(BaseModel):
    status: str = Field(..., alias="status")
    message: str = Field(..., alias="message")
    auth_token: str | None = Field(alias="authToken")

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "message": "Successfully logged in.",
                "auth_token": "definitely_an_auth_token",
            }
        }


class User(BaseModel):
    username: str = Field(..., alias="username")
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    instagram_username: str = Field(..., alias="instagramUsername")
    bio: str = Field(..., alias="bio")
    location: str = Field(..., alias="location")
    total_photos: int = Field(..., alias="totalPhotos")
    created_at: str = Field(..., alias="createdAt")
    updated_at: str | None = Field(alias="updatedAt")

    @classmethod
    def from_db_model(cls, user: user.User):
        return cls(
            **{
                "username": user.username,
                "firstName": user.first_name,
                "lastName": user.last_name,
                "instagramUsername": user.instagram_username,
                "bio": user.bio,
                "location": user.location,
                "totalPhotos": user.total_photos,
                "createdAt": pendulum.instance(user.created_at).isoformat(),
                "updatedAt": pendulum.instance(user.updated_at).isoformat()
                if user.updated_at
                else None,
            }
        )


class UserResponse(BaseModel):
    status: str = Field(..., alias="status")
    user: User | None = Field(alias="user", required=False)
    message: str | None = Field(alias="message", required=False)

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "user": {
                    "username": "real_mclovin",
                    "first_name": "mclovin",
                    "last_name": "",
                    "instagram_username": "@real_mclovin",
                    "bio": "The real mclovin.",
                    "location": "892 Momoana St, Honolulu, HI 96820.",
                    "total_photos": 1,
                    "created_at": "2022-12-14T19:45:46.596079-05:00",
                    "updated_at": "2022-12-14T19:45:46.596079-05:00",
                },
            }
        }
