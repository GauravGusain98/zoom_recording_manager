"""Flask configuration."""
import os

FLASK_ENV = os.environ.get("FLASK_ENV", "development")

if FLASK_ENV == "development":
    from os import path
    from dotenv import load_dotenv

    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))

TESTING = os.environ.get("TESTING")
DEBUG = os.environ.get("DEBUG")

# Database configuration
POSTGRES = {
    "user": os.environ.get("DB_USERNAME"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "connection_name": os.environ.get("CONNECTION_NAME"),
}
# For socket based connection
SQLALCHEMY_DATABASE_URI = (
    "postgresql://%(user)s:%(password)s@/%(database)s?host=%(connection_name)s/"
    % POSTGRES
)
if FLASK_ENV == "development":
    # For TCP based conneciton
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s" % POSTGRES
    )

SQLALCHEMY_TRACK_MODIFICATIONS = True
WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get("SECRET_KEY")

S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
REGION_NAME= os.environ.get("REGION_NAME")
AWS_ACCESS_KEY_ID= os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY= os.environ.get("AWS_SECRET_ACCESS_KEY")