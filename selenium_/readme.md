### Selenium

1. Selenium 是一个用于web应用程序测试工具
2. Selenium 测试直接运行再浏览器中，模拟真正的用户
3. 通过driver驱动真实浏览器
4. 支持无界面浏览器操作
5. 

### Installation

[reference](https://python-selenium-zh.readthedocs.io/zh_CN/latest/1.%E5%AE%89%E8%A3%85/)


```
1. pip install selenium
2. google 驱动
    http://chromedriver.storage.googleapis.com/index.html
    
    
或者
1. 安装jave JRE
2. 下载 selenium-server-standalone
    https://selenium-release.storage.googleapis.com/index.html
3. jave -jar selenium-server-standalone-2.x.x.x.jar 驱动通信服务
```


### Selenium 元素定位

[元素定位-reference](https://python-selenium-zh.readthedocs.io/zh_CN/latest/4.%E5%85%83%E7%B4%A0%E5%AE%9A%E4%BD%8D/)

| methods | description |
| --- | --- |
| find_element_by_id  |  通过id |
| find_element_by_name | name |
| find_element_by_xpath | xpath  |
| find_element_by_tag_name | tag name |
| find_element_by_css_selector | css selector |
| find_element_by_link_text | 文本连接 |


### 元素对象


| attr | description |
| --- | --- |
| .get_attribute('xxx') | 获取元素某个属性 |
| .text | 元素文本 |
| .id | 获取id |
| .tag_name | 获取tag name |



### 交互

[交互-reference](https://python-selenium-zh.readthedocs.io/zh_CN/latest/3.%E5%AF%BC%E8%88%AA/#_2)


| key | description |
| --- | --- |
| click | 点击 |
| send_key() | 输入 |
| .back() | 浏览器后退 |
| .forword() | 浏览器前几 |
| .page_source | 获取页面代码 |
| .clear() | 清空输入框 |


### Chrome handless
