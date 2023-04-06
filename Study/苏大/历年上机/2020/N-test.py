"""
2020年Python复试上机编程题（仅一道，20分钟完成）：
编写函数check(L) 验证整数列表L中是否存在5个数，可以构成一个公差为1的等差数列。

具体说明：
    1. 列表L中的元素一定是整数，函数中无需验证L中元素的类型
    2. 列表L的长度不小于5，函数中无需考虑L的长度不足5的情况
    3. 如果列表L中有符合要求的等差数列，函数返回True 否则返回False

编写程序测试check代码的正确性，提交的源代码可以包括测试代码，也可以不包括

评分说明
    1. 评分只考察 check函数的内容
    2. 函数有语法错误或运行发生异常均不得分
"""


def check(L):
    """ 测试用例要考虑清楚 """
    L = list(set(sorted(L)))
    # for i in range(0, len(L) - 4):
    #     if L[i] == L[i + 1] - 1 and L[i + 1] == L[i + 2] - 1 and L[i + 2] == L[i + 3] - 1 and L[i + 3] == L[i + 4] - 1:
    #         return True
    #         break
    # return False
    for i in range(len(L) - 4):
        count = 0
        for j in range(1, 5):
            if L[i + j] - L[i + j - 1] == 1:
                count += 1
            else:
                break
        if count == 4:
            return True
    return False


if __name__ == "__main__":
    print(check([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))