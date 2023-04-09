"""
gevent生成协程演示
"""

import gevent
from gevent import monkey
monkey.patch_time() # 修改对time模块中阻塞的解释行为
from time import sleep

# 协程函数
def foo(a,b):
    print("Running foo ...",a,b)
    # gevent.sleep(3)
    sleep(3)
    print("Foo again..")

def bar():
    print("Running bar ...")
    # gevent.sleep(2)
    sleep(2)
    print("Bar again..")

# 生成协程对象
f = gevent.spawn(foo,1,2)
g = gevent.spawn(bar)

gevent.joinall([f,g]) #阻塞等待f,g代表的协程执行完毕