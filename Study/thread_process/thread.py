from threading import Thread


class MyThead(Thread):
    def __init__(self):
        Thread.__init__(self)  # 要求实现 Thread的初始化方法
        self.name = '次线程'
    def run(self) -> None:  # 固定的-> 当线程被执行的时候, 被执行的就是run()
        for i in range(100):
            print(f'{self.name}: {i}')


def func(name):
    for i in range(100):
        print(f'{name}: {i}')


def way1():
    """ 函数调用实现多线程 """
    t = Thread(target=func, args=('次线程', ))
    t.start()  # 多线程状态为可以开始工作状态, 具体的执行时间由CPU决定


def way2():
    """ 创建类实现多线程 """
    t = MyThead()
    t.start()


def main():
    # way1()
    way2()
    for i in range(100):
        print(f'主线程: {i}')


if __name__ == '__main__':
    main()