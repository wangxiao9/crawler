'''
task:
    获取云合平台的热播数据
'''
import json

import jsonpath, requests, pandas


class Yunhe:
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "cookie": "JSESSIONID = E5137DA1CB2E72770CDA11CB2E8DB16B;Hm_lvt_030f908df5513cb0a704c88c5da2bc37 = 1670305316;Hm_lpvt_030f908df5513cb0a704c88c5da2bc37 = 1670305480"
        }

        self.url = "https://www.enlightent.cn/sxapi/top/getHeatTop.do"
        self.params = {
            "sort": "allHot",
            "channelType": "tv",
            "day": 1
        }

    def __get_page_json(self):
        response = requests.post(url=self.url, headers=self.headers, data=self.params)
        with open("yunhe.json", 'w+', encoding="utf-8") as f:
            f.write(json.dumps(response.json(), ensure_ascii=False))
        f.close()


    def __sort_json(self):
        obj = json.load(open('yunhe.json', 'r', encoding="utf-8"))
        nameList = jsonpath.jsonpath(obj, '$..name')
        DayList = jsonpath.jsonpath(obj, '$..occurDays')
        channelList = jsonpath.jsonpath(obj, '$..channel')

        dataframe = pandas.DataFrame({"电视剧": nameList, "上映时间": DayList, "播放平台": channelList})
        dataframe.to_csv("yunhe.csv", index=False,mode='a', sep=',')

    def run(self):
        self.__sort_json()


if __name__ == '__main__':
    Yunhe().run()