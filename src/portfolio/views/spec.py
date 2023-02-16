from typing import List

import pendulum
from pydantic import BaseModel, Field

from portfolio.models import image, user


class AuthHeader(BaseModel):
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
    github_username: str | None = Field(alias="githubUsername")
    unsplash_username: str | None = Field(alias="unsplashUsername")
    email: str | None = Field(alias="email")
    profile_picture_path: str | None = Field(alias="profilePicturePath")
    about_picture_path: str | None = Field(alias="aboutPicturePath")
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
                "profilePicturePath": user.profile_picture_path,
                "githubUsername": user.github_username,
                "unsplashUsername": user.unsplash_username,
                "email": user.email,
                "aboutPicturePath": user.about_picture_path,
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


class Image(BaseModel):
    id: int | None = Field(alias="id", required=False)
    width: int = Field(..., alias="width")
    height: int = Field(..., alias="height")
    blur_hash: str | None = Field(alias="blurHash", required=False)
    description: str | None = Field(alias="description")
    city: str = Field(..., alias="city")
    country: str = Field(..., alias="country")
    full_path: str = Field(..., alias="fullPath")
    thumbnail_path: str = Field(..., alias="thumbnailPath")
    created_at: str | None = Field(alias="createdAt", required=False)
    updated_at: str | None = Field(alias="updatedAt", required=False)

    @classmethod
    def from_db_model(cls, model: image.Image):
        return cls(
            **{
                "id": model.id,
                "width": model.width,
                "height": model.height,
                "blurHash": model.blur_hash,
                "description": model.description,
                "city": model.city,
                "country": model.country,
                "fullPath": model.full_path,
                "thumbnailPath": model.thumbnail_path,
                "createdAt": pendulum.instance(model.created_at).isoformat(),
                "updatedAt": pendulum.instance(model.updated_at).isoformat()
                if model.updated_at
                else None,
            }
        )


class ImageSpec(BaseModel):
    image_id: int = Field(..., alias="imageId")
    description: str = Field(..., alias="description", min_length=1)
    city: str = Field(..., alias="city", min_length=1)
    country: str = Field(..., alias="country", min_length=1)


class GetImageResponse(BaseModel):
    status: str = Field(..., alias="status")
    image: Image = Field(..., alias="image")

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "image": {
                    "id": 1,
                    "width": 1920,
                    "height": 1080,
                    "blurHash": "ak12j3h",
                    "description": "Image of a bridge.",
                    "city": "Boston",
                    "country": "United States",
                    "fullPath": "s3://some-bucket/full/bridge.jpg",
                    "thumbnailPath": "s3://some-bucket/thumbnail/bridge.jpg",
                    "created_at": "2022-12-14T19:45:46.596079-05:00",
                    "updated_at": "2022-12-14T19:45:46.596079-05:00",
                },
            }
        }


class ListImageResponse(BaseModel):
    status: str = Field(..., alias="status")
    images: List[Image] = Field(..., alias="images")

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "images": [
                    {
                        "id": 1,
                        "width": 1920,
                        "height": 1080,
                        "blurHash": "ak12j3h",
                        "description": "Image of a bridge.",
                        "city": "Boston",
                        "country": "United States",
                        "fullPath": "s3://some-bucket/full/bridge.jpg",
                        "thumbnailPath": "s3://some-bucket/thumbnail/bridge.jpg",
                        "created_at": "2022-12-14T19:45:46.596079-05:00",
                        "updated_at": "2022-12-14T19:45:46.596079-05:00",
                    }
                ],
            }
        }


class CreateImageRequest(BaseModel):
    images: List[Image] = Field(..., alias="images")

    class Config:
        schema_extra = {
            "example": {
                "status": "success",
                "images": [
                    {
                        "width": 1920,
                        "height": 1080,
                        "blurHash": "ak12j3h",
                        "description": "Image of a bridge.",
                        "city": "Boston",
                        "country": "United States",
                        "fullPath": "s3://some-bucket/full/bridge.jpg",
                        "thumbnailPath": "s3://some-bucket/thumbnail/bridge.jpg",
                    }
                ],
            }
        }


class UpdateImageRequest(BaseModel):
    image: Image = Field(..., alias="image")

    class Config:
        schema_extra = {
            "example": {
                "image": {
                    "id": 1,
                    "width": 1920,
                    "height": 1080,
                    "blurHash": "ak12j3h",
                    "description": "Image of a bridge.",
                    "city": "Boston",
                    "country": "United States",
                    "fullPath": "s3://some-bucket/full/bridge.jpg",
                    "thumbnailPath": "s3://some-bucket/thumbnail/bridge.jpg",
                    "created_at": "2022-12-14T19:45:46.596079-05:00",
                    "updated_at": "2022-12-14T19:45:46.596079-05:00",
                }
            }
        }


class UpdateImageResponse(BaseModel):
    status: str = Field(..., alias="status")
    image: Image = Field(..., alias="image")


class ErrorResponse(BaseModel):
    status: str = "failed"
    message: str = Field(..., alias="message", min_length=1)

    class Config:
        schema_extra = {"example": {"status": "failed", "message": "Something went wrong."}}
