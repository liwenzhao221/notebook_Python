"""
协程行为示例
"""

from greenlet import greenlet

def fun1():
    print("执行 fun1")
    gr2.switch()
    print("结束 fun1")
    gr2.switch()

def fun2():
    print("执行 fun2")
    gr1.switch()
    print("结束 fun2")

# 将函数变为协程
gr1 = greenlet(fun1)
gr2 = greenlet(fun2)

gr1.switch() # 选择执行的协程函数

