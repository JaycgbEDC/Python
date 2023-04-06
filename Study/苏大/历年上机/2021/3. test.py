""" 查找某一个数后面离它最近的比他大的数，如果没有就是none
[1,3,5]   [3,5,none]
[7,3,5]    [none,5,none] """


def func1(l):
    res = []
    for i, num1 in enumerate(l):
        for num2 in l[i + 1:]:
            if num2 > num1:
                res.append(num2)
                break
        if len(res) != i + 1:
            res.append(None)
    return res


if __name__ == "__main__":
    print(func1([7,3,5]))