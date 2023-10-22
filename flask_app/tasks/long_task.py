import time
from celery.utils.log import get_task_logger

from flask_app import db
from celery import current_app as celery_app
from flask_app.models import Message
from celery.signals import task_postrun

logger = get_task_logger(__name__)


@celery_app.task(bind=True, name='Long Task job')
def long_task(self):
    for i in range(3):
        time.sleep(1)
        messages = db.session.query(Message).all()
        logger.info(messages)
        self.update_state(
            state="PROGRESS",
            meta=
            {
                "current": i,
                "total": 10,
                "status": [m.id for m in messages]
            }
        )

    return {"status": "Task completed!"}


@task_postrun.connect()
@celery_app.task(name='Long task job post-run')
def close_connection(*args, **kwargs):
    logger.info("Closing connection....")
    db.session.close()

