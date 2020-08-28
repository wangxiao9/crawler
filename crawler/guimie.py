__author__ = 'wangxiao'

import requests
import re
import bs4
from matplotlib.image import imread
from numpy import *
import pandas
import jieba
import matplotlib.pyplot as plt

# 获取返回的页面xml数据
from wordcloud import WordCloud


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
#     with open('../stop.txt', 'r', encoding='utf-8') as stopfile:
#         stop = stopfile.read()
#         stop = stop.split()
#         stop +=stop
#         # 分词
#     list = jieba.cut(reader, cut_all=all)
#     sentence = ''
#     for word in list:
#         if word not in stop and word.isspace() == False:
#             sentence +=word
#             sentence += ','
#         # #sentence = sentence[:-1]
#         # return sentence
#     print(sentence)

def operation_data(file):
    with open(file, encoding='utf-8') as f:
        txt = f.read().replace('/n', '')
        txt = txt.split()
        data_list = [jieba.lcut(line) for line in txt]
    # 读取停用词
    with open('../stop.txt', 'r', encoding='utf-8') as stopfile:
        stop = stopfile.read()
        stop = stop.split()
        stop +=stop

    # 去掉停用词
    # for words in data_list:
    #     print(operation_stop_data(words, stop))
    s_data_cut = pandas.Series(data_list)
    all_words_after = s_data_cut.apply(lambda x: [i for i in x if i not in stop])
    # 5 词频统计
    all_words = []
    for i in all_words_after:
        all_words.extend(i)
    word_count = pandas.Series(all_words).value_counts()
    return word_count

#设置图云
def wordCloudPic(word_count):
    pic = imread(r'../1.png')
    wc = WordCloud(background_color="white",
                   max_words=2000,
                   mask=pic,
                   max_font_size=200,
                   random_state=42
                   )
    wc2 = wc.fit_words(word_count)
    plt.figure(figsize=(16, 8))
    plt.imshow(wc2)
    plt.axis("off")
    plt.show()
    wc.to_file("../ciyun.png")


def operation_stop_data(list_data, stop_data):
    new = ''
    for line in list_data:
        if line not in stop_data:
            new = new + line
    return new


if __name__ == '__main__':
    # response = get_data()
     # danmu = parse_html(response)
     # save_csv(danmu)
    #print(operation_data('danmu.csv'))
    word_count = operation_data('danmu.csv')
    wordCloudPic(word_count)