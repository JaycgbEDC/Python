'''
一个至少包含三个元素的整形列表L，若i<j<k,L[i]>L[j]>L[k]是一组逆序对
返回列表逆序对的个数
:param L: [1,8,5,3,4,1]
:return: 7
'''


def func(L):
    count = 0
    for i in range(len(L) - 2):
        for j in range(i + 1, len(L) - 1):
            if L[i] > L[j]:
                for k in range(j + 1, len(L)):
                    if L[j] > L[k]:
                        count += 1
    return count


print(func([1,8,5,3,4,1]))