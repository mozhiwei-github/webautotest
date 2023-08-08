import psutil
from bbs.common.log import log
from browsermobproxy import Server, Client

"""BrowserMob Proxy （Selenium 代理）相关功能函数"""


def start_browsermob_proxy(server_path, host="localhost", port=8080):
    """启动本地 browermob-proxy 服务"""
    server = Server(server_path, {"host": host, "port": port})
    server.start()
    proxy = server.create_proxy()
    return proxy, server


def terminate_browsermob_processes():
    """杀死本地 browermob-proxy 服务进程"""
    # Find BrowserMob-Proxy processes that may still be alive and kill them
    for process in psutil.process_iter():
        try:
            process_info = process.as_dict(attrs=['name', 'cmdline'])
            if process_info.get('name') in ('java', 'java.exe'):
                for cmd_info in process_info.get('cmdline'):
                    if cmd_info == '-Dapp.name=browsermob-proxy':
                        process.kill()
        except psutil.NoSuchProcess:
            pass


def get_browsermob_proxy_client(server_address):
    """初始化一个 browermob-proxy Client"""
    return Client(server_address)


DefaultProxyHarOptions = {
    "captureHeaders": True,
    "captureContent": True
}


class ProxyClient(object):
    def __init__(self, proxy):
        self.proxy = proxy

    def new_har(self, ref=None, options=DefaultProxyHarOptions, title=None):
        """
        设置要记录的新Har
        @param ref: har引用名称
        @param options: 代理选项
        @param title: 第一个Har页面的标题，默认为ref参数的值
        @return:
        """
        return self.proxy.new_har(ref, options, title)

    def get_har(self):
        return self.proxy.har

    def get_har_entries(self, request_url_keywords=None):
        """
        获取Har的日志条目
        @param request_url_keywords: 请求Url的关键词
        @return:
        """
        entries = []
        try:
            har_resp = self.get_har()
            log_entries = har_resp["log"]["entries"]
            for entry in log_entries:
                # 根据请求Url前缀过滤条目
                if request_url_keywords and request_url_keywords not in entry["request"]["url"]:
                    continue

                entries.append(entry)
        except Exception as e:
            log.log_info(f"get_har_entries error: {e}", log_only=True)

        return entries
