from portfolio.models.user import User
from tests import fake


def get_random_user(
    id: int | None = None,
    username: str | None = None,
    password: str | None = None,
    first_name: str | None = None,
    last_name: str | None = None,
    instagram_username: str | None = None,
    bio: str | None = None,
    location: str | None = None,
    total_photos: int | None = None,
    profile_picture_path: str | None = None,
    github_username: str | None = None,
    unsplash_username: str | None = None,
    email: str | None = None,
) -> User:
    return User(
        id=id,
        username=username or fake.user_name(),
        password=password or fake.pystr(),
        first_name=first_name or fake.first_name(),
        last_name=last_name or fake.last_name(),
        instagram_username=instagram_username or fake.user_name(),
        bio=bio or fake.paragraph(),
        location=location or fake.address(),
        total_photos=total_photos or fake.pyint(max_value=100),
        profile_picture_path=profile_picture_path
        or f"thumbnails/{fake.file_name(extension='avif')}",
        github_username=github_username or fake.user_name(),
        unsplash_username=unsplash_username or fake.user_name(),
        email=email or fake.ascii_free_email(),
    )
