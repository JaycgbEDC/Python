# 设计一个字典，用户输入内容作为键，输出字典中对应的值，如果键不存在，则输出“您输入的键不存在！”

# a = dict()
a = {i:str(i) for i in range(1, 5)}
while 1:
    inp = int(input('请输入键值：\n'))
    print(a.get(inp, '您输入的键不存在！\n'))