import pendulum
from portfolio.models.image import Image
from tests import fake


def get_random_image(
    width: int | None = None,
    height: int | None = None,
    blur_hash: str | None = None,
    description: str | None = None,
    city: str | None = None,
    country: str | None = None,
    full_s3_url: str | None = None,
    thumbnail_s3_url: str | None = None,
    created_at: pendulum.DateTime | None = None,
    updated_at: pendulum.DateTime | None = None,
) -> Image:
    return Image(
        width=width or fake.pyint(max_value=1920),
        height=height or fake.pyint(max_value=1080),
        blur_hash=blur_hash or fake.pystr(),
        description=description or fake.text(),
        city=city or fake.city(),
        country=country or fake.country(),
        full_s3_url=full_s3_url or fake.image_url(),
        thumbnail_s3_url=thumbnail_s3_url or fake.image_url(),
        created_at=created_at or pendulum.now(),
        updated_at=updated_at or pendulum.now(),
    )
