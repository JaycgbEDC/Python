# 用二分查找计算n的平方根


def Binary_Search_Sqrt(n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) / 2
        if abs(mid**2 - n) < 1e-6:
            return mid
        elif mid**2 < n:
            low = mid
        else:
            high = mid


n = int(input('输入n：'))
res = Binary_Search_Sqrt(n)
print('{0}的平方根为：{1}'.format(n, res))