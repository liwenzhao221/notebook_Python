'''
HTTPServer 部分的主程序：

获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接受反馈数据
将数据组织为Response格式发送给客户端
'''
import json
from socket import *
import sys
from threading import Thread
import re
# import chardet

from config import *

# 服务器地址
ADDR = (HOST, PORT)

# 和web frame 通信的函数
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip,frame_port))
    except Exception as e:
        print(e)
        return
    # 将字典转换为json
    data = json.dumps(env)
    # 将解析后的请求发送给webframe
    s.send(data.encode())
    # 接受来自webframe数据
    data = s.recv(4096*100).decode()
    #print(json.loads(data))
    return json.loads(data)

# 将httpserver基本功能封装为类
class HTTPServer:
    def __init__(self):
        self.address = ADDR
        self.creat_socket()  # 和浏览器交互
        #self.connect_socket()  # 连接webframe
        self.bind()

    # 创建套接字
    def creat_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 创建和webframe交互的套接字
    # def connect_socket(self):
    #     self.connect_sockfd = socket()
    #     frame_addr = (frame_ip,frame_port)
    #     try:
    #         self.connect_sockfd.connect(('127.0.0.1',8080)) # 连接另外一个后端应用
    #     except Exception as e:
    #         print(e)
    #         sys.exit()

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.ip = self.address[0]
        self.port = self.address[1]

    # 启动服务
    def serve_forever(self):
        # 多线程的模型
        self.sockfd.listen(5)
        print('Listen the port : %s' % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print('Connect from ', addr)
            client = Thread(target=self.handle, args=(connfd,))
            client.setDaemon = True # python3.10后对之前的写法做了优化
            client.start()

    # 具体处理客户端请求任务
    def handle(self, connfd):
        # 获取HTTP请求
        request = connfd.recv(4096).decode()
        # r = chardet.detect(request)['encoding']

        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)' # 解释：\s用于匹配空格
        try:
            env = re.match(pattern,request).groupdict()# 返回捕获组组名和内容字典
        except:
            # 客户端断开
            connfd.close()
            return
        else:
            data = connect_frame(env)
            if data:
                self.response(connfd,data)
            # # 将字典转换为json
            # data = json.dumps(env)
            # # 将解析后的请求发送给webframe
            # self.connect_sockfd.send(data.encode())
            # # 接受来自webframe数据
            # data = self.connect_sockfd.recv(4096*100).decode()
            # #print(json.loads(data))
            # self.response(connfd,json.loads(data))

    # 给浏览器发送数据
    def response(self,connfd,data):
        # data=>{'status':'200','data':'xxxxx'}
        if data['status'] == '200':
            responseHeaders = 'HTTP/1.1 200 OK\r\n' # 相应行
            responseHeaders += 'Content-Type:text/heml\r\n'
            responseHeaders += '\r\n'
            responseBody = data['data']

        elif data['status'] == '404':
            responseHeaders = 'HTTP/1.1 404 Not Found\r\n'  # 相应行
            responseHeaders += 'Content-Type:text/heml\r\n'
            responseHeaders += '\r\n'
            responseBody = data['data']

        # 给浏览器发送数据
        response_data = responseHeaders + responseBody
        connfd.send(response_data.encode())





httpd = HTTPServer()
httpd.serve_forever()
