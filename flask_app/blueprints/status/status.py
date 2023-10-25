from flask import jsonify
from flask import Blueprint
from celery.result import AsyncResult

from flask_app.enums import CeleryTaskResultEnum

status_bp = Blueprint("status", __name__, url_prefix="/api/tasks/")


@status_bp.route("/status/<string:id>", methods=["GET"])
def get(id):
    task = AsyncResult(id)

    match task.state:
        case CeleryTaskResultEnum.PENDING.value:
            response = {"state": task.state, "status": "Pending..."}
        case CeleryTaskResultEnum.FAILURE.value:
            response = {
                "state": task.state,
                "current": task.info.get("current", 0),
                "total": task.info.get("total", 1),
                "status": task.info.get("status", ""),
            }
            if "result" in task.info:
                response["result"] = task.info["result"]
        case _:
            response = {
                "state": task.state,
                "status": str(task.info)
            }

    return jsonify(response)
