"""
2016
要求：
文本文件 input.txt 由若干英文单词和分隔符(空格，回车，换行)构成. 根据如下说明编写程序统计不同单词出现
的次数(频度). 将统计结果按出现频度从高到低排序，并将出现频度大于 5 的单词及其频度输出到文件 output.txt
中. 文件格式如下所示：
WinEdt, 31
1. 多个连续的分隔符被视为一个分隔符
2. 单词大小写敏感
3. 每个单词的长度不超过20个字符
4. 单词的数量未知
"""


import re
import os


def func(fileName):
    os.chdir("苏大\\历年上机\\2016\\")
    with open(fileName, 'r') as fp:
        res = {}
        word = []
        l = fp.readlines()
        pattern = re.compile(r'\b[a-zA-Z]{1,}\b')
        for s in l:
            word.extend(pattern.findall(s))
        print(word)
        for w in word:
            res[w] = res.get(w, 0) + 1
        temp = sorted(res, key = lambda x: res[x])
        print(temp)
        with open('output.txt', 'w') as f:
            for i in range(5):
                f.write(temp[i] + ', ' + str(res[temp[i]]) + '\n')
            f.write('黎萧')


func("input.txt")