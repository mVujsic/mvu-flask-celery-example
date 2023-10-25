from flask import Blueprint

from flask_app.tasks import long_task_job

home_bp = Blueprint("home", __name__, url_prefix='/api/home')


@home_bp.route("/")
def index():
    task = long_task_job.apply_async()

    return task.id, 200
