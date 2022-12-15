from typing import List

import requests, pandas
from bs4 import BeautifulSoup

'''
其他网站：
http://www.66ip.cn/3.html
'''
class Proxys:
    def __init__(self, page):
        self.page = page
        self.free_proxy_web = "https://www.89ip.cn/"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }

    def __sort_proxy(self, proxy:List):
        ip = proxy[0].get_text().strip()
        port = proxy[1].get_text().strip()
        return ip + ':' + port

    def __get_proxy_list(self, num):
        self.url = self.free_proxy_web + f'index_{num}.html'
        print(f"正在请求:{self.url}")
        response = requests.get(url=self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "lxml")
        table = soup.find("table", class_="layui-table")
        proxy_list = table.findAll("tr")
        new_proxy_ip = []
        for i in range(1, len(proxy_list)):
            ip_port = self.__sort_proxy(proxy_list[i].findAll("td"))
            new_proxy_ip.append(ip_port)

        return new_proxy_ip

    def run(self):
        for i in range(1, self.page + 1):
            new_proxy_ip_list = self.__get_proxy_list(i)
            dataframe = pandas.DataFrame({"ip_address": new_proxy_ip_list})
            dataframe.to_csv("proxies.csv", mode='a', index=False,  header=False, sep=',')


if __name__ == '__main__':
    Proxys(10).run()