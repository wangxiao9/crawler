__author__ = 'wangxiao'


import time
import re


s = '{  "jsonrpc": "2.0",  "method": "checkApplyFillInStatus",  "id": 0,  "params": [    "3bee1b36-46e5-44af-a6e9-74ee984e3a44",//user_id    "084545f6-ce99-40aa-ab2f-95b8e7cbaf96"//merchant_id  ]}'
express = '{  "jsonrpc": "2.0",  "method": "checkApplyFillInStatus",  "id": 0,'
new = re.findall(express, s, re.S)
print(new)