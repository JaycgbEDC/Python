# 题：有一段英文，其中有单独的字母I误写为i，纠正
# 分析：英文i习惯--单独出现要大写。i前后都不是字母。

import re

s = "i am a teacher,i am man, so do i, and kyrie irving is my idol, so do i"
pattern = re.compile(r'([^\w]|\b)i([^\w]|\b)')
index = 0
while True:
    matchres = pattern.search(s, index)
    if matchres:
        if matchres.start(1) == 0: # 1表示第一个子模式，以I开头
            s = 'I' + s[1:]
        elif matchres.end(2) == len(s): # 以I结尾
            s = s[:matchres.start(1)+1] + 'I'
        else:
            s = s[:matchres.start(1)+1] + 'I' + s[matchres.end(2)-1:]
    else:
        break
    index = matchres.end(2) + 1
print(s)

""" 法二：不使用正则表达式
s = s.replace('i ', 'I ')
s = s.replace(' i ', ' I ')
s = s.replace(' i', ' I')
print(s) 
"""