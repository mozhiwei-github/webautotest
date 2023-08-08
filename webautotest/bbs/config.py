import os
from contants import TaskRunMode


USER_HOME_PATH = os.path.expanduser('~')
assert USER_HOME_PATH, "获取用户目录失败"
browsermob_tools_path = r""

# 兼容不同的运行方式
class DefaultConfig:
    # 运行方式
    RUN_MODE = TaskRunMode.LOCAL
    # browsermob_proxy local路径
    BROWSERMOB_PROXY_PATH = r"D:\python-project\tools\browsermob-proxy-2.1.4-bin\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"
    # BROWSERMOB_PROXY_LOCAL_PORT = 8081
    BROWSERMOB_PROXY_LOCAL_PORT = 8082
    # browsermob_proxy online
    BROWSERMOB_PROXY_SERVER_HOST = "host.docker.internal"
    BROWSERMOB_PROXY_SERVER_PORT = "58080"
    BROWSERMOB_PROXY_SERVER_PORT_PERFIX = "5"
    # selenium grid hub address
    DRIVER_REMOTE_HUB = "http://host.docker.internal:4444/wd/hub"

    #TODO:本地调试时可以额外配置HOST\PORT
    #TODO:如果采用docker需要额外配置

config = DefaultConfig()
case_id = os.environ.get("caseid")
docker_env = os.environ.get("docker_env", None)
if case_id and docker_env:
    config.RUN_MODE = TaskRunMode.REMOTE




