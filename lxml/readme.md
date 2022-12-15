### xpath

- 实例化一个etree的对象
- 调用etree对象结合xpath 定位，捕捉到内容

### 步骤

```
1. pip install lxml
2. 导入lxml.etree
    from lxml import etree
3. 解析本地文件
    tree = etree.parse("xxx.html")
4. 服务器响应
    tree = etree.HTML(response.read().decode("utf-8"))
5. xpath
    tree.xpath(表达式)
```
### 使用规则

[xpath reference](https://www.w3school.com.cn/xpath/index.asp)

| expression | description |
| --- | --- | 
| // | 查询所有子节点 | 
| / | 子节点 | 
| //div[@class=""] | 查找div 节点下class属性值 |
| //div/text() | div节点下文本内容 | 
| //meta[not(@itemprop)] | 不包含 | 
| //li[contains(@class, "ddd")] | 包含模糊查询 |

