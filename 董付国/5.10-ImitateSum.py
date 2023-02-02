# 编写函数，模拟内置函数sum()


def ImitateSum(n):
    if isinstance(n, list) or isinstance(n, tuple) or isinstance(n, set):
        res = 0
        for i in n:
            res += i
        return res


print(ImitateSum({1,2,3}))