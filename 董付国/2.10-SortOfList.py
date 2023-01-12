# 生成包含20个随机数的列表，将前10个元素升序排列，后10个元素降序排列，并输出结果

import random
a = [random.randint(1,100) for _ in range(20)]
x1 = a[:10]
x2 = a[:9:-1]
x1.sort()
x2.sort(reverse=True)
a[:10] = x1
a[10:] = x2
print(a)