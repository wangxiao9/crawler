import scrapy

from my_scrapy.items import CarItem


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/diandongche/list-0-0-0-1-0-0-0-0-1.html']

    def parse(self, response):

        carList = response.xpath('//div[@class="list-cont-bg"]//img/@src')
        for car in carList:

            carImage = car.xpath('.//img/@src').extract_first()
            carName = car.xpath('.//a[@class="font-bold"]/text()').extract_first()
            scoreNumber = car.xpath('.//span[@class="score-number"]/text()').extract_first()
            carPrice = car.xpath('.//span[@class="font-arial"]/text()').extract_first()
            carLink = car.xpath('.//a[@class="font-bold"]/@href').extract_first()

            carItems = CarItem(carName=carName, carLink=carLink, carImage=carImage, carPrice=carPrice, carScore=scoreNumber)
            # -> pipline download
            yield carItems