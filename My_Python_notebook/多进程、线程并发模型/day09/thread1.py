"""
thread1.py  线程基础使用
步骤： 1. 创建线程对象
      2. 启动线程
      3. 回收线程
"""

import threading
from time import sleep
import os

a = 1

# 线程函数
def music():
    global a
    print("a = ",a)
    a = 10000
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放: 葫芦娃")

# 线程对象
t = threading.Thread(target = music)
t.start() # 启动线程

for i in range(4):
    sleep(1)
    print(os.getpid(),"播放: 黄河大合唱")

t.join() # 回收线程

print("===========================")

print("a:",a)





