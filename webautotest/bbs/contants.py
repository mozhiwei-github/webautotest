from enum import Enum, unique


@unique
class TaskRunMode(Enum):
    LOCAL = "本机"
    REMOTE = "远程"

