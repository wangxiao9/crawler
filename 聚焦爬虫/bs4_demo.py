__author__ = 'wangxiao'

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>多个层级</span>Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')

# 增加缩进，美化输出
soup.prettify()

# 获取title标题名
soup.title.string

# 获取p标签，获取的是第一个p标签
soup.p


# 查找a标签，获取的也是第一个
soup.find('a')

# 获取所有的a标签，存在列表中
soup.find_all('a')

# 获取id为link2标签
soup.find_all(id='link2')

# 获取class='title'的标签
soup.find_all(class_='title')

# 获取标签文本内容
soup.find(id='link2').text

# 获取标签文本内容
soup.find(id='link2').string

# 获取标签文本内容
soup.find(id='link2').get_text()

# text/get_text()可以获取当前标签中所有的文本， string只能获取直系文本

# 获取第一个a标签下的href属性值
soup.find('a').get('href')

# 获取a标签的name
soup.find('a').name

# select选择器 > 表示一个层级
soup.select('.story > #link1')

# select 空格表示多个层级
print(soup.select('.story > #link1 span'))