from flask import Blueprint

from flask_app.tasks import long_task

home_bp = Blueprint("home", __name__, url_prefix='/api/home')


@home_bp.route("/")
def index():
    task = long_task.apply_async()

    return task.id, 200
