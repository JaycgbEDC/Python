# 输入一个列表和2个整数作为下标，然后输出列表中介于2个下标之间的元素组成的子列表。
# eg：输入[1,2,3,4]和2，3，输出[3,4]

a = eval(input('Please input a list, eg:[1,2,3,4]\n'))
index1, index2 = eval(input('Please input two integers, eg:2,3\n'))
print(a[index1:index2+1])
