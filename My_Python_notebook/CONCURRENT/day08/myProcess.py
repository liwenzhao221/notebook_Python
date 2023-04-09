"""
自定义进程类
"""
from multiprocessing import Process
from time import *

# 自定义进程类
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__() # 加载父类init

    def f1(self):
        print("步骤1")
    def f2(self):
        print("步骤2")

    # 作为流程启动函数
    def run(self):
        for i in range(self.value):
            self.f1()
            self.f2()

if __name__ == '__main__':
    p = MyProcess(2)
    p.start()
    p.join()
