# xiaohongshu_spider
批量下载小红书作者笔记中的图片

## 使用说明
```txt
进入项目目录下
启动：`python3 -m spider -u uid [-l args]`
必选参数-u(uid)：为要爬取的小红书作者的用户id
可选参数-l(limit)：指定要爬取的最大页数，小红书api返回的一页数据为6条
例如： `python3 -m spider -u jasdjf1234lkh -l 10` 为爬取uid为jasdjf1234lkh的用户的前10页笔记中的图片
```