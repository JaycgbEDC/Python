# 编写函数fast_goldbach验证哥德巴赫猜想，该函数利用sympy包中的isprime函数判断质数


import time
from math import sqrt
from sympy import isprime


def my_isprime(n):
    if n >= 2:
        for i in range(2, int(sqrt(n) + 1)):
            if n % i == 0:
                return False
    else:
        return False
    return True


def goldbach(n):
    if n <= 2 or n % 2 != 0:
        print('请输入大于2的偶数')
        return
    for i in range(2, n // 2 + 1):
        if my_isprime(i) and my_isprime(n - i):
            print('{0} = {1} + {2}'.format(n, i, n - i))


def fast_goldbach(n):
    if n <= 2 or n % 2 != 0:
        print('请输入大于2的偶数')
        return
    for i in range(2, n // 2 + 1):
        if isprime(i) and isprime(n - i):
            print('{0} = {1} + {2}'.format(n, i, n - i))


def test_goldbach():
    n = int(input('请输入大于2的偶数：'))
    while n != 0:
        start1 = time.time()
        goldbach(n)
        end1 = time.time()
        start2 = time.time()
        fast_goldbach(n)
        end2 = time.time()
        print('法1用时: {0}\n法2用时: {1}'.format(end1 - start1, end2 - start2))
        n = int(input('请输入大于2的偶数：'))


if __name__ == '__main__':
    test_goldbach()