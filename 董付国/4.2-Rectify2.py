# 有一段英文，其中有单词中间的字母i误写为I，纠正

import re

s = "He lIkes swImmIng."
pattern = re.compile(r'(\w)I(\w)')
index = 0
while True:
    matchres = pattern.search(s, index)
    if matchres:
        s = s[:matchres.start(0)+1] + 'i' + s[matchres.end(0)-1:]
    else:
        break
    index = matchres.end(0) + 1
print(s)