'''
一个数可以分解为多个质数乘积的结果
ex: 18 = 2*3*3
:param n:
:return: 所分解成质因子的个数
'''


def func(n):

    def isprime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    if n <= 1 or isprime(n):
        return 0
    count = 0

    while n != 1:
        for num in range(2, n + 1):
            if n % num == 0 and isprime(num):
                n //= num
                count += 1
                break
    return count


print(func(27))