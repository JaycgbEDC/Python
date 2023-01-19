# 输入4位整数作为年份，判断是否为闰年

year = int(input('请输入4位整数\n'))
if year% 400 == 0 or (year% 4 == 0 and year% 100 != 0):
    print('闰年')
else:
    print('不是闰年')