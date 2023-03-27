"""
读取二进制文件input.txt，该文件包含了20k个整数，且用struct模块序列化的
在20000个数中找一个满足下列条件的最大集合：
  集合中所有数之间的最大公因数是1（即两两互质）
"""


import os
import struct
from sympy import isprime


def factors_num(num):
    """ 查找num的因子 """
    res = set()
    while num != 1:
        for i in range(2, num + 1):
            if num % i == 0:
                res.add(i)
                num //= i
                break
    return res


def func():
    os.chdir('./苏大/历年上机/2018')
    res = set()
    with open('./input.txt', 'rb') as fp:
        temp = []
        size = struct.calcsize('i')  # 计算整数所占字节数
        s = fp.read(size)
        while s:
            num = struct.unpack('i', s)[0]
            temp.append(num)
            s = fp.read(size)
        temp = sorted(set(temp))
        factors = set()
        for num in temp:
            factor = factors_num(num)
            if factor & factors:
                continue
            res.add(num)
            factors = factors | factor


if __name__ == "__main__":
    print(func())