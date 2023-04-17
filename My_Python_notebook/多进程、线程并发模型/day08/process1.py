"""
Process 创建进程演示
1. 编写进程函数
2. 生成进程对象
3. 启动进程
4. 回收进程
"""

import multiprocessing as mp
from time import sleep

a = 1

# 进程执行函数
def fun():
    print("开始一个进程")
    sleep(2)
    global a
    print("a = ",a)
    a = 10000
    print("子进程结束")

# 创建进程对象
p = mp.Process(target=fun)
# 启动进程
p.start()

# 父进程执行事件
sleep(3)
print("父进程干点事")

# 回收进程
p.join()

print("a:",a)
"""
pid = os.fork()
if pid == 0:
    fun()
    os._exit()
else:
    os.wait()
"""

print("======================")
