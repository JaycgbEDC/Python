# 将当前工作目录修改为“C:\”，并验证，最后将当前工作目录恢复为原来的目录

import os
curdir = os.getcwd()
os.chdir('C:\\')
print(os.getcwd())
verf = input('当前目录是否为C:\，输入Y/N：')
if verf == 'Y':
    os.chdir(curdir)