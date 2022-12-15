# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas
from itemadapter import ItemAdapter

# 开启setting pipline
class MyScrapyPipeline:
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        # with open('car.json', 'a', encoding='utf-8') as f:
        #     f.write(item)

        dataframe = pandas.DataFrame({"carName": item.get('carName'), "carLink": item.get("carLink"), "carImage": item.get("carImage"), "carPrice": item.get("carPrice"), "carScore": item.get("carScore")})
        dataframe.to_csv("catInfo.csv", mode='a', index=False, header=False, sep=',')
        return item

    def close_spider(self, spider):
        pass