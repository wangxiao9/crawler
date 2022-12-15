from bs4 import BeautifulSoup
import requests



class Starbucks:
    def __init__(self):
        self.url = 'https://www.starbucks.com.cn/menu/'
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "cookie": "JSESSIONID = E5137DA1CB2E72770CDA11CB2E8DB16B;Hm_lvt_030f908df5513cb0a704c88c5da2bc37 = 1670305316;Hm_lpvt_030f908df5513cb0a704c88c5da2bc37 = 1670305480"
        }

    def get_page(self):
        response = requests.get(url=self.url, headers= self.headers)
        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.select('ul[class="grid padded-3 product"] strong')
        for product in products:
            print(product.get_text())

if __name__ == '__main__':
    Starbucks().get_page()