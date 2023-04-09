"""
模拟僵尸进程产生
"""

import os,sys
import signal

# 忽略子进程的退出行为，子进程退出自动由系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    sys.exit(2)
else:
    """
    os.wait() 处理僵尸
    """
    # pid,status = os.wait()
    # print("pid:",pid)
    # print('status:',os.WEXITSTATUS(status))
    while True: # 让父进程不退出
        pass