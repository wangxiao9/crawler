### JsonPath


```
1. 安装
    pip install jsonpath
    
2. step
    obj = json.load("xx.json", 'r', encoding='utf-8')
    res = jsonpath.jsonpath(obj, 'expression')
    
```


### expression
- $. 

| expression | description |
| --- | --- |
| $ | root对象 |
| @  | 当前对象 |
| . 或者[] | 子运算符 |
| .. | 递归下降 |
| * | 通配符 |
|?()| 过滤|


