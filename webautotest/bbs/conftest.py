import os
from bbs.common.webdriver import get_chrome_options
import pytest
from bbs.common.browsermob_proxy import terminate_browsermob_processes, start_browsermob_proxy, get_browsermob_proxy_client
from config import config
from contants import TaskRunMode
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from bbs.common.utils import get_domain_ip


@pytest.fixture(scope="function")
def chrome_driver_init():
    """Chrome驱动初始化"""
    if config.RUN_MODE == TaskRunMode.LOCAL: # 本地运行的方式
        os.system('taskkill /im chromedriver.exe /F')
        # terminate_browsermob_processes()

        # proxy, server = start_browsermob_proxy(config.BROWSERMOB_PROXY_PATH, port=config.BROWSERMOB_PROXY_LOCAL_PORT)
        # 获取webdriver运行配置
        # chrome_options = get_chrome_options(proxy.proxy)
        chrome_options = get_chrome_options()
        # 本地运行chrome driver
        driver = webdriver.Chrome(options=chrome_options)

        yield driver
        # yield proxy, driver

        # 停止 chrome driver
        driver.quit()
        # 停止browsermob-proxy服务
        # server.stop()
    else: # 远程运行的方式
        proxy_server_ip = get_domain_ip(config.BROWSERMOB_PROXY_SERVER_HOST)
        proxy = get_browsermob_proxy_client(f'{proxy_server_ip}:{config.BROWSERMOB_PROXY_SERVER_PORT}')
        proxy_server = f'{proxy_server_ip}:{config.BROWSERMOB_PROXY_SERVER_PORT_PERFIX}{proxy.port}'
        # 获取 chrome driver运行配置
        chrome_options = get_chrome_options(proxy_server)
        # 远程运行chrome driver
        driver = webdriver.Remote(command_executor=config.DRIVER_REMOTE_HUB,
                                  desired_capabilities=DesiredCapabilities.CHROME,
                                  options=chrome_options)
        yield proxy, driver

        # 停止chrome driver
        driver.quit()
        # 关闭browsermob-proxy
        assert proxy.close() == 200







