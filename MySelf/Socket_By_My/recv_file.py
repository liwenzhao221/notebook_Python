from socket import *
from config import *

s = socket()
s.bind((IP,PORT))
s.listen(5)
f = open('copy.jpg','wb')
connfd,addr = s.accept()
while True:
    data = connfd.recv(1024)
    if data == '#':
        break
    f.write(data)
print(connfd.recv(1024).decode())
f.close()
s.close()


