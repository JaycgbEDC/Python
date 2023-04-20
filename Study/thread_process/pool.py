# 线程池: 一次性开辟一些线程. 我们用户直接给线程池子提交任务. 线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def func(name):
    for i in range(100):
        print(f'{name}: {i}')


def create_pool():
    with ThreadPoolExecutor(50) as t:
        for i in range(60):
            t.submit(func, name = f"次线程{i}")


def main():
    create_pool()
    for i in range(100):  # 等待线程池中的任务全部执行完毕. 才继续执行(守护)
        print(f'主线程: {i}')


if __name__ == '__main__':
    main()