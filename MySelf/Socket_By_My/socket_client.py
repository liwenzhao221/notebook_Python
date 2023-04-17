from socket import *

IP = '127.0.0.1'
PORT = 8080
ADDR = (IP,PORT)

s = socket()
s.connect(ADDR)

while True:
    data = input('请输入:')
    s.send(data.encode())
    mes = s.recv(1024)
    # if not mes:
    #     break
    print(mes)

s.close()