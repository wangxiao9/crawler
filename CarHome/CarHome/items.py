# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarhomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    carName = scrapy.Field()
    carLink = scrapy.Field()
    carImage = scrapy.Field()
    carPrice = scrapy.Field()
    carScore = scrapy.Field()
