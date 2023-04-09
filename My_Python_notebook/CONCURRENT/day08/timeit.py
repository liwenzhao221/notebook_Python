import time

def timeit(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print("%s函数运行时间：%.6f"%(func.__name__,
                               end_time-start_time))
        return res
    return wrapper
