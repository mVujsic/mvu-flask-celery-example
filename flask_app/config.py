import os
from dotenv import load_dotenv
from kombu import Queue, Exchange

load_dotenv()

BASEDIR = os.path.abspath(os.path.dirname(__name__))
DB = os.environ.get('DATABASE_URL')


class LocalConfig(object):
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(16).hex())

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", DB)

    CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE", "Europe/Berlin")
    BROKER_URL = os.getenv("BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
    CELERY_SEND_SENT_EVENT = True
    CELERY_QUEUES = (
        Queue('high', Exchange('high'), routing_key='high'),
        Queue('normal', Exchange('normal'), routing_key='normal'),
        Queue('low', Exchange('low'), routing_key='low'),
    )

    CELERY_ROUTES = {
        # -- HIGH PRIORITY QUEUE -- #
        # -- NORMAL PRIORITY QUEUE -- #
        'flask_app.tasks.long_task_job': {'queue': 'normal'},
        # -- LOW PRIORITY QUEUE -- #
    }

    CELERY_DEFAULT_QUEUE = 'normal'
    CELERY_DEFAULT_EXCHANGE = 'normal'
    CELERY_DEFAULT_ROUTING_KEY = 'normal'


class DevelopmentConfig(object):
    pass


class ProductionConfig(object):
    pass


# return active config
available_configs = dict(local=LocalConfig)
selected_config = os.getenv("FLASK_ENV", "local")
config = available_configs.get(selected_config, "local")
