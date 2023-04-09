"""
thread2.py
线程基础演示实例 2
"""
from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    print("线程函数传参")
    sleep(sec)
    print("%s执行完毕"%name)

# 创建多个线程
jobs=[]
for i in range(3):
    t = Thread(target=fun,args=(2,),
               kwargs={'name':'T%d'%i})
    jobs.append(t)  # 存线程对象
    t.start()

for i in jobs:
    i.join()
