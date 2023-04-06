# 两种方法计算100以内所有奇数的和

""" 法一：
l  = [i for i in range(1,100)]
sum = 0
for i in l:
    if i % 2 != 0:
        sum += i
print(sum)
"""

# 法二：
l = [i for i in range(1,100) if i %2 != 0]
print(sum(l))