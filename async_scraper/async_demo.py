import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup

from proxy.get import GetProxy

'''

https://myapollo.com.tw/zh-tw/begin-to-asyncio/
https://www.learncodewithmike.com/2020/09/python-asynchronous-scraper-using-asyncio-and-aiohttp.html
https://ithelp.ithome.com.tw/articles/10262385

'''

async def main():
    links = [
        'https://v.qq.com/channel/usuk',
        'https://v.qq.com/channel/net_tv',
    ]

    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch(link, session)) for link in links]
        await asyncio.gather(*tasks)


async def fetch(link, session):
    async with session.get(url=link) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "lxml")
        images = soup.findAll('img', class_="figure_pic")
        for image in images:
            print(image.attrs['src'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())