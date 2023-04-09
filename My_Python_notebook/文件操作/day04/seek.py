"""
seek.py  文件偏移量测试
"""

# 以r,w打开文件偏移量在开头，以a打开文件偏移量在结尾
f = open("mm.jpg",'rb+')
print(f.tell())

# f.write("Hello world")
#
# print(f.tell())

# 以开头为基准向后移动5个字符
f.seek(1024,0)

f.write('你好'.encode())
# data = f.read()
# print(data)

f.close()
