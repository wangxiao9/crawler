__author__ = 'wangxiao'

import re

# 提取python
key1 = "java, python, C++, go"
res1 = re.findall('python', key1)[0]

# 提取标签内容
key2 = '<div class="border"><span>python</span></div><div class="border"><span>java</span></div>'
res2 = re.findall('<span>(.*?)</span>', key2)

# 提取数据
key3 = '今年业绩要达到4亿'
res = re.findall('\d', key3)

# 等等