from test import *
# from threading import Thread
from multiprocessing import Process
import time


jobs = []

tm = time.time()
for i in range(10):
    t = Process(target = count,args=(1,1))
    # t = Process(target=io)
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()
print("Process io:",time.time() - tm)
