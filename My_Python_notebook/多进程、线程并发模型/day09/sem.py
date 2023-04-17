"""
sem.py 信号量演示
注意: 信号量可以当做是一种资源，执行任务需要消耗信号量资源，
这样可以控制进程执行行为
"""

from multiprocessing import Process,Semaphore
from time import sleep
import os

# 创建信号量资源
sem = Semaphore(3)

# 任务函数 (系统中最多能够同时运行三个该任务)
def handle():
    sem.acquire() # 消耗一个信号量
    print("%s执行任务"%os.getpid())
    sleep(2)
    print("%s 拯救了宇宙"%os.getpid())
    sem.release() # 增加一个信号量

jobs = []
for i in range(10):
    p = Process(target = handle)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
