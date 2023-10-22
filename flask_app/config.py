import os
from dotenv import load_dotenv

load_dotenv()

BASEDIR = os.path.abspath(os.path.dirname(__name__))
DB = os.environ.get('DATABASE_URL')


class Config(object):
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(16).hex())

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", DB)

    CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE", "Europe/Berlin")
    BROKER_URL = os.getenv("BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
    CELERY_SEND_SENT_EVENT = True


# return active config
available_configs = dict(local=Config)
selected_config = os.getenv("FLASK_ENV", "local")
config = available_configs.get(selected_config, "local")
