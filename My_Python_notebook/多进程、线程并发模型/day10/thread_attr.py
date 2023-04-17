"""
thread_attr.py
线程属性示例
"""

from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性示例")

t = Thread(target = fun,name = "Tarena")

t.setDaemon(True) # 主线程退出分支线程也退出

t.start()

t.setName("Tedu")
print("Name:",t.getName()) # 线程名称
print("is alive:",t.is_alive()) # 是否在生命周期
print("Daemon:",t.isDaemon())
# t.join()
