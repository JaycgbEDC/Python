import time


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def good_fibonacci(n):
    if n <= 1:
        return (n, 0)
    (a, b) = good_fibonacci(n - 1)
    return (a + b, a)


def test():
    n = int(input('输入斐波那契数：'))
    start1 = time.time()
    res1 = fibonacci(n)
    end1 = time.time()
    start2 = time.time()
    res2 = good_fibonacci(n)[0]
    end2 = time.time()
    print('原始递归计算Fibonacci用时: {0}，结果为: {1}'.format(end1 - start1, res1))
    print('改进递归计算Fibonacci用时: {0}，结果为: {1}'.format(end2 - start2, res2))


if __name__ == '__main__':
    test()