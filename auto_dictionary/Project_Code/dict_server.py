'''
dict 服务端

功能：业务逻辑处理
模型：多进程tcp并发
'''
import sys
from socket import *
from multiprocessing import Process
import signal  # 处理僵尸进程
from mysql import Database
from time import sleep

# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)
# 建立数据库对象
db = Database(database='auto_dictionary')

# 接受客户端请求，分配处理函数
def request(c):
    db.create_cursor()
    # 循环接受客户端请求
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(),':',data)
        if not data or data[0] == 'E':
            sys.exit()# 对应的子进程退出
        elif data[0] == 'R':
            do_register(c,data)
        elif data[0] == 'L':
            do_login(c,data)
        elif data[0] == 'Q':
            do_query(c,data)
        elif data[0] == 'H':
            do_hist(c,data)

# 服务端注册处理
def do_register(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    # 返回true表示注册成功，false表示注册失败
    if db.register(name,passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')

# 登录
def do_login(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name,passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')

# 查单词
def do_query(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    word = tmp[2]

    # 插入历史记录
    db.insert_hist(name,word)

    # 没找到范湖None，找到返回单词解释
    mean = db.query(word)
    if not mean:
        c.send('没有找到该单词'.encode())
    else:
        msg = '%s : %s'%(word,mean)
        c.send(msg.encode())

# 查询记录
def do_hist(c,data):
    name = data.split(' ')[1]
    r = db.history(name) # 数据库处理
    if not r:
        c.send(b'Fail')
        return
    c.send(b'OK')

    for i in r:
        #i--->(name,word,time)
        msg = '%s %-16s %s'%i
        sleep(0.1)
        c.send(msg.encode())

# 搭建网络
def main():
    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    # 循环等待客户端连接
    print('Listen the port 8000')
    while True:
        try:
            c, addr = s.accept()
            print('Connect from', addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit('服务端退出')
        except Exception as e:
            print(e)
            continue

        # 微客户端创建子进程
        p = Process(target=request, args=(c,))
        p.daemon = True  # 父进程退出，子进程也跟着退出
        p.start()


if __name__ == '__main__':
    main()
