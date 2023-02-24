# 统计一个英文文本词频，按词频和字典顺序排序（词频是主关键字，字典顺序是次关键字）


import re


d = dict()
with open('test.txt', 'r') as fp:
    l1 = fp.readlines()
    for line in l1:
        line_up = line.upper()
        for i in line_up:
            if 'A' <= i <= 'Z':
                d[i] = d.get(i, 0) + 1
l = d.items()
res1 = sorted(l, key = lambda x: x[0])
res = sorted(res1, key = lambda x: x[1])
print(res)