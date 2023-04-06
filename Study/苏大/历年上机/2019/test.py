"""
    (1)	编写函数read_file从文件中读取数据，将所有的整数按照其在文件中出现的顺序依次存储到数组arr中；
    (2)	编写函数print将数组arr显示在屏幕上，每行显示n个数，每个整数占6列；
    (3)	编写函数count统计数字0至9在数组arr所有整数中的出现次数，将结果放入数组res中（即res[0]存储数字0的出现次数，
    res[1]存储数字1的出现次数，其余以此类推）；
    (4)	编写函数print_res将数组res显示在屏幕上，每行显示5个数，可以复用步骤(2)中print函数；
    (5)	编写函数sort_array将数组arr中的整数按照因子和从小到大排序，如果两个整数的因子和相等，
    则按照它们的自然大小排序（注意：计算一个整数的因子和时包括1和其本身）；
    (6)	编写函数filter_array对数组arr中的整数进行筛选，结果继续保存在arr中，筛选规则如下：保留所有的偶数，
    同时保证这些偶数按照从小到大排序。说明：完成筛选之后，数组arr中的元素可以分成两部分，前半部分是有效内容，
    即所有的偶数，后半部分则是无效内容，参数size记录了数组arr中有效内容的长度（注意：筛选要求在原数组上进行，
    如使用新的辅助数组来完成筛选，扣10分）；
    (7)	编写函数write_file对数组arr中的有效内容（即所有偶数）进行质因数分解，并将结果输出到屏幕和文本文件output.txt中。
    输出要求：每一个整数的质因数分解结果占一行，具体显示格式如下图所示：
    :return:
"""


import os
from math import sqrt


def read_file(filename):
    os.chdir('./苏大/历年上机/2019')
    with open(filename, 'r') as fp:
        arr = fp.read().split()
        return list(map(int, arr))


def my_print(arr, n):
    count = 0
    for num in arr:
        count += 1
        print('{0:<6d}'.format(num), end = '')
        if count == n:
            count = 0
            print()


def count(arr):
    res = [0] * 10
    for num in arr:
        for ch in str(num):
            res[int(ch)] += 1
    return res


def print_res(res):
    my_print(res, 5)


def sort_array(arr):

    def factor_sum(num):
        res = 1 + num
        for i in range(2, int(num**(1/2)) + 1):
            if num % i == 0:
                if num // i != i:
                    res += i + num // i
                else:
                    res += i
        return res

    arr.sort(key = lambda x: (factor_sum(x), x))


def filter_array(arr):
    # 这其实是一个算法---偶数按从大到小排在前面
    i, j = 0, len(arr) - 1
    size = 0
    arr.sort()
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            temp = arr[i]
            arr[i] = arr[size]
            arr[size] = temp
            size += 1
    return size


def factor(num):
    """ 求数num的因数之和 """
    res = []
    while num != 1:
        for i in range(2, num + 1):
            if num % i == 0:
                res.append(i)
                num //= i
                break
    return '*'.join(list(map(str, res)))


def write_file(arr, size):
    with open('./output.txt', 'w+') as fp:
        for i, num in enumerate(arr[:size]):
            s = factor(num)
            fp.write(s + '\n')


if __name__ == "__main__":
    arr = read_file('./data.txt')
    my_print(arr, 5)
    res = count(arr)
    print_res(res)
    sort_array(arr)
    size = filter_array(arr)
    my_print(arr, 10)
    write_file(arr, size)