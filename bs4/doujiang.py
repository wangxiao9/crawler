
import time

import requests

from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

def write(contents):
    with open('mitang2.txt', 'a+', encoding="utf-8") as f:
        f.write(contents)
    f.close()


def request():
    for i in range(0, 161):
        print(f"当前获取的第{i}页")
        page = str(i)
        res = requests.get(f"https://sj.qubook.cc/read.php?id=92680&txt=/TXT/%C3%DB%CC%C7%B5%C4%D7%CC%CE%B6.txt&yeshu={page}", headers=headers)
        res.encoding = res.apparent_encoding

        soup = BeautifulSoup(res.text, "lxml")
        contents = soup.find("span", id="Content")
        if contents is not None:
            write(contents.getText())
        time.sleep(0.5)


if __name__ == '__main__':
    # res = requests.get("https://sj.qubook.cc/read.php?id=92680&txt=/TXT/%C3%DB%CC%C7%B5%C4%D7%CC%CE%B6.txt&yeshu=160")
    # res.encoding = res.apparent_encoding
    #
    # soup = BeautifulSoup(res.text, "lxml")
    # contents = soup.find("span", id="Content")
    # print(contents.getText())
    request()
