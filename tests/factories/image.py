import pendulum

from portfolio.models.image import Group, Image
from tests import fake


def get_random_image(
    id: int | None = None,
    group_id: int | None = None,
    width: int | None = None,
    height: int | None = None,
    blur_hash: str | None = None,
    description: str | None = None,
    city: str | None = None,
    country: str | None = None,
    full_path: str | None = None,
    thumbnail_path: str | None = None,
    group: Group | None = None,
    created_at: pendulum.DateTime | None = None,
    updated_at: pendulum.DateTime | None = None,
) -> Image:
    if group_id is None and group is None:
        group = get_random_group()

    return Image(
        id=id,
        group_id=group_id,
        width=width or fake.pyint(max_value=1920),
        height=height or fake.pyint(max_value=1080),
        blur_hash=blur_hash or fake.pystr(),
        description=description or fake.text(),
        city=city or fake.city(),
        country=country or fake.country(),
        full_path=full_path or fake.image_url(),
        thumbnail_path=thumbnail_path or fake.image_url(),
        created_at=created_at or pendulum.now(),
        updated_at=updated_at or pendulum.now(),
        group=group,
    )


def get_random_group(id: int | None = None, name: str | None = None) -> Group:
    return Group(id=id, name=fake.pystr())
