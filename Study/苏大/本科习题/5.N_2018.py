# 2h：矩阵乘法不会
import math
import re


def func1():
    """ 判断整数m、n是否互质: 运用求最大公约数方法 """
    m, n = eval(input())
    if m <= 1 or n <= 1:
        return False
    while n:
        m, n = n, m % n
    return m == 1


def func2():
    """ 求一个整数列表的逆序数 """
    s = input('输入一个整数列表: ')
    pat = re.compile(r'\d')
    l = list(map(int, pat.findall(s)))
    res = 0
    if l == None or len(l) == 1:
        return 0
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                res += 1
    return res


def func3(mat1, mat2):
    """ 矩阵的乘法 """
    mat3 = []
    m, n = len(mat1), len(mat2)
    for i in range(m):
        mat3.append([])
        for j in range(len(mat2[0])):
            v = [mat2[k][j] for k in range(n)]
            mat3[i].append(sum([v1 * v2 for v1, v2 in zip(mat1[i], v)]))
    return mat3


def func4():
    """ 一维列表转为二维列表 """
    s = input('输入一个n*n的整数列表: ')
    pat = re.compile(r'\d')
    l = list(map(int, pat.findall(s)))
    res = []
    n = int(math.sqrt(len(l)))
    count = 0
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(l[count])
            count += 1
        res.append(temp)
    return res


def func5():
    """ 单词排序 """
    s = input('输入一个英文单词字符串，用空格隔开：')
    l1 = s.split()
    d = {}
    for i in l1:
        d[i] = d.get(i, 0) + 1
    res = sorted(d, key = lambda x: d[x], reverse = True)[:3]
    return res


def func6():
    """ Jaccard系数（可用集合的并交做） """
    s_in = input('输入两个单词，用逗号隔开')
    s, t = s_in.split(',')
    a = b = c = 0
    for i in set(s):
        if i in t:
            a += 1
        else:
            b += 1
    c = len(set(t)) - a
    return (a, b, c)
    

def func7():
    """ 统计字符数最多值 """
    s = list(input('输入一个非空字符串：').upper())
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    res = list(d.items())
    res.sort(key = lambda x: x[1], reverse = True)
    return [res[0][0], res[0][1]]


def func8():
    """ 字符串提取整数计算平均值排序 """
    s = input('输入一个包含整数的字符串: ')
    pat = re.compile(r'\d{3,5}')
    l = list(map(int, pat.findall(s)))
    def cal_mean(x):
        s = str(x)
        sum = 0
        for i in s:
            sum += int(i)
        return sum / len(s)        
    l.sort(key = lambda x: cal_mean(x), reverse = True)
    return l


if __name__ == '__main__':
    print(func1())
    # print(func2())
    # print(func3([[1, 2], [1, 3]], [[1, 1, 1], [1, 1, 1]]))
    # print(func4())
    # print(func5())
    # print(func6())
    # print(func7())
    # print(func8())