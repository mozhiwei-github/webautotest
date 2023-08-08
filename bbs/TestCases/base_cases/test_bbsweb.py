import os
import allure
import pytest
from bbs.common.log import log
from bbs.utils import driver_step, driver_wait_until
from selenium.webdriver.support import expected_conditions as EC
from bbs.common.webpage import WebPage


@allure.epic('bbs-web test')
@allure.feature('sence: bbs-web test')
class TestBbsWeb(object):
    @allure.story('case: test')
    @allure.description(
        """
        step1: open windows test
        """
    )
    def test_bbsweb(self, chrome_driver_init):
        # proxy, driver = chrome_driver_init
        driver = chrome_driver_init
        # 浏览器窗口最大化
        # driver.maxmize_window()
        test_url = "https://www.meizu.cn/"

        allure.dynamic.title(f"bbs-web-test")
        with driver_step("step1: test_bbsweb", driver):
            bbs_page = WebPage(driver, pageurl=test_url, pagename="魅族社区官网")
            original_window = driver.current_window_handle
            driver_wait_until(driver, EC.title_is("魅族社区-魅族官网论坛-魅族智能手机官方交流平台"))
            log.log_info("页面打开成功")


if __name__ == '__main__':
    # pytest.main(["-v", "-s", __file__])
    allure_attach_path = os.path.join("Outputs", "allure")
    pytest.main(["-v", "-s", __file__, '--alluredir=%s' % allure_attach_path])
    os.system("allure serve %s" % allure_attach_path)
