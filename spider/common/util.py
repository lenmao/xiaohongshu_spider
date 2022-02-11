import requests
import hashlib

domain = 'https://www.xiaohongshu.com'

headers = {'Host': 'www.xiaohongshu.com',
           'Content-Type': 'application/json',
           'Accept': '*/*',
           'Accept-Language': 'zh-cn',
           'Accept-Encoding': 'gzip, deflate, br',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E217 MicroMessenger/6.8.0(0x16080000) NetType/WIFI Language/en Branch/Br_trunk MiniProgramEnv/Mac',
           'Device-Fingerprint': 'WHJMrwNw1k/GZuv20MGK+CdCmLIgo/SMs6ybzkLsvQaIyVddwkw/fztmjIogXXXpFPcFUAo6ZrwmtS/m+LanYqLHYkVJbK6XndCW1tldyDzmauSxIJm5Txg==1487582755342',
           'Authorization': 'wxmp.f6991546-00d2-40ab-b1a2-e459ba6510b4',
           'Referer': 'https://servicewechat.com/wxb296433268a1c654/60/page-frame.html'}


def get(sign_item):
    x_sign = generate_x_sign(sign_item)
    request_url = domain + sign_item
    headers['X-sign'] = x_sign
    return requests.get(request_url, headers=headers)


def generate_x_sign(url):
    """
    小红书接口请求签名参数构造
    :param url:
    :return:
    """
    md5 = hashlib.md5()
    md5.update(bytes(url + 'WSUDD', encoding='utf-8'))
    return 'X' + md5.hexdigest()
