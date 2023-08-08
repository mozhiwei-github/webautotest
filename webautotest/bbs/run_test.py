from bbs.common.yaml_reader import YamlReader
from bbs.common.log import log
import pytest
import os.path
from bbs.common.contants import EnvVar
"""执行启动脚本"""

def run_pytest(case_list, serve, generate):
    file_path = os.path.abspath(os.path.dirname(__file__))
    # allure报告
    allure_attach_path = os.path.join("Outputs", "allure")
    allure_html_path = os.path.join("Outputs", "report")
    allure_absolute_path = os.path.join(file_path, allure_attach_path)
    if os.path.exists(allure_absolute_path):
        for file in os.listdir(allure_absolute_path):
            os.remove(os.path.join(allure_absolute_path, file))

    pytest_args = [
        '-s',
        '-q',
        '--tb=short',
        *case_list,
        '--alluredir=%s' % allure_attach_path,
    ]

    # if smb:
    #     pytest_args.append(f"--smb={smb}")

    pytest.main(pytest_args)

    if os.listdir(allure_absolute_path):
        # 存在generate参数，生成html报告
        if generate:
            log.log_info("*****生成allure html报告中*****")
            os.system("allure generate %s -o %s" % (allure_attach_path, allure_html_path))
        # 存在serve参数，启动本地服务查看html报告
        if serve:
            log.log_info("*****启动allure报告服务中*****")
            os.system("allure serve %s" % allure_attach_path)
    else:
        log.log_info("allure日志目录为空")

if __name__ == '__main__':
    import logging
    import argparse
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "common", "config", "config.yml")
    reader = YamlReader()
    config_data = reader.read_yaml(config_path)

    parser = argparse.ArgumentParser("For web-auto test")
    parser.add_argument("case", help="测试用例文件路径，多个文件用英文分割。")
    parser.add_argument("-s", "--serve", action='store_true',
                        help="是否以allure服务形式查看报告，ps：需要本机已经安装allure命令")
    parser.add_argument("-g", "--generate", action='store_true',
                        help="是否生成allure报告。ps：需本机已经安装allure命令")
    # parser.add_argument("--smb", help="smb地址，使用smb中文件替换对应测试文件")
    args = parser.parse_args()

    case_list = args.case.split(",")
    run_case_list = []

    def match_project_case(case):
        # 遍历项目找到相应案例路径
        for project_folder in config_data:
            project_info = config_data[project_folder]
            if not project_info:
                continue
            # 项目路径不存在的时候跳过
            project_folder_path = os.path.join(os.getcwd(), project_folder)
            if not project_folder_path:
                continue
            # 项目案例配置不存在时跳过
            project_case_list = project_info.get("cases", None)
            if not project_case_list:
                continue
            for project_case in project_case_list:
                project_case_path = project_case["param"]
                # 案例路径模糊匹配
                if case == project_case_path or project_case_path.endswith(case):
                    run_case_list.append(os.path.join(project_folder, project_case_path))
                    return

    for case_path in case_list:
        match_project_case(case_path)
    assert run_case_list, "测试用例列表匹配失败"
    yaml_result = reader.read_yaml(os.path.join(os.getcwd(), "bbs", "common", "config", "common.yml"))

    # 设置日志级别环境变量
    debug_config = yaml_result.get("debug", False)
    if debug_config:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    os.environ[EnvVar.UITEST_LOG_LEVEL.value] = str(log_level)

    # run_pytest(run_case_list, args.serve, args.generate, args.smb)
    run_pytest(run_case_list, args.serve, args.generate)





