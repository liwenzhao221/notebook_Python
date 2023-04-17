"""
gevent server 基于协成的tcp并发
思路 : 1. 每个客户函数端设置为协成
      2. 将socket模块下的阻塞变为可以触发协程跳转
"""
import gevent
from gevent import monkey
monkey.patch_all() # 执行脚本,修改socket
from socket import *

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')
    c.close()

# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

# 循环接收来自客户端连接
while True:
    c,addr = s.accept()
    print("Connect from",addr)
    # handle(c) # 处理具体客户端请求
    gevent.spawn(handle,c) # 协程方案
