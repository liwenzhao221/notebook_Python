"""
poll_server　完成ｔｃｐ并发服务
重点代码

【1】 创建套接字
【2】 将套接字register
【3】 创建查找字典，并维护
【4】 循环监控IO发生
【5】 处理发生的IO
"""
from socket import *
from select import *

#　创建监听套接字，作为关注的ＩＯ
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 创建ｐｏｌｌ对象
p = poll()

#　建立查找字典，通过ＩＯ的fileno查找io对象
#　始终与ｒｅｇｉｓｔｅｒ的ＩＯ保持一直
fdmap = {s.fileno():s}

#　关注　ｓ
p.register(s,POLLIN|POLLERR)

#　循环监控ＩＯ发生
while True:
    events = p.poll() # 阻塞等待ＩＯ发生
    #　循环遍历查看哪个ＩＯ准备就绪
    for fd,event in events:
        print(events)
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            #　关注客户端连接套接字
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()] = c  #　维护字典
        elif event & POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd) #　取消监控
                fdmap[fd].close()
                del fdmap[fd] #　从字典删除
                continue
            print(data)
            p.register(fdmap[fd],POLLOUT)
        elif event & POLLOUT:
            fdmap[fd].send(b'OK')
            p.register(fdmap[fd], POLLIN)














