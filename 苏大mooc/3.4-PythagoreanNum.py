# 用穷举法找出1-100之间的勾股数，要求不重复、每一行输出5组勾股数、程序效率高


from math import sqrt

count = 0
for i in range(2, 101):
    for j in range(i + 1, 101):
        k = int(sqrt(i**2 + j**2))
        if (i**2 + j**2 == k**2) and (k in range(1, 101)):
            count += 1
            print((i, j, k), end='\t')
            if count == 5:
                count = 0
                print('')