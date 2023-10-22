from enum import Enum


class ApplicationTypeEnum(Enum):
    API = 'api'
    WORKER = 'worker'


class CeleryTaskResultEnum(Enum):
    PENDING = 'PENDING'
    FAILURE = 'FAILURE'
