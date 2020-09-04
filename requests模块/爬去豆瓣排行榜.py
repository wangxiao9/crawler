__author__ = 'wangxiao'

import requests
import os
"""
1.指定url
2.发起请求
3.获取响应数据
4.持久化数据
"""


class CrawlerMovie:
    def __init__(self):
        self.url = "https://movie.douban.com/j/chart/top_list"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
        }

    def get_douban(self):
        param = {
            "type": "17",
            "interval_id": "100:90",
            "action": "",
            "start": "0",
            "limit": "20"
        }
        res = requests.get(url=self.url, json=param, headers=self.headers)
        return res.json()

    def run(self):
        res = self.get_douban()
        if not os.path.exists('./data'):
            os.mkdir('./data')
        for i in res:
            rank = i["rank"]
            cover_url = i["cover_url"]
            title = i["title"]
            url = i["url"]
            score = i["score"]
            movie = str(rank) + "*" + cover_url + "*" + title + "*" + url + "*" + score
            with open('./data/movie.txt', 'a') as f:
                f.write(movie + '\n')
                f.write("---------------------------------------------------------\n" )
        print("爬取电影信息成功！！！")

if __name__ == '__main__':
    CrawlerMovie().run()
    # for i in data:
    #     print(i['rank'])