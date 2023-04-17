import time



n = 0
with open('log.txt','ab+') as line:
    # while True:
    #     n += 1
    #     time.sleep(1.5)
    #     s = '%d %s\n'%(n,time.ctime())
    #     line.write(s.encode())
    #
    #     line.flush()
    line.seek(0)
    while True:
        data = line.readline()

        print(data)