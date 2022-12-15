import scrapy

from CarHome.items import CarhomeItem


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/diandongche/list-0-0-0-1-0-0-0-0-1.html']



    def parse(self, response):
        current_page = 2
        carList = response.xpath('//div[@class="list-cont-bg"]')
        for car in carList:
            carImage = "https:" + car.xpath('.//img/@src').extract_first()
            carName = car.xpath('.//a[@class="font-bold"]/text()').extract_first()
            scoreNumber = car.xpath('.//span[@class="score-number"]/text()').extract_first()
            carPrice = car.xpath('.//span[@class="font-arial"]/text()').extract_first()
            carLink = "https://car.autohome.com.cn" + car.xpath('.//a[@class="font-bold"]/@href').extract_first()

            carItems = CarhomeItem(carName=carName, carLink=carLink, carImage=carImage, carPrice=carPrice,
                               carScore=scoreNumber)
            # -> pipline download
            yield carItems


        while(current_page < 11):
            url = f'https://car.autohome.com.cn/diandongche/list-0-0-0-1-0-0-0-0-{current_page}.html'
            current_page +=1
            yield scrapy.Request(url=url, callback=self.parse)


