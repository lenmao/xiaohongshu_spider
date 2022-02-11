import requests
import hashlib
import json

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


def grab(uid, limit):
    """
    获取小红书作者的所有笔记中图片链接地址
    :param uid: 小红书用户id
    :param limit 爬取页数限制
    :return: 图片地址列表
    """
    list_domain = 'https://www.xiaohongshu.com'
    list_template_url = '/fe_api/burdock/weixin/v2/user/' + uid + '/notes?'
    info_domain = 'https://www.xiaohongshu.com'
    info_template_url = '/fe_api/burdock/weixin/v2/note/nid/single_feed'
    count = 0
    page = 1
    res_list = []
    while True:
        sign_item = list_template_url + 'page=' + str(page) + '&page_size=15'
        x_sign = generate_x_sign(sign_item)
        request_url = list_domain + sign_item
        headers['X-sign'] = x_sign
        response = requests.get(request_url, headers=headers)
        json_str = response.text
        res_data = json.loads(json_str)
        data_list = res_data['data']
        if not data_list or len(data_list) == 0:
            break
        total_size = len(data_list)
        print(f'第{page}页，共有{total_size}条笔记')
        for info in data_list:
            nid = info['id']
            temp_url = info_template_url.replace('nid', nid)
            info_x_sign = generate_x_sign(temp_url)
            headers['X-sign'] = info_x_sign
            response = requests.get(info_domain + temp_url, headers=headers)
            json_str = response.text
            res_data = json.loads(json_str)
            try:
                img_list = res_data['data']['imageList']
            except Exception:
                continue
            # print(f'{nid}笔记共有' + str(len(img_list)) + '张图片')
            for img in img_list:
                count = count + 1
                res_list.append(img['url'])
        page = page + 1
        if limit != 0 and page > limit:
            break

    print(f'共有{count}张图片')
    return res_list


def generate_x_sign(url):
    """
    小红书接口请求签名参数构造
    :param url:
    :return:
    """
    md5 = hashlib.md5()
    md5.update(bytes(url + 'WSUDD', encoding='utf-8'))
    return 'X' + md5.hexdigest()
