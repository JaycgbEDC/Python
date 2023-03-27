""" 查找一个数列中两个数相乘最大，如果两个pair 都是最大的就是相加起来最大的那个，返回元组，里边的元素先小后大 """


def func1(l):
    if len(l) < 2:
        return []
    x, y = l[0], l[1]
    max = x * y
    for i, num1 in enumerate(l):
        for num2 in l[i + 1:]:
            if num1 * num2 > max:
                max = num1 * num2
                x, y = num1, num2
            elif num1 * num2 == max:
                if num1 + num2 > x * y:
                    max = num1 * num2
                    x, y = num1, num2
    if x > y:
        x, y = y, x
    return (x, y)


if __name__ == "__main__":
    while 1:
        print(func1(int(input())))