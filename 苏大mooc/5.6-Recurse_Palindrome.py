def judge_palin(s):
    """ 判断s是否为回文 """
    if s == '' or len(s) == 1:
        return True
    if s[0] != s[len(s) - 1]:
        return False
    return judge_palin(s[1:-1])


def test():
    s = input('请输入要判断的字符串: ')
    if judge_palin(s):
        print('是回文')
    else:
        print('不是回文')


if __name__ == '__main__':
    test()