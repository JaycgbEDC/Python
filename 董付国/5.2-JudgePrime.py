# 编写函数，判断一个整数是否为素数

from math import sqrt


def JudgePrime(n):
    if not isinstance(n, int) or n < 2:
        print("请输入大于1的整数！")
        return
    m = int(sqrt(n) + 1)
    for i in range(2, m):
        if n % i == 0:
            return False
    return True


if JudgePrime(7):
    print("素数")