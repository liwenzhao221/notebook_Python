'''
dict 客户端

功能：根据用户输入，发送请求，得到结构
结构：一级界面-->注册 登录 退出
    二级界面-->查单词 历史记录 注销
'''
import encodings.oem
from socket import *
from getpass import getpass # 运行只能只用终端，不能使用pycharm，不支持getpass

# 服务器地址
ADDR = ('127.0.0.1',8000)
s = socket()
s.connect(ADDR)

# 注册函数
def do_register():
    while True:
        name = input('User:')
        passwd = getpass()
        passwd1 = getpass('Again:')

        if passwd != passwd1:
            print('两次密码不一致')
            continue
        if ' ' in name or ' ' in passwd:
            print('用户名密码不能有空格')
            continue
        msg = 'R %s %s'%(name,passwd)
        s.send(msg.encode()) # 发送给服务器
        data = s.recv(128).decode()# 接受结果
        if data == 'OK':
            print('注册成功')
        else:
            print('注册失败')
        return

# 搭建客户端网络
def main():

    while True:
        print('''
        ======================Welcome=========================
        1.注册                2.登录                     3.退出
        ======================================================
        ''')
        cmd = input('输入选项：')
        if cmd == '1':
            do_register()
        elif cmd == '2':
            s.send(cmd.encode())
        elif cmd == '3':
            s.send(cmd.encode())
        else:
            print('请输入正确选项')

if __name__ == '__main__':
    main()