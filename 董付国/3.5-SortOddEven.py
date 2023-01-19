# 生成一个包含20个随机整数的列表，对其中偶数下标的元素降序排列，奇数下标的元素不变

import random
l = [random.randint(1, 100) for _ in range(20)]
print('生成的列表：', l)
l[::2] = sorted(l[::2], reverse=True)
print('排序完的列表：', l)