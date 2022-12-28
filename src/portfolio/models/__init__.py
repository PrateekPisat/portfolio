from strapp.sqlalchemy.model_base import declarative_base

Base = declarative_base()


# isort: split
from portfolio.models import image, user  # noqa
