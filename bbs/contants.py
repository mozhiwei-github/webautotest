from enum import Enum, unique


@unique
class TaskRunMode(Enum):
    LOCAL = "本机"
    REMOTE = "远程"

@unique
class TopElement(Enum):
    LOGO = "logo"
    BBS = "社区"
    STORE = "商城"
    SERVER = "服务"
    FLYME = "Flyme"
    DOWNLOAD = "App下载"

@unique
class MainUrl(Enum):
    STORE = "https://www.meizu.com/"
    BBS = "https://www.meizu.cn/"
    CARE = "https://care.meizu.com/"
    FLYME = "https://www.flyme.cn/"
    INTRODUCE = "https://www.meizu.cn/introduce/"