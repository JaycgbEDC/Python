# 编写函数，接受一个字符串，分别统计大写字母、小写字母、数字、其他字符的个数，并以元组的形式返回结果


def CountNum(s):
    upc = loc = dig = oth = 0
    for i in s:
        if i.isupper():
            upc += 1
        elif i.islower():
            loc += 1
        elif i.isdigit():
            dig += 1
        else:
            oth += 1
    return (upc, loc, dig, oth)


print(CountNum('WoAiNi1314_&*'))