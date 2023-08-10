from bbs.common.webpage import WebPage
import allure
import os
from selenium.webdriver.common.by import By
from bbs.utils import driver_wait_until
from selenium.webdriver.support import expected_conditions as EC
from bbs.contants import MainUrl

class BbsWebpage(WebPage):
    PageUrl = "https://www.meizu.cn/"
    PageName = "魅族社区官网"

    os.environ['PageUrl'] = PageUrl

    def click_top_element(self, topelement_name=None):
        """
        顶部栏元素点击
        @param topelement_name: 点击的模块名
        @return:
        """
        if topelement_name == "logo":
            item = self.find_element((By.XPATH, '//div/svg/g[@id="red-icon_文字"]'), multiple=False)
            self.element_click(element=item, element_name=topelement_name)
            self.wait_util(EC.number_of_windows_to_be(2), message=f"点击logo打开{MainUrl.STORE.value}")
            if not self.back():
                return False
            return True
        if topelement_name == "社区":
            item = self.find_element((By.XPATH, '//div[@class="_tabs_inner_14m5i_108"]//ul/li[0]'))
            self.element_click(element=item, element_name=topelement_name)
            self.wait_util(EC.number_of_windows_to_be(2), message=f"点击社区打开{MainUrl.BBS.value}")
            if not self.back():
                return False
            return True
        if topelement_name == "商城":
            item = self.find_element((By.XPATH, '//div[@class="_tabs_inner_14m5i_108"]//ul/li[1]'))
            self.element_click(element=item, element_name=topelement_name)
            self.wait_util(EC.number_of_windows_to_be(2), message=f"点击商城打开{MainUrl.STORE.value}")
            if not self.back():
                return False
            return True









