import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}


def handle(image):
    img_stream = requests.get(image, headers=headers).content
    name = re.findall('http://ci.xiaohongshu.com/(.*?)\?', image)[0]
    path = './images/' + name + '.jpg'
    with open(path, 'wb') as f:
        f.write(img_stream)
