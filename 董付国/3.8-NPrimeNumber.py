# 输出所有由1、2、3、4这四个数字组成的素数，每个素数中每个数字只使用一次
# 原理：判断一个数是否为质数：在一般领域，对正整数 n，如果用 2 到 Math.sqrt(n) 之间的所有整数去除，均无法整除，则 n 为质数

from math import sqrt
l = [2, 3]
for i in range(1, 5):
    for j in range(1, 5):
        if j != i:
            l.append(i*10+j)
for i in range(1, 5):
    for j in range(1, 5):
        if j != i:
            for k in range(1, 5):
                if k != j and k != i:
                    l.append(i*100+j*10+k)
for i in range(1, 5):
    for j in range(1, 5):
        if j != i:
            for k in range(1, 5):
                if k != j and k != i:
                    for m in range(1, 5):
                        if m != k and m != j and m != i:
                            l.append(i*1000+j*100+k*10+m)
print(l)
for i in l:
    for j in range(2, int(sqrt(i)+1)):
        if i % j == 0:
            l.remove(i)
            break
print(l)