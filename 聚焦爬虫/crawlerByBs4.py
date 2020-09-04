__author__ = 'wangxiao'

import time

import bs4
import requests
from random import choice

class CrawlerNovel:
    def __init__(self):
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        ]
        self.url = "http://www.quanshuwang.com/book/0/858"
        self.headers = {
            "user-agent": choice(self.user_agent_list)
        }

    def get_response(self):
        res = requests.get(url=self.url, headers=self.headers).content
        return res

    def run(self):
        res = self.get_response()
        # 1. 实例化bs4
        soup = bs4.BeautifulSoup(res, 'lxml')
        targets = soup.select(".clearfix > li")
        for target in targets:
            title = target.a.string
            chapter_url = target.a['href']
            time.sleep(5)
            every_chapter = requests.get(url=chapter_url, headers=self.headers).text
            soup_chapter = bs4.BeautifulSoup(every_chapter, 'lxml')
            tag_chapter = soup_chapter.find("div", class_="mainContenr")
            content = tag_chapter.text
            print(content)
    def test(self):
        url = "http://www.quanshuwang.com/book/0/858/274178.html"
        res = requests.get(url, headers=self.headers).text
        print(res)





if __name__ == '__main__':
    CrawlerNovel().test()