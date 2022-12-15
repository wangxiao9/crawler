# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas
import requests


class CarhomePipeline:
    def open_spider(self, spider):
        self.nameList = []
        self.linkList = []
        self.imageList = []
        self.priceList = []
        self.scoreList = []

    def process_item(self, item, spider):
        self.nameList.append(item.get('carName'))
        self.linkList.append(item.get('carLink'))
        self.imageList.append(item.get('carImage'))
        self.priceList.append(item.get('carPrice'))
        self.scoreList.append(item.get('carScore'))

        return item

    def close_spider(self, spider):
        dataframe = pandas.DataFrame(
            {"carName": self.nameList, "carLink": self.linkList, "carImage": self.imageList,
             "carPrice": self.priceList, "carScore": self.scoreList})
        dataframe.to_csv("carInfo.csv", mode='a', index=False, header=False, sep=',')


# 多管道下载

class CarImagesDownloadPipeline:

    def process_item(self, item, spider):
        res = requests.get(item.get('carImage'))
        file_name = item.get('carImage').split('/')[-1]
        with open(f'.//carImage//{file_name}', 'wb') as f:
            f.write(res.content)
        f.close()
        return item
