"""
fork1.py fork进程演示细节
"""

import os
from time import sleep

print("=========================")
a = 1
def fun():
    print("fun .... ")

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("Child process")
    print("a = ",a)  # 从父进程空间拷贝了变量
    fun()
    a = 10000  # 只是修改了自己空间的a
else:
    sleep(1)
    print("Parent process")
    print("a:",a)

print("All a ->",a)