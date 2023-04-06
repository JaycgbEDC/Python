# 输入一段英文，输出这段英文中所有长度为3个字母的单词

import re
s = input("请输入一段英文：")
res = []
pattern = re.compile(r'(\b\w{3}\b)')
index = 0
while True:
    matchres = pattern.search(s, index)
    if matchres:
        res.append(matchres.group(0))
    else:
        break
    index = matchres.end(0)
print(res)