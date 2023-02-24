# 计算距离某日期x天是什么日期，x可正可负


import datetime


def Solution1(y, m, d, count):
    if count >= 0:
        while count:
            month = JudgeLeap(y)
            if d + count > month[m]:
                count -= month[m - 1] - d
                d = 0
                m += 1
                if m > 12:
                    y += 1
                    m = 1
            else:
                d += count
                break
    else:
        while count:
            month = JudgeLeap(y)
            if d + count <= 0:
                count += d
                d = month[m - 2]
                m -= 1
                if m == 0:
                    y -= 1
                    m = 12
            else:
                d += count
                break
    return "-".join(map(str, (y, m, d)))


def Solution2(y, m, d, count):
    cur = datetime.date(y, m, d)
    res = cur + datetime.timedelta(days=count)
    return res


def JudgeLeap(year):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # 闰年
        month[1] = 29
    return month


x = map(int, input('输入日期和距离天数并用逗号隔开：').split(','))
print(Solution1(*x))