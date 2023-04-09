"""
epoll_server　完成ｔｃｐ并发服务
"""
from socket import *
from select import *

#　创建监听套接字，作为关注的ＩＯ
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 创建eｐｏｌｌ对象
ep = epoll()

#　建立查找字典，通过ＩＯ的fileno查找io对象
#　始终与ｒｅｇｉｓｔｅｒ的ＩＯ保持一直
fdmap = {s.fileno():s}

#　关注　ｓ
ep.register(s,EPOLLIN|EPOLLERR)

#　循环监控ＩＯ发生
while True:
    events = ep.poll() # 阻塞等待ＩＯ发生
    print("你有新的ＩＯ需要处理哦")
    #　循环遍历查看哪个ＩＯ准备就绪
    for fd,event in events:
        print(events)
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            #　关注客户端连接套接字
            ep.register(c,EPOLLIN|EPOLLET) #　设置边缘触发
            fdmap[c.fileno()] = c  #　维护字典
        # elif event & EPOLLIN:
        #     data = fdmap[fd].recv(1024).decode()
        #     if not data:
        #         ep.unregister(fd) #　取消监控
        #         fdmap[fd].close()
        #         del fdmap[fd] #　从字典删除
        #         continue
        #     print(data)
        #     ep.unregister(fd) # 先取消关注再重新添加
        #     ep.register(fdmap[fd], EPOLLOUT)
        # elif event & POLLOUT:
        #     fdmap[fd].send(b'OK')
        #     ep.unregister(fd)
        #     ep.register(fdmap[fd], EPOLLIN)














