__author__ = 'wangxiao'

import requests
"""
1.指定url
2.发起请求
3.获取响应数据
4.持久化数据
"""

class CrawlerBoss:
    def __init__(self):
        self.url = "https://www.zhipin.com/c101190400-p100305/?page=1&ka=page-1"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
        }
    def get_web_content(self):
        res = requests.get(url=self.url, headers=self.headers)
        print(res.text)


if __name__ == '__main__':
    CrawlerBoss().get_web_content()