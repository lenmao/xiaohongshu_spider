import json
from spider.common.util import get


def grab(uid, limit):
    """
    获取小红书作者的所有笔记中图片链接地址
    :param uid: 小红书用户id
    :param limit 爬取页数限制
    :return: 图片地址列表
    """
    list_template_url = '/fe_api/burdock/weixin/v2/user/' + uid + '/notes?'
    info_template_url = '/fe_api/burdock/weixin/v2/note/nid/single_feed'
    count = 0
    page = 1
    res_list = []
    while True:
        sign_item = list_template_url + 'page=' + str(page) + '&page_size=15'
        response = get(sign_item)
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
            response = get(temp_url)
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


def userinfo(uid):
    info_template_url = '/fe_api/burdock/weixin/v2/user/' + uid
    response = get(info_template_url)
    json_str = response.text
    res_data = json.loads(json_str)
    return res_data['data']['nickname']
