"""
测算一个大列表，插入一个数据的时间
"""

import time
from linklist import *

l = []
link = LinkList() #链表

for i in range(999999):
    l.append(i)

# link.init_list(l)

tm = time.time()
l.insert(0,8866)
# link.head_insert(8866)
print(time.time() - tm)