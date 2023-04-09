"""
file_write.py
文件写操作
"""

# 打开文件
# f = open('a.py','a')
f = open('a.py','w')

# 写操作
# f.write("hello 死鬼\n")
# f.write("哎呀,干啥\n")

# 将列表中每一项分别写入文件内
l = ['hello world\n','hello kitty\n']
f.writelines(l)


# f.close()
