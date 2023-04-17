"单线程"

from test import *
import time

tm = time.time()

for i in range(10):
    count(1,1)
    # io()

print("Single IO:",time.time() - tm)

