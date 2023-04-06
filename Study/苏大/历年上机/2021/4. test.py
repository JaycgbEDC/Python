""" 数组包含很多集合，集合都是一些数字， 然后返回集合(集合中是数字)  数字出现频率大于[数组长度/2] [{1,2},{1,2,3}] """


def func1(l):
    res = set()
    d = {}
    s = len(l) // 2
    for i in l:
        for j in i:
            d[j] = d.get(j, 0) + 1
    for k, v in d.items():
        if v > s:
            res.add(k)
    return res