"""
buffer.py
缓冲区刷新测试
"""

# f = open('a.py','w',1) # 行缓冲
f = open('a.py','w')

while True:
    data = input(">>")
    if not data:
        break
    f.write(data + '\n')
    f.flush()  # 刷新缓冲区

f.close()