import functools

import boto3
import flask


def inject_db(fn=None, *, commit_on_success=False):
    def _inject_db(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            db = flask.current_app.extensions["db"]()

            try:
                result = fn(*args, **kwargs, db=db)
            except Exception:
                db.rollback()
                db.close()
                raise
            else:
                if commit_on_success:
                    db.commit()
            finally:
                db.close()

            return result

        return wrapper

    if fn is not None:
        return _inject_db(fn)
    return _inject_db


def inject_config(fn=None):
    def _inject_config(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            config = flask.current_app.extensions["config"]
            return fn(*args, **kwargs, config=config)

        return wrapper

    if fn is not None:
        return _inject_config(fn)
    return _inject_config


def inject_s3(fn=None):
    def _inject_s3(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            s3 = boto3.client("s3", region_name="us-east-1")
            return fn(*args, **kwargs, s3=s3)

        return wrapper

    if fn is not None:
        return _inject_s3(fn)
    return _inject_s3
