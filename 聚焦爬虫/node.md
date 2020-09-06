## 聚焦爬虫
### 编码流程
1. 指定url
2. 发起请求
3. 获取响应数据
4. 数据持久化
5. 持久化数据存储

## 数据解析分类
* 正则
* bs4
* xpath

## 数据解析原理
* 解析局部的文本内容，标签之间或者标签中的属性内容进行提取
    * 对指定标签进行定位
    * 标签内属性进行提取
    
    
## 正则
### 常用正则表达式
标识 | 备注
---|---
.| 除换行意外所有的字符
[] | [a-z] 匹配集合中的任意字符
\d| 数字[0-9]
\D | 非数字
\w | 数字，字母，下划线，中文
\W | 非\w
\s | 所有的空白字符包，制表符等
\S | 非空白
* | 任意多次 >=0
+ | 至少一次 >=1
? | 可有可无， 0或者1次
{n} | 固定n次
{n, } | 至少n次
{n,m} | n-m次
$ | 以什么结尾
^ | 以什么开头
.* | 贪婪模式
.*? | 非贪婪模式

## bs4
* bs4数据解析原理
    * 实例化BeautifulSoup对象，将页面源码加载到对象中
    * 通过BeautifulSoup对象相关属性或者方法对标签定位，数据提取
* 安装
    * pip install bs4
    * pip install lxml
* bs4使用步骤
    * 引入对象
        from bs4 impost BeautifulSoup
    * 实例化BeautifulSoup对象
        soup = BeautifulSoup(res, 'lxml')
    * 使用
        * soup.tagName: 返回第一次出现的这个标签
        * soup.find(): 返回第一次出现的搜索的内容
        * soup.find_all(): 返回查询的内容的列表
        * soup.select(): 层级选择器
        * soup.p.text/get_text():获取p 标签下所有的文本内容
        * soup.p.string: 获取该标签下直属内容
        * soup.a['href] = soup.a.get('href'): 获取a标签的href属性
## xpath
* xpath原理
    * 实例化一个etree对象，且需将被解析页面源码加载到对象中
    * 调用etree对象中的xpath
* 安装
    * pip install xpath

    
## 通用处理中文乱码
1. res.encode('iso-8859-1').decode('gbk'')
    