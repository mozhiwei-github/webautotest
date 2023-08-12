from bbs.common.webpage import WebPage
import allure
import os
from selenium.webdriver.common.by import By
from bbs.utils import driver_wait_until
from selenium.webdriver.support import expected_conditions as EC
from bbs.contants import MainUrl, TopElement
from bbs.utils import back_to_original_window
from bbs.item_code import TopElementItem, TopHotEvent, HotTopic, TopSwiper
import random

class BbsWebpage(WebPage):
    PageUrl = "https://www.meizu.cn/"
    PageName = "魅族社区官网"

    os.environ['PageUrl'] = PageUrl

    def click_top_element(self, topelement_name=None, original_window=None):
        """
        顶部栏元素点击
        @param topelement_name: 点击的模块名
        @param original_window: 初始窗口句柄ID
        @return:
        """
        # if topelement_name == "logo":
        item = self.find_element((By.CSS_SELECTOR, TopElementItem.LOGO.value), multiple=False)
        self.element_click(element=item, element_name=TopElement.LOGO.value)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击logo打开{MainUrl.STORE.value}"):
            self.log_error(f"官网首页顶部栏点击{TopElement.LOGO.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.STORE.value}加载", time_wait=1)
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        self.log_info(f"官网首页顶部栏点击{TopElement.LOGO.value}跳转验证Successful")


        # if topelement_name == "社区":
        item = self.find_element((By.XPATH, TopElementItem.BBS.value))
        self.element_click(element=item, element_name=TopElement.BBS.value)
        if not self.get_current_url() == MainUrl.BBS.value:
            self.log_error(f"官网首页顶部栏点击{TopElement.BBS.value}跳转验证Failture")
        self.log_info(f"官网首页顶部栏点击{TopElement.BBS.value}跳转验证Successful")
        self.sleep(1)

        # if topelement_name == "商城":
        item = self.find_element((By.XPATH, TopElementItem.STORE.value))
        self.element_click(element=item, element_name=TopElement.STORE.value)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击商城打开{MainUrl.STORE.value}"):
            self.log_error(f"官网首页顶部栏点击{TopElement.STORE.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.STORE.value}加载", time_wait=1)
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        self.log_info(f"官网首页顶部栏点击{TopElement.STORE.value}跳转验证Successful")

        # if topelement_name == "服务":
        item = self.find_element((By.XPATH, TopElementItem.SERVER.value))
        self.element_click(element=item, element_name=TopElement.SERVER.value)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击服务打开{MainUrl.CARE.value}"):
            self.log_error(f"官网首页顶部栏点击{TopElement.SERVER.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.CARE.value}加载", time_wait=1)
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        self.log_info(f"官网首页顶部栏点击{TopElement.SERVER.value}跳转验证Successful")

        # if topelement_name == "Flyme":
        item = self.find_element((By.XPATH, TopElementItem.FLYME.value))
        self.element_click(element=item, element_name=TopElement.FLYME.value)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击Flyme打开{MainUrl.FLYME.value}"):
            self.log_error(f"官网首页顶部栏点击{TopElement.SERVER.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.FLYME.value}加载", time_wait=1)
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        self.log_info(f"官网首页顶部栏点击{TopElement.FLYME.value}跳转验证Successful")

        # if topelement_name == "App下载":
        item = self.find_element((By.XPATH, TopElementItem.DOWNLOAD.value))
        self.element_click(element=item, element_name=TopElement.DOWNLOAD.value)
        if not self.get_current_url() == MainUrl.INTRODUCE.value:
            self.log_error(f"官网首页顶部栏点击{TopElement.DOWNLOAD.value}跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.INTRODUCE.value}加载", time_wait=1)
        self.back(expect_url=MainUrl.BBS.value)
        self.sleep(1)
        self.log_info(f"官网首页顶部栏点击{TopElement.DOWNLOAD.value}跳转验证Successful")
        return True

    def click_hotevent(self, original_window=None):
        """
        点击首页顶部热门事件推广位
        @param original_window: 初始窗口句柄ID
        @return:
        """
        item = self.find_element((By.XPATH, TopHotEvent.HOTEVENT.value))
        if not item:
            self.log_info("首页顶部热门事件tab不存在")
            return True
        self.element_click(element=item, element_name="热门事件")
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击热门事件打开{MainUrl.STORE.value}"):
            self.log_error(f"官网首页顶部栏点击热门事件跳转验证Failture")
        self.wait_page_loaded(message=f"等待{MainUrl.STORE.value}加载", time_wait=1)
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        return True

    def click_hottopic(self, original_window=None):
        """
        点击首页顶部任一热门话题
        @param original_window: 初始窗口句柄ID
        @return:
        """
        if self.find_element((By.XPATH, HotTopic.NOMORE.value)):
            more_button = self.find_element((By.XPATH, HotTopic.HASMORE.value))
            if more_button:
                self.element_click(element=more_button, element_name="首页热门话题更多按钮")
                self.sleep(2)

        item_list = self.find_element((By.XPATH, HotTopic.HOTTOPICLIST.value), multiple=True)
        item = random.choice(item_list)
        item_title = self.get_text(element=item.find_element(By.XPATH, './/div[@class="_ht_t1_ont9d_379"]'))
        self.element_click(item, element_name=f"首页热门话题: {item_title}")
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"首页点击热门话题{item_title}", wait_time=2):
            self.log_error(f"首页点击热门话题{item_title}Failure")
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        return True

    def click_slider(self, original_window):
        item_list = self.find_element((By.XPATH, TopSwiper.TOPWSWIPERLIST.value), multiple=True)
        try_time = len(item_list) * 2
        item_active_list = self.find_element((By.XPATH, TopSwiper.TOPWSWIPERACTIVELIST.value), multiple=True)
        item_active = random.choice(item_active_list)
        self.click_element_if_clickable(item_active, retries=try_time, wait_time=0.8)
        # self.click_element_if_clickable(item.find_element(
        #     By.XPATH, './div[@class="swiper-slide swiper-slide-duplicate swiper-slide-duplicate-active _slider_img_w_157cm_8"]'), retries=20, wait_time=wait_time)
        if not self.wait_util(EC.number_of_windows_to_be(2), message="随机点击轮播图"):
            self.log_error(f"首页点击任一轮播图Failure")
        self.wait_page_loaded(message="等待点击轮播图跳转页面加载", time_wait=2)
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        return True
























