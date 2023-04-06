# 2h-10m
import os
import re


def readWordsFromFile(filename):
    os.chdir(r'./苏大/本科习题')
    res = []
    with open(filename, 'r') as fp:
        temp = fp.readlines()
        pat = re.compile(r'[a-zA-Z]+')
        for i in temp:
            res += pat.findall(i)
    return res


def findMultiAlphaWords(l, num):
    res = []
    for i in l:
        temp = i.lower()
        for j in temp:
            if temp.count(j) >= num:
                res.append(i)
                break
    return res


def delMultiData(l):
    global wordResultLst
    res = []
    for i in wordResultLst:
        if res.count(i) == 0:
            res.append(i)
    wordResultLst = res


def printWordLst(l, count):
    temp = 0
    for i in l:
        temp += 1
        print('{0:20s}'.format(i), end = '')
        if temp == count or l.index(i) == (len(l) - 1):
            print()
            temp = 0


def getNumberOfWords(l):
    res = []
    for i in l:
        sum = 0
        for j in i:
            sum += ord(j)
        res.append(sum)
    return res


def sortByDigitalSum(l):
    global numlst
    def cal_sum(x):
        sum = 0
        for i in str(x):
            sum += int(i)
        return sum
    numlst.sort(key = lambda x: cal_sum(x), reverse = True)


def printNumLst(l, count):
    temp = 0
    for i in l:
        temp += 1
        print('{0:8d}'.format(i), end = '')
        if temp == count or l.index(i) == (len(l) - 1):
            print()
            temp = 0


def staticDigitalTimes(l):
    res = {}
    for i in l:
        for j in str(i):
            res[j] = res.get(j, 0) + 1    
    return res


def printDicToFile(filename, d):
    temp = list(d.items())
    temp.sort(key = lambda x: x[1], reverse = True)
    with open(filename, 'w+') as fp:
        s = '{0:<2s}: {1:>3d}'.format(temp[0][0], temp[0][1])
        print(s)
        fp.write(s)


if __name__ == "__main__":
    # ----从data.txt文件中读取所有单词-------
    wordlst = readWordsFromFile(r".\Files\2.data.txt")
    print("文件中单词个数:", len(wordlst))  # 输出单词个数

    # ----找出单词中，存在某个字母重复num次的单词-----
    wordResultLst = findMultiAlphaWords(wordlst, 2)
    print("至少含有重复2次的字母的单词：", len(wordResultLst))

    # ----删除wordResultLst中重复单词的多余份数，只保留一份-----
    delMultiData(wordResultLst)
    print("===删除重复单词的多余单词后的结果===")
    printWordLst(wordResultLst, 4)  # 输出所有单词，每行输出4个单词

    # ----将wordResultLst中的所有单词转换为整数------
    numlst = getNumberOfWords(wordResultLst)

    # ----对numlst中的所有整数进行根据数字累加和进行降序排序----
    sortByDigitalSum(numlst)
    print("===整数降序排序的结果===")
    printNumLst(numlst, 5)  # 输出整数列表，每行输出5个整数

    # ----统计数字出现的次数----------
    resultDic = staticDigitalTimes(numlst)
    print("===出现次数最多的数字===")
    printDicToFile(r".\Files\2.result1.txt", resultDic)