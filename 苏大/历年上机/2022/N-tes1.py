'''
给定字符串s，找到满足条件的子串，条件是：子串中包含且仅包含的k个不同字符
返回子串列表，以长度升序，长度相同时以字典顺序
ex: s='aadbac',k=2
return: ['ac', 'ad', 'ba', 'db', 'aad']
:param s: 给定字符串
:param k: 子串中有且仅有的k个不同字符
:return: 排序后的字串列表
'''


def func1(s, k):
    res = []
    for i in range(len(s)):
        count = 0
        temp = ''
        for ch2 in s[i:]:
            if ch2 not in temp:
                count += 1
            temp += ch2
            if count == k:
                res.append(temp)
            if count > k:
                break
    res.sort(key = lambda x: (len(x), x))
    return res


if __name__ == "__main__":
    print(func1('aadbac', 2))