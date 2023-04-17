from socket import *

IP = '127.0.0.1'
PORT = 8080
ADDR = (IP, PORT)

s = socket()
s.bind(ADDR)
s.listen(5)
while True:
    print("Listen port 8080..")
    try:
        connfd,addr = s.accept()
        print('Connect from %d'%addr)
    except KeyboardInterrupt:
        print('Server is exit')
        break
    except Exception as e:
        print('进入了未知的异常')
        print(e)
        break
    else:
        while True:
            data = connfd.recv(1024).decode()
            if not data:
                break
            print(data)
            connfd.send(b'Thank you,I will learn more')
        connfd.close()

s.close()
