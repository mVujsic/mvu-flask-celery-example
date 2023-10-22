from loguru import logger
from celery import current_app as current_celery_app


def make_celery(app):
    logger.info("Creating and registration celery...")
    celery = current_celery_app

    celery.config_from_object(app.config)
    logger.info(f"Creating Celery on {app.config['BROKER_URL']} broker")

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery

