# 生成包含1000个0~100之间的随机整数，并统计每个元素的出现次数

""" 
# 法一
import random
a = [random.randint(0, 100) for i in range(100)]
d = dict()
for num in a:
    d[num] = d.get(num, 0) + 1
print(d, sum(d.values()))
 """
# 法二
import random
from collections import defaultdict
a = [random.randint(0, 100) for i in range(100)]
frequences = defaultdict(int)
for item in a:
    frequences[item] += 1
print(frequences, sum(frequences.values()))