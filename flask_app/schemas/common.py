from marshmallow import Schema
from marshmallow.fields import Str, Integer


class TaskMetaSchema(Schema):
    current = Integer()
    total = Str()
    status = Str()


task_meta_schema = TaskMetaSchema()


def set_task_meta(*arg, **kwargs):
    return kwargs
