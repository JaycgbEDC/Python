# 读取一个英文文本文件的内容，并将其中的大写字母变为小写字母，小写字母变大写字母

with open(r'./董付国/English.txt', 'r+') as fp:
    lines = fp.readlines()
    #fp.truncate(0)
    for i, line in enumerate(lines):
        lines[i] = line.swapcase()
    fp.seek(0)
    fp.writelines(lines)