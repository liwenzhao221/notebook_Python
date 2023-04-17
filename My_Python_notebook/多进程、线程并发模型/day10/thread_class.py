from threading import Thread

class ThreadClass(Thread):
    def __init__(self, value):
        self.value = value
        super().__init__()  # 加载父类init

    def f1(self):
        print("步骤1")

    def f2(self):
        print("步骤2")

    # 作为流程启动函数
    def run(self):
        for i in range(self.value):
            self.f1()
            self.f2()


if __name__ == '__main__':
    t = ThreadClass(2)
    t.start()
    t.join()
