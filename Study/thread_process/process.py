from multiprocessing import Process


class MyProcess(Process):
    def __init__(self):
        Process.__init__(self)  # 要求实现 Thread的初始化方法
        self.name = '次进程'
    def run(self) -> None:  # 固定的-> 当进程被执行的时候, 被执行的就是run()
        for i in range(100):
            print(f'{self.name}: {i}')


def func(name):
    for i in range(100):
        print(f'{name}: {i}')


def way1():
    """ 函数调用实现多进程 """
    p = Process(target=func, args=('次进程', ))
    p.start()  # 多进程状态为可以开始工作状态, 具体的执行时间由CPU决定


def way2():
    """ 创建类实现多进程 """
    p = MyProcess()
    p.start()


def main():
    way1()
    # way2()
    for i in range(100):
        print(f'主进程: {i}')


if __name__ == '__main__':
    main()