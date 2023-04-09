"""
空洞文件
"""

f = open('test','wb')

f.write(b'START')
f.seek(1024*1024*100,2)
f.write(b'END')

f.close()