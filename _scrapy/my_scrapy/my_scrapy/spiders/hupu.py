import scrapy


class HupuSpider(scrapy.Spider):
    name = 'hupu'
    allowed_domains = ['hupu.com']
    start_urls = ['http://hupu.com/']

    def parse(self, response):
        print(response.body.decode("utf-8"))
