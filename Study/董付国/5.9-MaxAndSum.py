# 编写函数，可以接收任意多个整数并输出其中的最大值和所有整数之和


def MaxAndSum(*p):
    print("最大值：", max(p), "所有整数之和：", sum(p))


MaxAndSum(1,2,3,4,5)