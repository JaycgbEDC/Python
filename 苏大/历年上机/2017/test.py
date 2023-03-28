"""
2017
要求：
已知：二进制数据文件 data.bin 中存放了若干个整数，请编写程序完成如下功能：
1、编写程序读取所有数据.

2、以每相邻两个整数为一对按顺序构成二维平面上的坐标点. 例如：有数据 12 ， 34 ， 53 ， 25 ， 61 ，
28 ， 78 等，则构成六个坐标点如下： (12, 34) 、 (34, 53) ， (53, 25) ,  (25, 61) ,  (61, 28) ,  (28,
78) ；

3、以每个坐标点为圆心，以该点与其后面第一个点的欧氏距离为半径 r . 计算每个圆包含的坐标点数. 计算最后
一个点时以其和第一个点的欧氏距离为半径.
例如：
坐标点 (12, 34) 的圆半径$r=\sqrt{(12-34)^2+(34-53)^2}$是坐标点 (12, 34) 与 (34, 53) 的欧式距离.
坐标点 (28, 78) 的圆半径$r=\sqrt{(28-12)^2+(78-34)^2}$是坐标点 (28, 78) 与 (12, 34) 的欧式距离.
坐标点 包含点数 点密度
(x坐标，y坐标) (占5列，右对齐) (占7列，右对齐，保留2位小数)

4、计算所有圆的点密度值，然后输出点密度值最大的 5 个坐标点以及相应圆中包含的点数和点密度值. 输出格式

要求：
上述文字部分不需要显示.
其中：圆的点密度为圆包含的点数除以圆面积，如果点在圆上，则也算圆包含该点，在计算点密度时，圆心也算一
个点. 计算圆面积时$\pi=3.14$. 例如：坐标点 (2, 1) ，则该坐标点也属该坐标点的圆内的一个点.

"""


import os
import struct
import math


def read_file(filename):
    os.chdir(r'./苏大./历年上机./2017')
    res = []
    with open(filename, 'r') as fp:
        # size = struct.calcsize('i')
        # temp = fp.read(size)
        # while temp:
        #     res.append(struct.unpack('i', temp)[0])
        #     temp = fp.read(size)
        return list(map(int, fp.read().split(',')))
        # return res
    

def coordinate(data):
    res = []
    for i in range(len(data) - 1):
        res.append((data[i], data[i + 1]))
    return res

def point(data, r, centl):
    num = 0
    for i in data:
        if r >= math.sqrt((i[0] - centl[0])**2 + (i[1] - centl[1])**2):
            num += 1
    return num


def cal(data):
    # 注意这里的取余技巧
    res = []
    for i in range(len(data)):
        r = math.sqrt((data[i][0] - data[(i + 1) % len(data)][0])**2 + (data[i][1] - data[(i + 1) % len(data)][1])**2)
        num = point(data, r, data[i])
        area = 3.14 * r * r
        res.append((data[i], num, num/area))
    return res


def print_res(res):
    res.sort(key = lambda x: x[2], reverse = True)
    for i in range(5):
        print('{0}{1:>5d}{2:>7.2f}'.format(res[i][0], res[i][1], res[i][2]))
    

if __name__ == "__main__":
    data = read_file(r'./data.bin')
    coord = coordinate(data)
    res = cal(coord)
    print_res(res)