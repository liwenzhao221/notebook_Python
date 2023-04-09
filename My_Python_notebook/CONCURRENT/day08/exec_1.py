from multiprocessing import Process
from timeit import timeit

# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        # 除了1和其本身出现了能被整除的数
        if n % i == 0:
            return False
    return True

# 单进程完成任务
@timeit
def no_multi_process():
    prime = []
    for i in range(1,100001):
        if isPrime(i):
            prime.append(i)
    sum(prime)

# 自定义进程类
class Prime(Process):
    def __init__(self,prime,begin,end):
        self.prime = prime
        self.begin = begin  # 取值的开始
        self.end = end   # 取值的末尾
        super().__init__()
    def run(self):
        for i in range(self.begin,self.end):
            if isPrime(i):
                self.prime.append(i)
        sum(self.prime)

@timeit
def use_4_process():
    prime = []
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(prime,i,i+25000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

@timeit
def use_10_process():
    prime = []
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(prime,i,i+10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

if __name__ == '__main__':
    # no_multi_process()
    # use_4_process()
    use_10_process()

