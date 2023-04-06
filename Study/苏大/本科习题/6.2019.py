import math
import re


def func1():
    """ 判断点的区域 """
    s = input('输入一个坐标：')
    l = list(map(int, s.split(',')))
    if -1 < l[0] < 1 and -1 < l[1] < 1:
        return 1
    elif (l[0] < -1 or l[0] > 1) or (l[1] < -1 or l[1] > 1):
        return -1
    else:
        return 0

def func2():
    l = list(map(int, input('输入三个整数：').split(',')))
    if l[0] < 0 or l[0] > 9 or l[1] >= l[2]:
        return None
    count = 0
    for i in range(l[1], l[2] + 1):
        if str(l[0]) in str(i):
            count += 1
    return count


def func3():
    l = list(map(int, input('输入正整数列表：').split(',')))
    t = []
    res = []
    temp = ''
    for i in l:
        t.append(int(str(i)[0]))
        t.append(int(str(i)[-1]))
    def isprime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
    for i in t:
        if not isprime(i):
            temp += str(i)
        else:
            if temp:
                res.append(int(temp))
            res.append(i)
            temp = ''
    if temp:
        res.append(int(temp))
    return res


def func4(l):
    """ 矩阵“转置” """
    m = len(l)
    res = []
    r = c = 0
    for i in range(2 * m - 1):
        res.append([])
        if i <= m - 1:
            r = i
        else:
            r = m - 1
        c = i - r
        while r >= 0 and c <= m - 1:
            res[i].append(l[r][c])
            r -= 1
            c += 1
        for _ in range(m - len(res[i])):
            res[i].append(0)
    return res
    

def func5():
    """ 英文单词处理 """
    s = input('输入一个英文单词：')
    ex = False
    res = ''
    if len(s) < 2:
        return None
    for i in s:
        if 'A' <= i <= 'Z':
            ex = True
            break
    if ex:
        res = s.lower()
        res = s.capitalize()
    else:
        temp1 = s[:len(s) - 1].lower()
        temp2 = s[len(s) - 1].upper()
        temp3 = [temp1.capitalize(), temp2]
        res = ''.join(temp3)
    return res


def func6():
    """ 字符串处理 """
    s = input('输入一个字符串：')
    pat = re.compile(r'[A-Za-z0-9]+')
    word1 = pat.findall(s)
    if word1:
        return ''
    word2 = []
    for i in word1:
        temp = ''
        if len(i) > 5:
            temp = i[0] + '*' * (len(i) - 2) + i[-1]
        else:
            temp = i
        word2.append(temp)
    return ' '.join(word2)


def func7():
    """ 单词掌握情况 """
    words = input('输入单词列表，用逗号隔开：').split(',')
    chars = input('输入chars：')
    count = 0
    for i in words:
        judge = True
        for j in i:
            if i.count(j) > chars.count(j):
                judge = False
                break
        if judge:
            count += 1
    return count


def func8(l):
    """ 学号志愿者时长统计 """
    d = {}
    for i in l:
        if (len(i[0]) == 9) and  (i[0].isdigit()) and (1 <= i[1] <= 3):
            d[i[0]] = d.get(i[0], 0) + i[1]
    res = list(d.items())
    res.sort(key = lambda x: x[0])
    res.sort(key = lambda x: x[1], reverse = True)
    return (res[0][0], res[0][1])


if __name__ == '__main__':
    # print(func1())
    # print(func2())
    # print(func3())
    # print(func4([[1,2,3],[4,5,6],[7,8,9]]))
    # print(func5())
    # print(func6())
    # print(func7())
    print(func8([("19274056",3), ("192740A01",2), ("192740101",3)]))