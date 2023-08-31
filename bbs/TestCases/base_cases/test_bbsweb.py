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
        sub-step1: 官网页面打开验证
        sub-step2: 官网首页顶部栏点击跳转验证
        sub-step3: 官网首页顶部热门事件点击跳转验证
        sub-step4: 官网首页热门话题点击任一跳转验证
        sub-step5: 官网首页轮播位点击验证
        sub-step6: 官网首页展示模式切换点击验证
        sub-step7: 官网首页点击圈子打开圈子详情页
        sub-step8: 官网首页点击人气用户打开用户主页
        sub-step9: 官网首页点击文章列表打开文章详情页验证
        sub-step10: 官网首页搜索框点击推荐热词验证
        sub-step11: 官网首页搜索框点击热词验证
        """
    )
    @allure.step('step1: 官网页面基础用例验证')
    def test_bbsweb(self, chrome_driver_init):
        # proxy, driver = chrome_driver_init
        driver = chrome_driver_init
        # 浏览器窗口最大化
        # driver.maxmize_window()
        # test_url = "https://www.meizu.cn/"
        PageUrl = os.environ.get("PageUrl")
        allure.dynamic.title(f"官网自动化测试：{PageUrl}")
        with driver_step("sub-step1: 官网页面打开验证", driver):
            # bbs_page = WebPage(driver, pageurl=test_url, pagename="魅族社区官网")
            bbs_page = BbsWebpage(driver)
            original_window = driver.current_window_handle
            driver_wait_until(driver, EC.title_is("魅族社区-魅族官网论坛-魅族智能手机官方交流平台"))
            log.log_info("页面打开成功")

        with driver_step("sub-step2: 官网首页顶部栏点击跳转验证", driver):
            if not bbs_page.click_top_element(original_window=original_window):
                log.log_error("官网首页顶部栏点击跳转验证Failture")
            log.log_info("官网首页顶部栏点击跳转验证Successful")

        with driver_step("sub-step3: 官网首页顶部热门事件点击跳转验证", driver):
            if not bbs_page.click_hotevent(original_window=original_window):
                log.log_error("官网首页顶部热门事件点击跳转验证Failure")
            log.log_info("官网首页顶部热门事件点击跳转验证Successful")

        with driver_step("sub-step4: 官网首页热门话题点击任一跳转验证", driver):
            if not bbs_page.click_hottopic(original_window=original_window):
                log.log_error("官网首页热门话题点击任一跳转验证Failure")
            log.log_info("官网首页热门话题点击任一跳转验证Successful")

        with driver_step("sub-step5: 官网首页轮播位点击验证", driver):
            if not bbs_page.click_slider(original_window=original_window):
                log.log_error("官网首页点击任一轮播图跳转验证Failure")
            log.log_info("官网首页点击任一轮播图跳转验证Successful")

        with driver_step("sub-step6: 官网首页展示模式切换点击验证", driver):
            if not bbs_page.mode_switch():
                log.log_error("官网首页展示模式切换点击验证Failure")
            log.log_info("官网首页展示模式切换点击验证Successful")

        with driver_step("sub-step7: 官网首页点击圈子打开圈子详情页", driver):
            if not bbs_page.click_circle(original_window=original_window):
                log.log_error("官网首页点击圈子打开圈子详情页Failure")
            log.log_info("官网首页点击圈子打开圈子详情页Successful")

        with driver_step("sub-step8: 官网首页点击人气用户打开用户主页", driver):
            if not bbs_page.click_hotuser(original_window):
                log.log_error("官网首页点击人气用户打开用户主页Failure")
            log.log_info("官网首页点击人气用户打开用户主页Successful")

        with driver_step("sub-step9: 官网首页点击文章列表打开文章详情页验证", driver):
            if not bbs_page.click_article(original_window=original_window):
                log.log_error("官网首页点击文章列表打开文章详情页验证Failure")
            log.log_info("官网首页点击文章列表打开文章详情页验证Successful")

        with driver_step("sub-step10: 官网首页搜索框点击推荐热词验证", driver):
            if not bbs_page.click_search_random(original_window=original_window):
                log.log_error("官网首页搜索框点击推荐热词验证Failure")
            log.log_info("官网首页搜索框点击推荐热词验证Successful")

        with driver_step("sub-step11: 官网首页搜索框点击热词验证", driver):
            if not bbs_page.click_search_hotword(original_window=original_window):
                log.log_error("官网首页搜索框点击热词验证Failure")
            log.log_info("官网首页搜索框点击热词验证Successful")






if __name__ == '__main__':
    # pytest.main(["-v", "-s", __file__])
    file_path = os.path.abspath(os.path.dirname(__file__))
    allure_attach_path = os.path.join(file_path, "Outputs", "allure")
    pytest.main(["-v", "-s", __file__, '--alluredir=%s' % allure_attach_path])
    os.system("allure serve %s" % allure_attach_path)
