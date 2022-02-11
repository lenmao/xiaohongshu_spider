import os
from multiprocessing.dummy import Pool
from spider.collect.collector import grab, userinfo
from spider.download.downloader import handle
import argparse
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--uid', help='the user id of xiaohongshu', required=True)
    parser.add_argument('-l', '--limit', help='page limit', default=0)
    args = parser.parse_args()
    uid = args.uid
    username = userinfo(uid)
    img_list = grab(uid, int(args.limit))
    pool = Pool(5)
    if not os.path.exists('./images'):
        os.mkdir('./images')
    print('开始下载')
    pool.map(handle, img_list)
    print('下载完毕')
