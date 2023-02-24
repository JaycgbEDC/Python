# 编写函数实现十进制整数转十六进制；十六进制转二进制


def decimal_bin(n):
    """ 十进制整数转二进制 """
    res = ''
    temp = int(n)
    while temp != 0:  # 除留取余法
        rem = temp % 2
        temp //= 2
        res = str(rem) + res
    return '0b' + res


def decimal_hex(n):
    """ 十进制整数转十六进制 """
    res = ''
    temp = int(n)
    while temp != 0:
        rem = temp % 16
        temp //= 16
        if rem >= 10:
            rem = chr(ord('a') + rem - 10)
        res = str(rem) + res
    return '0x' + res


def hex_decimal(n):
    """ 十六进制转二进制 """
    l = list(n)
    count = 0
    res = 0
    for i in l[::-1]:
        if 'a' <= i <= 'f':
            num = ord(i) - ord('a') + 10
        else:
            num = int(i)
        res += 16**(count) * num
        count += 1
    return decimal_bin(str(res))


def test():
    print('my：十进制222转十六进制为：{0}'.format(decimal_hex('222')))
    print('my：十六进制abcf9999转二进制为：{0}'.format(hex_decimal('abcf9999')))
    print('十进制222转十六进制为：{0}'.format(hex(222)))
    print('十六进制abcf9999转二进制为：{0}'.format(bin(int('abcf9999', 16))))


if __name__ == '__main__':
    test()