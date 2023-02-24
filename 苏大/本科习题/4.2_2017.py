import random
import math
import os


def productRndNum():
    rnd = random.randint(100, 200)
    res = [random.randint(100, 500) for _ in range(rnd)]
    return res


def getDigNumber(l1, l2):
    res = []
    def judge(n):
        while n != 0:
            temp = n % 10
            if temp in l2:
                return True
            n //= 10
        return False
    for i in l1:
        if judge(i):
            res.append(i)
    return res


def printOut(l, num):
    count = 0
    for i in l:
        count += 1
        print('{0:>5d}'.format(i), end = '')
        if count == num:
            print()
            count = 0


def getDivisorNum(l):
    res = []
    for i in l:
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                res.append(j)
                if j != i / j:
                    res.append(int(i / j))
    return res


def staticResult(l):
    res = {}
    for i in l:
        res[i] = res.get(i, 0) + 1
    return res


def printMax5Out(d):
    l = list(d.items())
    l.sort(key = lambda x: x[1], reverse = True)
    count = 0
    for i in l:
        count += 1
        print('{0}: {1}'.format(i[0], i[1]))
        if count == 5:
            break


def delMultiDivisor(l):
    global resultLst
    res = []
    for i in resultLst:
        if res.count(i) == 0:
            res.append(i)
    resultLst = res


def printDivisorToFile(filename, l):
    os.chdir(r'./苏大/本科习题')
    with open(filename, 'w+') as fp:
        count = 0
        for i in l:
            count += 1
            s = '{0:>5}'.format(i)
            fp.write(s)
            if count == 8:
                count = 0
                fp.write('\n')


if __name__ == "__main__":
    # ----产生随机整数-------
    numberLst = productRndNum()

    # ----找出包含数字 2 或 6 的整数，其中 digLst 包含数字 2 和 6-----
    digLst = [2, 6]
    num26Lst = getDigNumber(numberLst, digLst)
    printOut(num26Lst, 8)

    #-----找出所有整数的因子-----
    resultLst = getDivisorNum(num26Lst)

    #-----统计每个因子出现的次数-----
    resultStatic = staticResult(resultLst)
    printMax5Out(resultStatic)

    # ----删除 resultLst 中重复因子的多余份数，只保留一份-----
    delMultiDivisor(resultLst)
    print("===出现次数最多的数字===")
    printDivisorToFile(r"./Files/3.result.txt", resultLst)