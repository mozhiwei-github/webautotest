from enum import Enum, unique
import os

base_dir = os.path.dirname(os.path.dirname(__file__))
logs_file = os.path.join(base_dir, "logs")

@unique
class ServerHost(Enum):
    """服务器地址"""
    #TODO:补充服务配置
    CDS = "111"
    AUTO_TEST_HOST = "222"


@unique
class EnvVar(Enum):
    """环境变量"""
    UITEST_LOG_LEVEL = "UITEST_LOG_LEVEL"  # UI自动化测试日志等级
    KVM_ENV = "kvm_env"  # KVM虚拟机环境
    CASE_ID = "caseid"  # 用例ID
    CASE_NAME = "casename"  # 用例名称
    USERNAME = "username"  # 触发用户
    AUTO_TEST_ENV = "autotestenv"  # 自动化测试环境