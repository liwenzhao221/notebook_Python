"""
编写接口程序,从终端输入端口名称,获取端口信息中的address

思路: 1. 通过端口名称,分离出对应段落
    2. 在段落正则匹配到address
"""

import re

def get_address(port):
    f = open("exc.txt")
    while True:
        # 获取一段
        data = ''
        for line in f:
            if line == '\n':
                break
            data += line

        # 文件已经结束
        if not data:
            break

        # 判断是不是想要的段落
        obj = re.match(port,data)
        if obj:
            # 如果obj不是None说明找到目标段
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            pattern = r"([0-9]{1,3}\.){3}[0-9]{1,3}/\d+|Unknow"
            address = re.search(pattern,data).group()
            return address

if __name__ == '__main__':
    port = input("端口:")
    print(get_address(port))
