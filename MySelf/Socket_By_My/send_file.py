from socket import *
from time import sleep

from config import *

s = socket()
s.connect((IP,PORT))
f = open('xxx.jpg','rb')
while True:
    data = f.read(1024)
    if not data:
        sleep(1.5)
        s.send(b'##')
        break
    s.send(data)

sleep(1.5)
s.send(b'send over')
s.close()
f.close()


