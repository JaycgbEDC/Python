# 2h-11m
import re
import os


def get_record(s):
    os.chdir(r'D:\Github\PostG\Python\苏大\本科习题')
    with open(s, 'r') as fp:
        return fp.readlines()


def get_v(l):
    res = set()
    pat = re.compile(r'[A-Z]{2}-\d{3}-\d{3}')
    for i in l:
        res.add(pat.findall(i)[0])
    return res


def count_v(l, v_set):
    res = dict.fromkeys(v_set, 0)
    pat = re.compile(r'[A-Z]{2}-\d{3}-\d{3}')
    for i in l:
        temp = pat.findall(i)
        res[temp[0]] += 1
    return res


def count_t(l, v_set):
    res = dict.fromkeys(v_set, 0)
    pat1 = re.compile(r'\d{2}:\d{2}:\d{2}')
    pat2 = re.compile(r'[A-Z]{2}-\d{3}-\d{3}')
    for i in l:
        t = pat1.findall(i)
        v_t = cal_t(t)
        temp = pat2.findall(i)
        res[temp[0]] += v_t
    return res


def cal_t(l):
    """ 计算时间差，输入值为列表，类型字符串 """
    sec = []
    for i in l:
        temp = i.split(':')
        sec.append(int(temp[0]) * 3600 + int(temp[1]) * 60 + int(temp[2]))
    return (sec[1] - sec[0])


def write_to_file(l, f_d, i_d, s):
    count = 0
    with open(s, 'w+') as fp:
        max_etc = len(l)
        num_v = len(get_v(l))
        f_l = list(f_d.items())  # items方法返回的是dict_items对象，不是列表
        f_l.sort(key = lambda x: x[1], reverse = True)
        i_l = list(i_d.items())
        i_l.sort(key = lambda x: x[1], reverse = True)
        fp.write('记录条数：{0}\n'.format(max_etc))
        fp.write('车辆数：{0}\n'.format(num_v))
        fp.write('进校次数最多的5辆车（单位：次）：\n')
        for i in f_l:
            count += 1
            if count <= 5:
                fp.write('{0}，{1}\n'.format(i[0], i[1]))
            else:
                count = 0
                break
        fp.write('累计停留时间最长的5辆车（单位：秒）\n')
        for i in i_l:
            count += 1
            if count <= 5:
                fp.write('{0}，{1}\n'.format(i[0], i[1]))

def main():
    vehicle_lst = get_record("./Files/1.data.txt")  # 读文件，获取全部ETC记录，构成列表
    vehicle_set = get_v(vehicle_lst)  # 获取全部不同的ETC编号，构成集合
    fre_dict = count_v(vehicle_lst, vehicle_set)  # 构造车辆进出校园次数的字典
    inter_dict = count_t(vehicle_lst, vehicle_set)  # 构造车辆累计停留时间的字典
    write_to_file(vehicle_lst, fre_dict, inter_dict, "./Files/1.report.txt")
    return


main()