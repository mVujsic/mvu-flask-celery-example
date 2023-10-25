import time
from celery.utils.log import get_task_logger

from flask_app import db
from celery import current_app as celery_app

from flask_app.enums import CeleryTaskResultEnum
from flask_app.models import Message
from celery.signals import task_postrun

from flask_app.schemas.common import set_task_meta

logger = get_task_logger(__name__)


@celery_app.task(bind=True)
def long_task_job(self):
    total_sleep = 10

    for i in range(10):
        time.sleep(1)
        messages = db.session.query(Message).all()
        self.update_state(
            state=CeleryTaskResultEnum.PENDING.value,
            meta=set_task_meta(
                current=i,
                total=total_sleep,
                status=[m.id for m in messages]
            )
        )

    return {"status": "Task completed!"}


@task_postrun.connect()
@celery_app.task
def close_connection(*args, **kwargs):
    logger.info("Closing connection....")
    db.session.close()

