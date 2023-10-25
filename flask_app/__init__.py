from flask import Flask
from loguru import logger
from flask_celeryext import FlaskCeleryExt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_app.config import config
from flask_app.enums import ApplicationTypeEnum
from flask_app.celery import make_celery


db = SQLAlchemy()
exc_celery = FlaskCeleryExt(create_celery_app=make_celery)
migrate = Migrate()


def _register_blueprints(app: Flask) -> None:
    from flask_app.blueprints.message import message_bp
    from flask_app.blueprints.status import status_bp
    from flask_app.blueprints.home import home_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(message_bp)
    app.register_blueprint(status_bp)


def create_app():
    logger.info('Creating app....')
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    exc_celery.init_app(app)

    app.config.from_object(config)
    logger.info('Application set.')

    _register_blueprints(app)

    return app



