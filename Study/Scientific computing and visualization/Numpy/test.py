import numpy as np


# 生成数组
# a = np.array((1,2,3))  # 不是行/列向量(a.shape值为(3,))，秩为1，可用a.reshape(3,1)转换为列向量
# b = np.array(([1,2], [3,4]))  # 2*2的矩阵
# x = np.linspace(0, 5, 11)
# print(a, b, x)
# print(a.shape, b.shape, x.shape)

a  = np.arange(10).reshape(1,10)
b = np.squeeze(a)  # 从数组的形状中删除单维度条目，即把shape中为1的维度去掉