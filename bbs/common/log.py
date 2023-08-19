import datetime
import logging
import os
import time
from pprint import pformat
import allure
from bbs.common.contants import ServerHost, EnvVar, logs_file
import json


"""日志处理函数"""

class Log(object):
    def __init__(self, casename="undefind", log_level=logging.INFO):
        self.caseid = os.environ.get(EnvVar.CASE_ID.value)
        # id = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + "." + str(round(time.time() * 1000))[-3:0]
        id = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        if not self.caseid:
            self.caseid = "cid_" + id
        self.casename = os.environ.get(EnvVar.CASE_NAME.value)
        if not self.casename:
            self.casename = casename
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)

        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        # 日志文件处理器
        self.log_file = os.path.join(logs_file, f"{self.caseid}.txt")
        self.file_handler = logging.FileHandler(self.log_file, mode="a+", encoding="UTF-8")
        self.file_handler.setLevel(log_level)
        self.file_handler.setFormatter(self.formatter)

        # 日志终端处理器
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(log_level)
        self.stream_handler.setFormatter(self.formatter)

        # 将日志处理器添加到logger中
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)

    def log_debug(self, msg):
        self.logger.debug(msg)

    def log_info(self, msg, title=None, attach=True, log_only=False, driver=None, screenshot=False,
                 compress_rate=0.7,
                 shot_delay=0):
        """
        Info级别日志输出
        @param msg: 日志信息
        @param title: allure附件信息的title
        @param attach: 是否添加到allure报告附件
        @param log_only: 是否仅打印日志
        @param driver: selenium浏览器驱动，传入时使用driver的截图作为附件
        @param screenshot: 是否添加截图附件
        @param compress_rate: 截图附件压缩比率
        @param shot_delay: 截图延迟秒数
        @return:
        """
        if title:
            msg = pformat(msg)
            allure.attach(msg, title)
            msg = f"{title}: {msg}"
        else:
            msg = str(msg)
            if attach:
                if driver:
                    from bbs.common.utils import attach_driver_screenshot
                    time.sleep(shot_delay)
                    attach_driver_screenshot(driver, msg, compress_rate=compress_rate)
                elif screenshot:
                    from bbs.common.utils import attach_screenshot
                    time.sleep(shot_delay)
                    attach_screenshot(msg, compress_rate=compress_rate)
                else:
                    allure.attach(msg, msg)
        self.logger.info(msg)
        if log_only:
            return

        header = str(time.strftime('%H:%M:%S', time.localtime(time.time()))) + " INFO:"
        self._marklog(header + msg)

    def log_pass(self, msg, attach=True, driver=None, compress_rate=0.7):
        msg = str(msg)
        self.logger.info(msg)
        header = str(time.strftime('%H:%M:%S', time.localtime(time.time()))) + " PASS:"
        self._marklog(header + msg)

        if attach:
            if driver:
                from bbs.common.utils import attach_driver_screenshot
                attach_driver_screenshot(driver, msg, compress_rate=compress_rate)
            else:
                from bbs.common.utils import attach_screenshot
                attach_screenshot(msg, compress_rate=compress_rate)

    def log_error(self, msg, log_only=False, attach=True, need_assert=True, driver=None):
        """
        Error级别日志输出
        @param msg: 日志信息
        @param log_only: 是否仅打印日志
        @param attach: 是否截图并添加到allure报告附件
        @param need_assert: 是否需要断言
        @param driver: selenium浏览器驱动，传入时采用driver的截图方法
        @return:
        """
        msg = str(msg)
        self.logger.error(msg)
        if log_only:
            return msg

        header = str(time.strftime('%H:%M:%S', time.localtime(time.time()))) + " ERROR:"
        self._marklog(header + msg)
        # 出现error时截图并添加到allure报告中
        if attach:
            if driver:
                from bbs.common.utils import attach_driver_screenshot
                attach_driver_screenshot(driver, msg, compress_rate=1.0)
            else:
                from bbs.common.utils import attach_screenshot
                attach_screenshot(msg, compress_rate=1.0)

        if need_assert:
            assert False, msg

        return msg

    def log_finish(self):
        msg = "测试结束"
        self.logger.error(msg)
        header = str(time.strftime('%H:%M:%S', time.localtime(time.time()))) + " FINISH:"
        self._marklog(header + msg)

    def _marklog(self, msg):
        if self.caseid.find("cid") < 0:
            self.report(msg)

    def report(self, msg):
        from bbs.common.utils import send_request
        data = {"caseid": self.caseid, "casename": self.casename, "mark": msg}
        response = send_request(f"{ServerHost.AUTO_TEST_CF.value}/interface/pctestreportmark", json=data,
                                timeout=60 * 3)
        try:
            res_json = json.loads(response.content)
            return res_json
        except Exception as e:
            self.logger.error(f"log report response decode error, content: {response.content}")
            return None

# 从环境变量中读取日志等级
log_level = int(os.environ.get(EnvVar.UITEST_LOG_LEVEL.value, logging.INFO))
log = Log(log_level=log_level)




