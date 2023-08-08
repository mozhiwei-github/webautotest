import importlib
import socket
from bbs.common.contants import logs_file
from bbs.common.log import log
import requests
import os
import allure




screen_temp_pic_name = os.path.join(logs_file, "origin_pic.png")

def try_import(module_name, element_name=None):
    """
    尝试引入模块（模块不存在时返回None）
    @param module_name: 模块名
    @param element_name: 模块内元素名称
    @return:
    """
    try:
        module_spec = importlib.util.find_spec(module_name)
    except Exception as e:
        return None
    if not module_spec:
        return module_spec

    module = importlib.import_module(module_name)

    if element_name:
        result = getattr(module, element_name)
    else:
        result = module

    return result


cv2 = try_import('cv2')
Image = try_import('PIL.Image')


def get_domain_ip(domain):
    """
    获取域名的指向ip
    :param domain: 域名
    :return:
    """
    result = None
    try:
        address = socket.getaddrinfo(domain, "http")
        result = address[0][4][0]
    except Exception as e:
        log.log_error("域名解析失败", attach=False)
    return result

# 发送http请求
def send_request(url, params=None, data=None, json=None, files=None, headers=None, timeout=10,
                 method='post', proxy=None, num_retries=1, _is_retry=False, verify=True):
    """
    :param dict url: 请求地址
    :param dict params: 请求查询参数
    :param dict data: 提交表单数据
    :param dict json: 提交json字符串数据
    :param dict files: 提交文件数据
    :param dict headers: 请求头
    :param int timeout: 超时时间，单位秒
    :param str method: 请求方法，get、post、put、delete
    :param str proxy: 设置代理服务器
    :param int num_retries: 超时重试次数
    :param bool _is_retry: 判定为重试请求，这不应该由用户发出
    :param bool verify: 是否验证证书
    :return: 
    """
    headers = headers or {}
    method = method.lower()
    if method == 'get':
        method_func = requests.get
    elif method == 'post':
        method_func = requests.post
    elif method == 'put':
        method_func = requests.put
    elif method == 'delete':
        method_func = requests.delete
    else:
        method_func = requests.post  # 默认使用post
    try:
        resp = method_func(url, params=params, headers=headers, data=data, json=json, files=files, timeout=timeout,
             proxies=proxy if _is_retry is True and proxy else None, verify=verify)
    except(requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        if num_retries > 0:
            return send_request(
                url,
                params=params,
                headers=headers,
                data=data,
                json=json,
                files=files,
                timeout=timeout,
                method=method,
                proxy=proxy,
                num_retries=num_retries - 1,
                _is_retry=True,
                verify=verify
            )
        else:
            raise
    except(requests.exceptions.RequestException, Exception):
        raise
    else:
        return resp


def attach_driver_screenshot(driver, name, compress_rate=0.7, image_path=screen_temp_pic_name):
    """
    添加浏览器截图至allure报告中
    @param driver: selenium浏览器驱动
    @param name: allure附件标题
    @param compress_rate: 压缩比率
    @param image_path: 截图存储路径
    @return:
    """
    driver.get_screenshot_as_file(image_path)

    # 压缩图片
    compress_png = compress_pic(pic_path=image_path, compress_rate=compress_rate)

    # 添加到allure报告中
    allure.attach.file(compress_png, name=name, attachment_type=allure.attachment_type.PNG)

def compress_pic(compress_rate=1.0, pic_path=screen_temp_pic_name):
    """
    压缩图片
    @param compress_rate: 压缩比率（影响清晰度）
    @param pic_path: 图片路径
    @return:
    """
    path, name = os.path.split(pic_path)
    filename, extension = os.path.splitext(name)
    new_name = f"{filename}_compress_{compress_rate}{extension}"
    new_path = os.path.join(path, new_name)

    if cv2:  # 安装了 opencv 时优先使用 cv2 压缩
        pic = cv2.imread(pic_path)
        height, width = pic.shape[:2]
        pic_resize = cv2.resize(pic, (int(width * compress_rate), int(height * compress_rate)),
                                interpolation=cv2.INTER_AREA)
        cv2.imwrite(new_path, pic_resize)
    else:  # 使用 Pillow 压缩
        img = Image.open(pic_path)
        if img.format == 'PNG':
            img = img.convert('RGB')

        img.save(new_path, quality=int(compress_rate * 100), optimize=True)

    return new_path
