# 生成一个包含50个随机整数的列表，然后删除其中所有奇数（从后往前删）

import random
l = [random.randint(1,100) for _ in range(50)]
print('生成的列表为：', l)
for i in l[::-1]:
    if i % 2 != 0:
        l.remove(i)
print('删除后的列表：', l)