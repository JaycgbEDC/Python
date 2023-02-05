# 将包含学生成绩的字典保存为二进制文件，然后读取内容并显示

import pickle
grade = {'张三':100, '李四':90, '王五':50}
fp = open('./董付国/Data.txt', 'wb+')
pickle.dump(grade, fp)
fp.seek(0)
x = pickle.load(fp)
print(x)