"""
消息队列演示
注意： 消息存入与去除关系为 先入先出
"""

from multiprocessing import Queue,Process
from time import sleep
from random import randint

# 创建队列
q = Queue(5) # 最大存储5个消息

def request():
    for i in range(10):
        x = randint(1,100)
        y = randint(1,100)
        q.put((x,y))  # 写消息队列
        print("=============")

def handle():
    while not q.empty():
        data = q.get() # 读消息队列
        print("x + y = ",data[0]+data[1])
        sleep(2)

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()











