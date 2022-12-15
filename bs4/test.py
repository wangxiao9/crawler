
import time

import requests

from bs4 import BeautifulSoup




def write(contents):
    with open('ww.txt', 'a+', encoding="utf-8") as f:
        f.write(contents)
    f.close()


def request():
    for i in range(9633292, 9633332):
        print(f"当前获取的第{i}页")
        page = str(i)
        res = requests.get(f"https://xxx.com/book/35559/{page}.html")
        soup = BeautifulSoup(res.text, "html.parser")
        contents = soup.find("div", class_="acontent")

        if contents is not None:
            write(contents.getText())
        time.sleep(5)


if __name__ == '__main__':
    request()
