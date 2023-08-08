from selenium.webdriver.chrome.options import Options

"""Selenium Webdriver相关功能函数"""


def get_chrome_options(proxy_server=None, binary_location=None, prefs=None):
    """
    获取 chrome webdriver 运行配置
    @param proxy_server: browsermob-proxy 服务地址
    @param binary_location: 浏览器所在路径（适用于Chrome内核浏览器）
    @return:
    """
    options = Options()

    if proxy_server:
        options.add_argument(f'--proxy-server={proxy_server}')

    if binary_location:
        options.binary_location = binary_location

    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-gpu')
    options.add_argument('--start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-site-isolation-trials')
    options.add_argument("service_args=['--ignore-ssl-errors=true','--ssl-protocol=TLSv1']")
    if prefs:
        options.add_experimental_option('prefs',prefs)
    return options