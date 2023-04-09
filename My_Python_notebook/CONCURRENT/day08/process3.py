"""
Process 给进程函数传参
"""

from multiprocessing import Process
from time import sleep

# 含有参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

# 通过args 给函数位置传参
# p = Process(target=worker,args=(2,'Levi'))
p = Process(target=worker,args=(2,),
            kwargs={'name':'Baron'})
p.start()
p.join()



