from bbs.common.webpage import WebPage
import allure
import os
from selenium.webdriver.common.by import By
from bbs.utils import driver_wait_until
from selenium.webdriver.support import expected_conditions as EC
from bbs.contants import MainUrl, TopElement, ListType
from bbs.utils import back_to_original_window
from bbs.item_code import TopElementItem, TopHotEvent, HotTopic, TopSwiper, ModeSwitch, Circle, HotUser,ArticleList
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

    def click_slider(self, original_window=None):
        """
        首页点击任一轮播图
        @param original_window: 初始窗口句柄ID
        @return:
        """
        item_list = self.find_element((By.XPATH, TopSwiper.TOPWSWIPERLIST.value), multiple=True)
        try_time = len(item_list) * 2
        item_active_list = self.find_element((By.XPATH, TopSwiper.TOPWSWIPERACTIVELIST.value), multiple=True)
        item_active = random.choice(item_active_list)
        self.click_element_if_clickable(item_active, retries=try_time, wait_time=0.5)
        # self.click_element_if_clickable(item.find_element(
        #     By.XPATH, './div[@class="swiper-slide swiper-slide-duplicate swiper-slide-duplicate-active _slider_img_w_157cm_8"]'), retries=20, wait_time=wait_time)
        if not self.wait_util(EC.number_of_windows_to_be(2), message="随机点击轮播图"):
            self.log_error(f"首页点击任一轮播图Failure")
        self.wait_page_loaded(message="等待点击轮播图跳转页面加载", time_wait=2)
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        return True

    def mode_switch(self):
        """
        首页点击模式切换验证
        @return:
        """
        current_mode = "DARK"
        if not self.find_element((By.XPATH, ModeSwitch.DARKMODE.value)):
            current_mode = "NORMAL"
        self.log_info(f"当前页面展示模式为{current_mode}")
        if not current_mode == "NORMAL":
            self.element_click(element=self.find_element((By.XPATH, ModeSwitch.DARKMODE.value)),
                               element_name=f"原始模式为{current_mode}, 预期切换为 NORMAL")
            self.sleep(3)
            if not self.find_element((By.XPATH, ModeSwitch.NORMALMODE.value)):
                self.log_error(f"预期切换为 NORMAL Failure")
            return True
        self.element_click(element=self.find_element((By.XPATH, ModeSwitch.NORMALMODE.value)),
                           element_name=f"原始模式为{current_mode}, 预期切换为 DARK")
        self.sleep(3)
        if not self.find_element((By.XPATH, ModeSwitch.DARKMODE.value)):
            self.log_error(f"预期切换为 DARK Failure")
        return True

    def click_circle(self, original_window=None):
        """
        点击首页圈子打开圈子详情页
        @param original_window: 初始窗口句柄 ID
        @return:
        """
        self.page_scroll_to_view(self.find_element((By.XPATH, TopSwiper.TOPSWIPERVIEW.value)))
        # self.sleep(2)
        # self.scroll_page(200)
        self.sleep(1)
        if not self.find_element((By.XPATH, Circle.CIRCLESHOWMORE.value)):
            self.element_click(self.find_element((By.XPATH, Circle.CICLEMOREBUTTON.value)), element_name="更多圈子展开按钮")
        # self.wait_util(self.find_element((By.XPATH, Circle.CIRCLESHOWMORE.value)))
        self.wait_util(EC.presence_of_element_located((By.XPATH, Circle.CIRCLESHOWMORE.value)))
        circle_list = self.find_element((By.XPATH, Circle.CICLELIST.value), multiple=True)
        circle = random.choice(circle_list)
        circle_title = self.get_text(element=circle.find_element(By.XPATH, './/div[@class="_item_content1_v7l0m_2"]'))
        self.element_click(circle, element_name=f"首页圈子：{circle_title}")
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"首页点击圈子：{circle_title} 打开详情页"):
            self.log_error(f"首页点击圈子：{circle_title} 打开详情页 Failure")
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        return True

    def click_hotuser(self, original_window=None):
        self.page_scroll_to_view(self.find_element((By.XPATH, Circle.CIRCLEVIEW.value)))
        self.sleep(1)
        self.scroll_page(scroll_height=self.get_current_page_height() + 200)
        self.sleep(1)
        user_list = self.find_element((By.XPATH, HotUser.HOTUSER.value), multiple=True)
        # 展示数量兼容考虑，仅取中间五个中任意一个
        user_list = user_list[0:5]
        user = random.choice(user_list)
        user_name = self.get_text(element=user.find_element(By.XPATH, './/div[@class="_content1_1qi0v_31"]'))
        self.element_click(element=user, element_name=f"{user_name}")
        self.sleep(1)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击打开用户：{user_name}主页"):
            self.log_error(f"点击人气用户打开用户：{user_name}主页Failure")
        self.back_to_first_window(original_window, expect_url=MainUrl.BBS.value)
        self.sleep(1)
        return True

    def click_article(self, list_type=None):
        """
        点击文章打开文章详情页
        @param list_type: 列表类型
        @return:
        """
        self.page_scroll_to_view(self.find_element((By.XPATH, HotUser.HOTUSERVIEW.value)))
        self.sleep(1)
        if not list_type:
            current_type = self.get_current_listtype()
            self.change_current_listtype(expect_type=current_type)
            result = self.find_article_and_click(current_type)
            if not result[0]:
                self.log_error(f"点击{list_type} 列表中的文章：{result[1]}，打开文章详情页")
            # 剩下两个list_type
            notactive_type_list = self.find_element((By.XPATH, ArticleList.ARTICLELIST.value), multiple=True)
            # next_type = notactive_type_list[0]
            for next_type in notactive_type_list:
                next_type_title = self.get_text(element=next_type)
                result = self.find_article_and_click(next_type_title)
                if not result[0]:
                    self.log_error(f"点击{list_type} 列表中的文章：{result[1]}，打开文章详情页")
            return True

        elif list_type == ListType.RECOMMEND.value:
            self.change_current_listtype(expect_type=ListType.RECOMMEND.value)
        elif list_type == ListType.NOW.value:
            self.change_current_listtype(expect_type=ListType.NOW.value)
        elif list_type == ListType.HOT.value:
            self.change_current_listtype(expect_type=ListType.HOT.value)
        self.sleep(1)
        result = self.find_article_and_click(list_type)
        if not result[0]:
            self.log_error(f"点击{list_type} 列表中的文章：{result[1]}，打开文章详情页")
        return True


    def find_article_and_click(self, list_type=None):
        """
        寻找列表中的任意文章并点击
        @param list_type: 列表类型
        @return:
        """
        # find_aritle
        article_list = self.find_element((By.XPATH, ArticleList.ARTICLELIST.value), multiple=True)
        article = random.choice(article_list)
        article_title = self.get_text(element=article.find_element(By.XPATH, './/div[@class="_it_title_18jbr_10"]'))
        self.page_scroll_to_view(article)
        self.sleep(2)
        # page_scroll_to_view()方法会将指定文章高度置顶，导致后续操作可能会存在异常，故此处将其回滚些许高度
        self.scroll_page(self.get_current_page_height()-150)
        self.sleep(1)

        # click_article
        self.element_click(element=article, element_name=article_title)
        if not self.wait_util(EC.number_of_windows_to_be(2), message=f"点击{list_type} 列表中的文章：{article_title}，打开文章详情页"):
            return False, article_title
        return True, article_title


    def get_current_listtype(self):
        """
        获取当前列表类型
        @return:
        """
        item = self.find_element((By.XPATH, ArticleList.LISTTYPEACTIVE.value))
        return item.text

    def change_current_listtype(self, expect_type=None):
        """
        切换列表为指定类型列表
        @param expect_type: 预期切换的列表类型
        @return:
        """
        self.page_scroll_to_view(self.find_element((By.XPATH, HotUser.HOTUSERVIEW.value)))
        self.sleep(1)
        current_type =self.get_current_listtype()
        if current_type == expect_type:
            return
        if expect_type == "精选":
            self.element_click(element=self.find_element((By.XPATH, '//div[@class="_tab_item_19gkq_86 and text()="精选""]')),
                               element_name=ListType.RECOMMEND.value)
            self.sleep(2)
        elif expect_type == "此刻":
            self.element_click(
                element=self.find_element((By.XPATH, '//div[@class="_tab_item_19gkq_86 and text()="此刻""]')),
                element_name=ListType.NOW.value)
            self.sleep(2)
        elif expect_type == "热门":
            self.element_click(
                element=self.find_element((By.XPATH, '//div[@class="_tab_item_19gkq_86 and text()="热门""]')),
                element_name=ListType.HOT.value)
            self.sleep(2)




































