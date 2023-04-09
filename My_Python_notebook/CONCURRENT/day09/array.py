"""
array.py
共享内存中存放列表，字节串
"""
from multiprocessing import Process,Array

# 创建共享内存，初始数据 [1,2,3,4]
# shm = Array('i',[1,2,3,4])
# shm = Array('i',4) # 开辟4个整形的列表空间
shm = Array('c',b'hello')

def fun():
    # 共享内存对象可以迭代
    for i in shm:
        print(i)
    shm[0] = b'H' # 修改共享内存

p = Process(target=fun)
p.start()
p.join()
for i in shm:
    print(i)
print(shm.value) # 整体打印字节串