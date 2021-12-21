from __future__ import annotations

from typing import Any, Dict

from pydantic.dataclasses import dataclass
import pendulum


@dataclass
class Location:
    name: str
    city: str
    country: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Location:
        return cls(name=data["name"], city=data["city"], country=data["country"])


@dataclass
class Image:
    id: int
    created_at: pendulum.DateTime
    updated_at: pendulum.DateTime
    width: int
    height: int
    blur_hash: str
    description: str
    location: Location
    urls: Dict[str, str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Image:
        return cls(
            id=data["id"],
            created_at=pendulum.from_format(data["created_at"], "YYYY-MM-DDTHH:mm:ssZ"),
            updated_at=pendulum.from_format(data["updated_at"]),
            width=data["width"],
            height=data["height"],
            blur_hash=data["blur_hash"],
            description=data["description"],
            location=Location.from_dict(data["location"]),
            urls=data["urls"],
        )