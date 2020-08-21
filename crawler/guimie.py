__author__ = 'wangxiao'

import requests
import re
import bs4
from numpy import *
import pandas
import jieba

# 获取返回的页面xml数据
def get_data():
    url = "https://comment.bilibili.com/120785256.xml"
    response = requests.get(url).content.decode("utf-8")
    return response


# 提取游泳的弹幕数据
def parse_html(response):
    """
    bs4解析xml
    """
    soup = bs4.BeautifulSoup(response)
    list = soup.findAll(name='d')
    danmu = [i.text for i in list]
    return danmu

# 存储弹幕数据
def save_csv(danmu):
    data = {
        "danmu": danmu
    }
    pandas_data = pandas.DataFrame(data)
    pandas_data.to_csv('danmu.csv', index=False, header=False, mode='w', encoding="utf-8")

# 数据处理
# def operation_data(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         # 加载用户自定义字典
#         jieba.load_userdict('../load_userdict.txt')
#         # 换行替换为空格
#         reader = f.read().replace('/n', '')
#         # 加载停用词
#         with open('../stop.txt', 'r', encoding='utf-8') as stop:
#             stopwords = [line.strip() for line in stop.readline()]
#         # 分词
#         list = jieba.cut(reader, cut_all=all)
#         sentence = ''
#         for word in list:
#             if word not in stopwords and word.isspace() == False:
#                 sentence +=word
#                 sentence += ','
#         #sentence = sentence[:-1]
#         return sentence

def operation_data(file):
    with open(file, encoding='utf-8') as f:
        txt = f.read()
        txt = txt.split()
        data_list = [jieba.lcut(line) for line in txt]
    # 读取停用词
    with open('../stop.txt', 'r', encoding='utf-8') as stopfile:
        stop = stopfile.read()
        stop = stop.split()
        stop +=stop

    # 去掉停用词
    # for words in data_list:
    #     if words not in stop:
    #         print(words)
    # allow_words = data_cut.apply(lambda x:[i for i in x if i not in stop])


    #print(data_list)
    print(stop)

if __name__ == '__main__':
    # response = get_data()
     # danmu = parse_html(response)
     # save_csv(danmu)
    #print(operation_data('danmu.csv'))
    operation_data('danmu.csv')