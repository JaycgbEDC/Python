""" 输入n  找出1~n 中 二进制1比0多的数，升序返回 """


def func1(n):
    l = []
    for num in range(1, n + 1):
        s = bin(num)[2:]
        if s.count('1') > s.count('0'):
            l.append(num)
    return l


if __name__ == '__main__':
    while 1:
        print(func1(int(input())))