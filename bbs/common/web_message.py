from bbs.common.log import log
"""
针对浏览器页面的cookies和local storage进行获取和更改
"""

def get_cookies(driver):
    """
    获取当前页面cookies方法
    @param driver: driver对象
    @return cookies_dict
    """
    cookies_dict = {}
    cookies = driver.get_cookies() # list
    for cookie in cookies:
        cookies_dict[cookie['name']] = cookie['value']
    return cookies_dict

def get_localStorage(driver):
    """
    获取当前页面localStorage方法
    @param driver: driver对象
    @return localStorage_dict
    """
    localStorage_dict = driver.execute_script('return window.localStorage') # dict

    return localStorage_dict


def get_cookie_value(driver,key):
    """
    @param driver: driver对象
    @param key: cookie_key
    @return value: cookie_value
    """
    cookies_dict = get_cookies(driver)
    if key in cookies_dict.keys():
        cookie_value = cookies_dict[key]
    else:
        log.log_error(f"该cookie—key{key}不存在")
    return cookie_value

def set_cookie_value(driver,key,value):
    """
    @param driver: driver对象
    @param key: cookie_key
    @param value: cookie_value
    """
    cookies_dict = get_cookies(driver)
    driver.add_cookie({"name":key,"value":value})

def get_localStorage_value(driver,key):
    """
    @param driver: driver对象
    @param key: localStorage_key
    @return localStorage_value
    """
    localStorage_dict = get_localStorage(driver)
    if key in localStorage_dict.keys():
        localStorage_value = localStorage_dict[key]
    else:
        log.log_error(f"该localStorage{key}不存在")
    return localStorage_value

def set_localStorage_value(driver,key,value):
    """
    @param driver: driver对象
    @param key: localStorage_key
    @param value: localStorage_value
    """
    localStorage_dict = get_localStorage(driver)

    driver.execute_script(f'localStorage.setItem("{key}","{value}")')
