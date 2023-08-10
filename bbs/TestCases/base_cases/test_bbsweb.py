import os
import allure
import pytest
from bbs.common.log import log
from bbs.utils import driver_step, driver_wait_until
from selenium.webdriver.support import expected_conditions as EC
from bbs.common.webpage import WebPage
from bbs.PageObject.bbs_web_page import BbsWebpage
from bbs.contants import TopElement


@allure.epic('官网页面自动化测试epic')
@allure.feature('官网页面自动化测试feature')
class TestBbsWeb(object):
    @allure.story('官网页面自动化测试story')
    @allure.description(
        """
        step1: 官网页面打开验证
        step2: 官网首页顶部栏点击跳转验证
        """
    )
    @allure.step('step1: 官网页面打开验证')
    def test_bbsweb(self, chrome_driver_init):
        # proxy, driver = chrome_driver_init
        driver = chrome_driver_init
        # 浏览器窗口最大化
        # driver.maxmize_window()
        # test_url = "https://www.meizu.cn/"
        PageUrl = os.environ.get("PageUrl")
        allure.dynamic.title(f"官网自动化测试：{PageUrl}")

        with driver_step("step1: 官网页面打开验证", driver):
            # bbs_page = WebPage(driver, pageurl=test_url, pagename="魅族社区官网")
            bbs_page = BbsWebpage(driver)
            original_window = driver.current_window_handle
            driver_wait_until(driver, EC.title_is("魅族社区-魅族官网论坛-魅族智能手机官方交流平台"))
            log.log_info("页面打开成功")

        with driver_step("step2: 官网首页顶部栏点击跳转验证", driver):
            if not bbs_page.click_top_element(original_window=original_window):
                log.log_error("官网首页顶部栏点击跳转验证Failture")
            log.log_info("官网首页顶部栏点击跳转验证Successful")





if __name__ == '__main__':
    # pytest.main(["-v", "-s", __file__])
    file_path = os.path.abspath(os.path.dirname(__file__))
    allure_attach_path = os.path.join(file_path, "Outputs", "allure")
    pytest.main(["-v", "-s", __file__, '--alluredir=%s' % allure_attach_path])
    os.system("allure serve %s" % allure_attach_path)
