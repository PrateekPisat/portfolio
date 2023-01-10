from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# isort: split
from portfolio.models import image, user  # noqa
