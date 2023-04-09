from time import sleep
from threading import Thread,Lock

# 交易类
class Account:
    def __init__(self,_id,balance,lock):
        self.id = _id  # 谁
        self.balance = balance # 有多少钱
        self.lock = lock # 锁

    # 取钱
    def withdraw(self,amount):
        self.balance -= amount # 取多少

    # 存钱
    def deposit(self,amount):
        self.balance += amount # 存多少

    # 查看余额
    def get_balance(self):
        return self.balance

# 创建两个账户
Tom = Account('Tom',5000,Lock())
Alex = Account('Alex',8000,Lock())

# 转账行为
def transfer(from_,to,amount):
    # 从 from_ --> to  转amount
    if from_.lock.acquire(): # 锁住自己账户
        from_.withdraw(amount) # 自己账户扣除
        sleep(0.5)
        if to.lock.acquire(): # 对方账户上锁
            to.deposit(amount) # 对方账户增加
            to.lock.release() # 对方解锁
        from_.lock.release() # 自己解锁
    print("%s给%s转了%d"%(from_.id,to.id,amount))

t1 = Thread(target=transfer,args=(Tom,Alex,2000))
t2 = Thread(target=transfer,args=(Alex,Tom,3500))

t1.start()
t2.start()

t1.join()
t2.join()

print(Tom.get_balance())
print(Alex.get_balance())




