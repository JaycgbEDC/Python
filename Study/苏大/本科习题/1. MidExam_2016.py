import re
import math
import random


def extract_display_prime(s):
    """ 提取s中包含数字3或数字7的所有素数并显示，每个值占10列右对齐，每行显示2个数 """
    pat = re.compile(r'\d+')
    list_str = pat.findall(s)
    list_extract = []
    for i in list_str:  # 提取过程
        if i.count('3') or i.count('7'):
            temp = int(i)
            is_prime = False
            for j in range(2, int(math.sqrt(temp) + 1)):
                if temp % j == 0:
                    is_prime = True
                    break
            if not is_prime:
                list_extract.append(temp)
    for i in range(0, len(list_extract), 2):  # 输出格式
        print('{0:>10d}'.format(list_extract[i]), end = '')
        if i + 1 < len(list_extract):
            print('{0:>10d}'.format(list_extract[i + 1]))
        else:
            print()
    return list_extract


def generate_coordinate(l):
    """ 将l中的数字组成坐标并排序 """
    len_l = len(l)
    coordinate = []
    for i in range(0, len_l, 2):
        if i + 1 < len_l:
            coordinate.append((l[i], l[i + 1]))
    coordinate.sort(key = lambda x: x[0])
    coordinate.sort(key = lambda x: x[1])
    return coordinate


def generate_point_A():
    """ 产生两个[0, 100]之间的随机实数作为点A的坐标，输出坐标值，保留2位小数，占10列右对齐 """
    point_a = (random.uniform(0, 100), random.uniform(0, 100))
    print('({0:>10.2f},{1:>10.2f})'.format(point_a[0], point_a[1]))
    return point_a


def sum_eculidean_distance(point, coordinate):
    """ 计算所有坐标点到A之间的欧氏距离之和 """
    sum = 0
    for i in coordinate:
        sum += math.sqrt((point[0] - i[0])**2 + (point[1] - i[1])**2)
    print('欧氏距离之和为: {0: 10.2f}'.format(sum))
    return sum


def mean_distance(point, coordinate):
    """ 计算所有坐标点到A点之间的平均距离 """
    mean = sum_eculidean_distance(point, coordinate) / len(coordinate)
    print('平均距离为: {0: 10.2f}'.format(mean))


def extract_english_word_cal_ascii(s):
    """ 提取字符串s中的所有单词，并将单词中所有字母的ASCII之和输出，每行显示10个整数，每个整数占8列左对齐 """
    pat = re.compile(r'[a-zA-Z]{2, }')
    word = pat.findall(s)
    sum_ascii = []
    for i in word:
        sum = 0
        for j in i:
            sum += ord(j)
        sum_ascii.append(sum)
    """ for i in range(0, len(sum_ascii), 10):  # 输出部分（较复杂）
        for j in range(0, 10):
            if i + j < len(sum_ascii):
                print('{0:<8d}'.format(sum_ascii[i + j]), end = '')
        print() """
    count = 0
    for i in sum_ascii:  #输出部分（简单）
        count += 1
        print('{0:<8d}'.format(i), end = '')
        if count == 10:
            count = 0
            print()
    

if __name__ == '__main__':
    s = 'Regular296expression913patterns465are280compiled102into510a122series480f563bytecodes16which366are262then773executed361by50a949 \
        matching556engine509written126in451C760For379advanced982use201it502may282be666necessary566t0631pay199carefu1685attention915t081 \
        4how577the455engine309wi11349executeI78a341given171RE279and52write744the69RE578in190a361certain466way726in9690rder667t031Oprodu \
        ce943bytecode760that203runs590faster4230ptimization723is787not458covered30in250this747document66because396it803requires530that6 \
        0lyou928have208a152good609understanding1940f31the772matching17engine599internals806'
    l = extract_display_prime(s)
    point_a = generate_point_A()
    coordinate = generate_coordinate(l)
    mean_distance(point_a, coordinate)
    extract_english_word_cal_ascii(s)