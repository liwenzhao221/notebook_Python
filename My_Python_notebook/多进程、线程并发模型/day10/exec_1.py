"""
模拟多线程下载一个文件
"""

from threading import Thread,Lock
import os

lock = Lock()  #锁
# 模拟服务器地址，其中有若干的路径下有目标资源
urls = ["/home/tarena/",
"/home/tarena/桌面/",
"/home/tarena/视频/",
"/home/tarena/图片/",
"/home/tarena/vscode/",
"/home/tarena/文档/",
"/home/tarena/下载/",
"/home/tarena/音乐/",
]

# 先判定哪些路径中有想要的文件
filename = input("要下载的文件:")
explorer = []
for i in urls:
    if os.path.exists(i+filename):
        explorer.append(i+filename)

# 没有文件
if not explorer:
    print("没有资源")
    os._exit(0)

# 文件打下
file_size = os.path.getsize(explorer[0])
# 将文件分块
block_size = file_size // len(explorer)

# 创建一个本地文件
fd = open(filename,'wb')

# 下载一块内容（文件的一部分）
def load(path,num):
    f = open(path,'rb')
    seek_num = block_size * (num - 1)
    f.seek(seek_num)
    data = f.read(block_size)
    with lock:
        fd.seek(seek_num)
        fd.write(data)

    # fd.seek(seek_num)
    # # 下载过程
    # size = block_size
    # while True:
    #     if size <= 1024:
    #         data = f.read(size)
    #         fd.write(data)
    #         break
    #     else:
    #         data = f.read(1024)
    #         fd.write(data)
    #         size -= 1024

num = 1
jobs = []
for path in explorer:
    t = Thread(target=load,args=(path,num))
    jobs.append(t)
    t.start()
    num += 1  # 下载第几块

for i in jobs:
    i.join()

