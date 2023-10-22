from flask import Blueprint
from flask import jsonify

from flask_app import db
from flask_app.models.message import Message

message_bp = Blueprint("messages", __name__, url_prefix="/api/messages")


@message_bp.route("/")
def index():
    messages = db.session.query(
        Message
    ).all()

    message = Message(text="Hello World")

    db.session.add(message)
    db.session.commit()

    message = dict(message=message.text)

    return jsonify(message)
