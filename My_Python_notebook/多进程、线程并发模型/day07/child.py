"""
创建二级子进程处理僵尸
"""
import os
from time import sleep

def f1():
    for i in range(3):
        sleep(2)
        print("写代码")

def f2():
    for i in range(2):
        sleep(4)
        print("测代码")

pid = os.fork()
if pid == 0:
    p = os.fork()  # 创建二级子进程
    if p == 0:
        f1()
    else:
        os._exit(0)  # 一级子进程退出
else:
    os.wait()  # 等待回收一级子进程
    f2()