#!/usr/bin/env python3
import argparse
import io
import os

import boto3
from boto3_type_annotations.s3 import Client
from configly import Config
from PIL import Image

THUMBNAIL_SIZE = (1280, 720)


def main(s3: Client, path_to_image_dir: str, bucket: str):
    for filename in os.listdir(path_to_image_dir):
        image_file = os.path.join(path_to_image_dir, filename)

        with Image.open(image_file) as image:
            full_file_path = f"full/{filename}"
            thumbnail_file_path = f"thumbnails/{filename}"
            s3.upload_file(Filename=image_file, Bucket=bucket, Key=full_file_path)

            image.thumbnail(size=THUMBNAIL_SIZE)
            with io.BytesIO() as out_file:
                image.save(out_file, format=image.format)
                out_file.seek(0)
                s3.upload_fileobj(Fileobj=out_file, Bucket=bucket, Key=thumbnail_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="UploadImages", description="Uploads images and their thumbnails to s3"
    )
    parser.add_argument(
        "path", help="Full path to the directory containing the images to be uploaded."
    )
    args = parser.parse_args()

    config = Config.from_yaml("./config.yml")
    s3 = boto3.client("s3", region_name=config.aws.region_name)
    main(s3, args.path, config.aws.bucket)
