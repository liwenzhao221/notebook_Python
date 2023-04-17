"""
获取进程PID号
"""

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    print("Child PID:",os.getpid()) # 自己pid
    print("Get parent PID:",os.getppid()) # 父pid
else:
    print("Parent PID:", os.getpid())  # 自己pid
    print("Get child PID:",pid)

