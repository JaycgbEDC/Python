# 输入小于1000的整数，对其进行因式分解

x = int(input('请输入一个小于1000的整数'))
y = x
res = []
i = 2
while 1:
    if x % i == 0:
        res.append(str(i))
        x /= i
    else:
        i += 1
    if x == 1:
        break
print("%d = " %y, end='')
print('*'.join(res))
