from bbs.common.webpage import WebPage
import allure
import os
from selenium.webdriver.common.by import By
from bbs.utils import driver_wait_until
from selenium.webdriver.support import expected_conditions as EC
from bbs.contants import MainUrl, TopElement
from bbs.utils import back_to_original_window

class BbsWebpage(WebPage):
    PageUrl = "https://www.meizu.cn/"
    PageName = "魅族社区官网"

    os.environ['PageUrl'] = PageUrl

    def click_top_element(self, topelement_name=None, original_window=None):
        """
        顶部栏元素点击
        @param topelement_name: 点击的模块名
        @return:
        """
        # if topelement_name == "logo":
        item = self.find_element((By.CSS_SELECTOR, '._title_14m5i_126'), multiple=False)
        self.element_click(element=item, element_name=TopElement.LOGO.value)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击logo打开{MainUrl.STORE.value}"):
            self.log_error(f"官网首页顶部栏点击{TopElement.LOGO.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.STORE.value}加载")
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.log_info(f"官网首页顶部栏点击{TopElement.LOGO.value}跳转验证Successful")
        self.sleep(3)

        # if topelement_name == "社区":
        item = self.find_element((By.XPATH, '//div[@class="_tabs_inner_14m5i_108"]//ul/li[1]'))
        self.element_click(element=item, element_name=TopElement.BBS.value)
        if not self.get_current_url() == MainUrl.BBS.value:
            self.log_error(f"官网首页顶部栏点击{TopElement.BBS.value}跳转验证Failture")
        self.sleep(3)
        self.log_info(f"官网首页顶部栏点击{TopElement.BBS.value}跳转验证Successful")

        # if topelement_name == "商城":
        item = self.find_element((By.XPATH, '//div[@class="_tabs_inner_14m5i_108"]//ul/li[2]'))
        self.element_click(element=item, element_name=TopElement.STORE.value)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击商城打开{MainUrl.STORE.value}"):
            self.log_error(f"官网首页顶部栏点击{TopElement.STORE.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.STORE.value}加载")
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(3)
        self.log_info(f"官网首页顶部栏点击{TopElement.STORE.value}跳转验证Successful")

        # if topelement_name == "服务":
        item = self.find_element((By.XPATH, '//div[@class="_tabs_inner_14m5i_108"]//ul/li[3]'))
        self.element_click(element=item, element_name=TopElement.SERVER.value)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击服务打开{MainUrl.CARE.value}"):
            self.log_error(f"官网首页顶部栏点击{TopElement.SERVER.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.CARE.value}加载")
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(3)
        self.log_info(f"官网首页顶部栏点击{TopElement.SERVER.value}跳转验证Successful")

        # if topelement_name == "Flyme":
        item = self.find_element((By.XPATH, '//div[@class="_tabs_inner_14m5i_108"]//ul/li[4]'))
        self.element_click(element=item, element_name=TopElement.FLYME.value)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击Flyme打开{MainUrl.FLYME.value}"):
            self.log_error(f"官网首页顶部栏点击{TopElement.SERVER.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.FLYME.value}加载")
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(3)
        self.log_info(f"官网首页顶部栏点击{TopElement.FLYME.value}跳转验证Successful")

        # if topelement_name == "App下载":
        item = self.find_element((By.XPATH, '//div[@class="_tabs_inner_14m5i_108"]//ul/li[5]'))
        self.element_click(element=item, element_name=TopElement.DOWNLOAD.value)
        if not self.get_current_url() == MainUrl.INTRODUCE.value:
            self.log_error(f"官网首页顶部栏点击{TopElement.DOWNLOAD.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.INTRODUCE.value}加载")
        self.back(expect_url=MainUrl.BBS.value)
        self.sleep(3)
        self.log_info(f"官网首页顶部栏点击{TopElement.DOWNLOAD.value}跳转验证Successful")
        return True











