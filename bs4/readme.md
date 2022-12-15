### bs4
[bs4 reference](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
```
1. 安装
    pip install bs4
2. 引入
    from bs4 import BeaufifulSoup
3. 生成对象
    soup = BeautifulSoup(res.text, "html.parser")
    contents = soup.find("xx", class_="xxx")
```

### 解析器

| 解析器 | 使用 | 优势 |
| --- | --- | --- |
| python 标准库 | BeautifulSoup(html, “html.parser”) |  |
| lxml HTML	 | BeautifulSoup(html, “lxml”)	 |  |
| lxml XML | BeautifulSoup(html, [“lxml”, “xml”]) BeautifulSoup(html, “xml”) | 解析xml  |
|html5lib | BeautifulSoup(html, “html5lib”)	|


```
如果用到 html5lib
pip install html5lib

```


#### 使用

```
bs4.prettify()  //输出全部内容
bs4.tag // 标签
bs4.select('.class')
bs4.find('', '')
bs4.finadAll()
getText() // 获取文本
```
