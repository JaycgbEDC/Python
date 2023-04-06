# 输入一个目录和一个文件名，搜索该目录及其子目录中是否存在该文件

import os


def find_File(dir, filename):
    if not os.path.isdir(dir):
        print('Error')
        return
    for i in os.listdir(dir):
        sub_path = os.path.join(dir, i)
        if i == filename:
            print('Find')
            return
        if os.path.isdir(sub_path):
            find_File(sub_path, filename)


search = input('输入一个目录和一个文件名，用空格分隔：')
file = search.split()
find_File(*file)