import importlib
import os
from urllib.parse import urlsplit

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from bbs.common.log import log


"""Selenium Web页面基类"""
def page_method_record(info):
    def wrapper(func):
        def dec(self, *args, **kwargs):
            if self.open_result:
                log.log_info(str(info))
                result = func(self, *args, **kwargs)
                return result
            log.log_error("failed" + str(info))
        return dec
    return wrapper

class WebPage(object):
    PageUrl = None # 页面url
    PageName = None # 页面描述名称

    def __init__(self, driver, do_pre_open=True, pageurl=None, pagename=None):
        """
        :param driver: WebDriver实例
        :param do_pre_open: 是否执行与打开操作
        :param pageurl: 页面url
        :param pagename: 页面描述名称
        """
        if pageurl:
            self.PageUrl = pageurl
        if pagename:
            self.PageName = pagename
        self.driver = driver
        self.driver_wait_dict = {}
        # 子类类名
        self.page_name = self.__class__.__name__
        # 子类文件路径
        self.filepath = importlib.import_module(self.__module__).__file__
        self.file_dir, self.filename_with_ext = os.path.split(self.filepath)
        # 子类文件名于扩展名
        self.filename, self.file_ext = os.path.splitext(self.filename_with_ext)

        # 设置全局隐式等待时间
        self.implicitly_wait(5)

        # 是否执行预打开操作
        if do_pre_open:
            self.open()

        self.wait_page_loaded()  #等待页面加载完成

        if self.PageUrl: #是否校验页面url
            current_url = urlsplit(self.get_current_url())._replace(query='').geturl() # 去除url中的query部分
            assert current_url == self.PageUrl, self.log_error(f"{self.PageName}Url校验失败，实际Url为{current_url}")

        self.log_info(f"{self.PageName}打开成功", screenshot=True)

    def get_current_url(self):
        """获取当前页面Url"""
        return self.driver.current_url

    def open_url(self, url, screenshot=False):
        """
        打开网页
        :param url: 网页url
        :param screenshot: 是否截图记录
        :return:
        """
        self.driver.set_page_load_timeout(30)
        self.open_result = False

        if screenshot:
            driver = self.driver
        else:
            driver = None

        try:
            self.driver.get(url)
            log.log_info(f"打开网页：{url}", driver=driver)
        except TimeoutException:
            log.log_error(f"打开网页：{url}超时，请检查网络或网址服务器", driver=self.driver)
        self.open_result = True

    def open(self):
        """打开页面"""
        self.open_url(self.PageUrl)

    def pre_open(self):
        """与打开页面"""
        self.open()

    def implicitly_wait(self, seconds=0):
        """
        设置隐式等待时长
        :param seconds: 隐式等待时长
        :return:
        """
        self.driver.implicitly_wait(seconds)

    def get_driver_wait(self, timeout=10):
        """
        获取WebDriverWait实例
        :param timeout: 等待超时时间（秒）
        :return:
        """
        _wait = self.driver_wait_dict.get(timeout, None)
        if not _wait:
            _wait = WebDriverWait(self.driver, timeout)
            self.driver_wait_dict[timeout] = _wait
        return _wait

    def wait_util(self, method, timeout=10, message=''):
        """
        根据提供的方法等待直至元素或超时
        :param method:元素查找方法
        :param timeout: 等待超时时间（秒）
        :param message:描述信息
        :return:
        """
        _wait = self.get_driver_wait(timeout)

        try:
            result = _wait.until(method, message)
            if message:
                log.log_info(f"等待{message}完成")
            return result
        except TimeoutException as e:
            assert not e, self.log_error(f"等待{message}超时")
        except Exception as e:
            assert not e, self.log_error(f"等待{message}出错，err:{e}")

    def wait_page_loaded(self, timeout=10, message=''):
        """
        等待页面加载完成
        :param timeout:等待超时时间（秒）
        :param message: 描述信息
        :return:
        """
        return self.wait_util(lambda driver : driver.execute_script('return document.readyState;') == "complete",
                              timeout, message)


    def log_info(self, msg, log_only=False, screenshot=False, attach=True, compress_rate=0.7, shot_delay=0):
        """
        输出Info级别日志
        :param msg: 日志信息
        :param log_only: 是否仅打印日志
        :param screenshot:是否添加截图附件
        :param attach:是否添加到allure报告附件
        :param compress_rate: 截图附件压缩比率
        :param shot_delay: 截图延迟秒数
        :return:
        """
        if screenshot:
            driver = self.driver
        else:
            driver = None
        log.log_info(msg, log_only=log_only, attach=attach, driver=driver, compress_rate=compress_rate, shot_delay=shot_delay)

    def log_error(self, msg, log_only=False, attach=True, need_assert=False):
        """
        输出Error级别日志
        @param msg: 日志信息
        @param log_only: 是否仅打印日志
        @param attach: 是否添加到allure报告附件
        @param need_assert: 是否需要断言
        @return:
        """
        log.log_error(msg, log_only=log_only, attach=attach, need_assert=need_assert, driver=self.driver)

    def log_pass(self, msg, screenshot=True, compress_rate=0.7):
        """
        输出Pass级别日志
        @param msg: 日志信息
        @param screenshot: 是否添加截图附件
        @param compress_rate: 截图附件压缩比率
        @return:
        """
        if screenshot:
            attach = True
            driver = self.driver
        else:
            attach = False
            driver = None

        log.log_pass(msg, attach=attach, driver=driver, compress_rate=compress_rate)