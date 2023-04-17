"""
进程退出演示
"""

import os,sys

pid = os.fork()

# 父子进程退出不会影响对方继续执行
if pid < 0:
    print("Error")
elif pid == 0:
    # os._exit(0) # 子进程退出
    print("Child process")
else:
    sys.exit("退出父进程")
    print("Parent process")

