""" 判断ABCD四队谁赢得比赛：
以下只有一句真话：
    1. A队长说：不是我们队也不是C队
    2. B队长说：是我们队或者D
    3. C队长说：是A队不是B队
    4. D队长说：B队长说错了
 """


candidates = "ABCD"
for i in candidates:
    counts = 0
    if i != 'A' and i != 'C':
        counts += 1
    if i == 'B' or i == 'D':
        counts += 1
    if i == 'A':
        counts += 1
    if i != 'B' and i != 'D':
        counts += 1
    if counts == 1:
        print('{0}赢得了比赛'.format(i))
        break