# 一段英文有单词连续重复了2次，检查重复的单词并只保留一个。

import re

s = "This is is a desk."
pattern = re.compile(r'(?P<f>\b\w+\b)\s(?P=f)')
index = 0
while True:
    matchres = pattern.search(s, index)
    if matchres:
        s = s.replace(matchres.group(0), matchres.group(1))
    else:
        break
    index = matchres.end(0)
print(s)