"""
将一个文件拷贝一份，
文件可能是文本文件也可能是二进制文件
"""

# 输入文件名称
filename = input("File:")

try:
    fr = open(filename,'rb')  # 二进制文件操作
except FileNotFoundError as e:
    print(e)
else:
    fw = open('file.jpg','wb')
    #循环读写
    while True:
        data = fr.read(1024)
        if not data:  # 读取结束
            break
        fw.write(data) # 将读取内容写入
    fr.close()
    fw.close()
