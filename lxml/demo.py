from typing import List

from lxml import etree
import requests, pandas

'''
task
1. 获取贝壳网站的房屋信息
    - 新房楼盘  ， 地址 ， 房价
    - 获取前十页
'''





class BeiKe():
    def __init__(self, num):
        self.page = num
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        }


    def __sorting_location(self, locations: List):
        new_locations = []

        for i in range(0,  len(locations)):
            if i == len(locations):
                break
            if locations[i] == '\n\t\t\t':
                locations.pop(i)
        for location in locations:
            new_locations.append(location.replace('\n\t\t', ''))
        return new_locations



    def __get_page(self, url):
        response = requests.get(url=url, headers=self.headers).text
        tree = etree.HTML(response)
        nameList = tree.xpath('//div[@class="resblock-name"]//a/text()')
        LocationList = self.__sorting_location(tree.xpath('//div[@class="resblock-desc-wrapper"]//a[@class="resblock-location"]/text()'))
        priceList =  tree.xpath('//div[@class="resblock-price"]//span[@class="number"]/text()')
        return nameList, LocationList, priceList

    def run(self):
        for i in range(1, self.page+1):
            (nameList, LocationList, priceList) = self.__get_page(f"https://su.fang.ke.com/loupan/pg{i}/")
            dataframe = pandas.DataFrame({"楼盘": nameList, "地址": LocationList, "价格": priceList})
            dataframe.to_csv("beike_su.csv", index=False, mode='a', header=False, sep=',')
        # print(nameList)
        # print(LocationList)
        # print(priceList)


if __name__ == '__main__':
    BeiKe(10).run()