"""
thread_lock.py
线程锁演示
"""

from threading import Thread,Lock

a = b = 0
lock = Lock() # 锁对象

def value():
    while True:
        lock.acquire()
        if a != b:
            print('a = %d,b = %d'%(a,b))
        lock.release() # 解锁操作

t = Thread(target=value)
t.start()

while True:
    with lock:  # with上锁
        a += 1
        b += 1
                # 语句块结束解锁
t.join()

