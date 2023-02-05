#!/usr/bin/env python3
import io
from typing import List

import blurhash
import boto3
import sqlalchemy
from boto3_type_annotations.s3 import Client
from configly import Config
from PIL import Image
from setuplog import log, setup_logging
from sqlalchemy.orm import scoped_session, Session, sessionmaker

from portfolio import models


def main(s3: Client, session: Session, bucket: str):
    images_to_store: List[models.image.Image] = []

    for content in s3.list_objects_v2(Bucket=bucket, Prefix="full/")["Contents"][1:]:
        log.info(f"Downloading file {content['Key']}")
        with io.BytesIO(s3.get_object(Bucket=bucket, Key=content["Key"])["Body"].read()) as in_file:
            image = Image.open(in_file)
            in_file.seek(0)
            blur_hash = blurhash.encode(in_file, x_components=4, y_components=3)

            images_to_store.append(
                models.image.Image(
                    width=image.width,
                    height=image.height,
                    blur_hash=blur_hash,
                    city="Boston, MA",
                    country="United States",
                    full_path=f"{content['Key']}",
                    thumbnail_path=f"{content['Key'].replace('full', 'thumbnail')}",
                )
            )
    session.add_all(images_to_store)
    session.commit()


if __name__ == "__main__":
    config = Config.from_yaml("./config.yml")
    s3 = boto3.client("s3", region_name=config.aws.region_name)
    setup_logging(config.logging.level)

    url = sqlalchemy.engine.url.URL.create(**config.database.to_dict())
    engine = sqlalchemy.create_engine(url)
    session_factory = sessionmaker()
    Session = scoped_session(session_factory)
    session = Session(bind=engine)

    main(s3, session, config.aws.bucket)
