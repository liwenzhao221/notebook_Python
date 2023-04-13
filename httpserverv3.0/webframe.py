'''
webframe.py  模拟后端应用工作流程
从httpserver接受具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
'''


import json
from socket import *
from settings import *
from select import select
from urls import *

# 应用类，处理某一方面的请求
class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd.bind((frame_ip,frame_port))

    # 启动服务
    def start(self):
        self.sockfd.listen(3)
        print('Start app listen %s'%frame_port)
        # c, addr = self.sockfd.accept()
        # while True:
        #     #c, addr = self.sockfd.accept()
        #     data = c.recv(1024).decode()
        #     print(json.loads(data))
        #     d = {'status': '200', 'data': 'xxxxxxx'}
        #     c.send(json.dumps(d).encode())
        self.rlist.append(self.sockfd)
        # select 监控请求
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = r.acctpe()
                    self.rlist.append(connfd)
                else:
                    self.handle(r)
                    self.rlist.remove(r)
    # 处理具体的httpserver请求
    def handle(self,connfd):
        request = connfd.recv(1024).decode()# 接收到的是一个json
        request = json.loads(request)
        # print(request)
        # d = {'status':'200','data':'xxxxxx'}
        # connfd.send(json.dumps(d).encode())
        # request -->{'method':'GET','info':'/'}
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])

        elif request['method'] == 'POST':
            pass

        # 将数据发送给httpserver
        # response => {'status':'20','data':'xxxx'}
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.colse()

    # 处理网页
    def get_html(self,info):
        if info == '/':
            filename = STATIC_DIT + '/index.html'
        filename = STATIC_DIT + info
        try:
            fd = open(filename)
        except Exception as e:
            fd = open(STATIC_DIT + '/404.html')
            return {'status':'404','data':fd.read()}
        else:
            return {'status': '200', 'data': fd.read()}

    # 处理数据
    def get_data(self,info):
        for url,func in urls: # 使用两个变量来取urls中的urls列表
            if url == info:
                return {'status':'200','data':func()}

        return {'status':'404','data':'sorry ...'}
app = Application()
app.start()




