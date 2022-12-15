import requests
from bs4 import BeautifulSoup
import asyncio
from aiohttp import ClientSession

from proxy.get import GetProxy


class QQTV:
    def __init__(self):
        self.url = "https://v.qq.com/channel/net_tv"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }

    def sort_page(self):
        # proxy = GetProxy().get_vaild_ip()
        # if proxy is None:
        #     print("代理无效，请重新获取")
        #     return False
        # response = requests.get(url=self.url, headers=self.headers, proxies= {'http': proxy, 'https': proxy})
        response = requests.get(url=self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "lxml")
        images = soup.findAll('img', class_="figure_pic")
        for image in images:
            print(image.attrs['src'])

if __name__ == '__main__':
    QQTV().sort_page()