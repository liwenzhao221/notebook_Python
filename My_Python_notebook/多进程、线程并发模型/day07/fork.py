"""
fork.py  fork进程创建演示
"""
import os
from time import sleep

# 创建子进程
pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    # 只有子进程执行
    sleep(3)
    print("The new process")
else:
    # 只有父进程执行
    sleep(4)
    print("The old process")

# 父子进程都执行
print("process test over")
