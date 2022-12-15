### 一、What's scrapy
[reference](https://docs.scrapy.org/en/latest/intro/tutorial.html)
爬取网站数据，提取结构性数据的应用框架，可应用于数据挖掘，信息处理，存储隶属数据

#### 1 五大组件组成
- Scheduler ： 它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引擎需要时，交还给引擎。
- Downloader： 负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理
- Spider： 它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)
- Item Pipeline： 它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方.
- Scrapy Engine ： 负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等



#### 2. 工作原理

![原理图](https://note.youdao.com/yws/api/personal/file/WEB520ba11b692f965f594a9074d393e36b?method=download&shareKey=1ed7c0069fccc9f1d1da69773553eb13)



```
1. Spider(核心爬虫文件)发送请求requests -> Scrapy Engine
2. Engine 传给Scheduler 告诉Scheduler 有requests请求
3. Scheduler  接受requests 入队 -> Engine
4. Engine 发送requests(http://www.baidu.com) -> Downloader 
5. Downloader 返回requests 的response -> Engine
6. Engine 返回response -> Spider
7. Spider 数据处理完毕，获取item数据 -> Engine
8. Engine -> Pipline 后期数据处理
    PIPline-> 告诉Sheduler处理的requests -> Engine -> Downloader 循环
```



### 二、 Installation

scrapy主要使用了Twisted, 如果安装不成功，可能是还需要安装Twisted依赖
```
 $ pip install scrapy
```

### 三、开启你的scrapy项目

##### 1. 目录结构
```
1. 创建项目 (不可使用数字开头，不可包含中文)
    $ scrapy startproject <your project name>

2. 目录结构
├── my_scrapy-----------------------------------创建的项目
    ├── my_scrapy --------------------------------创建的项目
       ├── spider
        ├── xxx.py ------------------------------实现爬虫的核心代码
        ├── __init__.py
    ├── __init__.py
    ├── items.py --------------------------------定义数据结构，继承scrapy.Item类
    ├── middlewares.py---------------------------代理 中间件
    ├── pipelines.py ----------------------------管道文件，值越小优先级越高，处理下载数据的后续操作
    ├── settings.py------------------------------配置文件，robot.txt, user-Agent 等
├── scrapy.cfg -------------------------------部署配置文件
```

#### 2. 编写程序


```
1. 自动生成
    $ cd Spider
    $ scrapy genspider hupu hupu.com 
         hupu ----- 程序名字
         hupu.com-- allowed_domains
         
2. 手动创建 hupu.py


class HupuSpider(scrapy.Spider):
    name = 'hupu'
    allowed_domains = ['hupu.com']
    start_urls = ['http://hupu.com/']

    def parse(self, response):
        pass
        
        
- name : 区别不同Spider, 唯一值
- allowed_domains： 允许访问的域名
- start_urls : 起始url
- parse: 解析返回的response


3. 运行爬虫代码
    $ scrapy crawl hupu

```


#### 3. 处理结果

```
parse(self, response)
 - response.text -------- 响应的字符串
 - response.body -------- 响应的二进制文件
 - response.xpath() ----- 返回xpath selector列表
 - extract() ------------ 提取selector 对象
 - extract_first() -------第一个数据
 - getall() --------------获取文本内容 返回列表 
 - get() -----------------获取文本内容，返回字符串
```
#### 4.Selectors

[reference](https://docs.scrapy.org/en/latest/topics/selectors.html)
```
1. 使用shell 获取 xpath对象
    $ scrapy shell https://car.autohome.com.cn/diandongche/list-0-0-0-1-0-0-0-0-1.html
    
2. 使用对象response 返回xpath 选择器
     >> response.xpath("//div")
     
```

| attr | description |
| --- | --- |
| //title//a | 获取标签 |
| //div[@class="sss"] | 获取div标签，class对象sss |
| //div//a/@href | 获取a标签的href对象 |
| //div//p/text() | 获取P标签文本 |
| //a[contains(@href, 'image')] | 标签a 对象包含image |




### 五、CrawlSpider


### 六、日志


```
1. 日志级别
  CRITICAL :严重
  ERROR: 一般错误
  WARNING: 警告
  INFO: 一般信息
  DEBUG: 调试信息
  
2. setting.py
   默认DEBUG
   添加关键字
   
   LOG_FIFE : log记录到文本中
   LOG_LEVEL : 显示日志等级
```


### 七、代理








































