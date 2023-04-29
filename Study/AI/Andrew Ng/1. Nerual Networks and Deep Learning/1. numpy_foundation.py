# 因为函数的输入是实数，所以我们很少在深度学习中使用“math”库。 而深度学习中主要使用的是矩阵和向量，因此numpy更为实用。
import math
import numpy as np


def sigmoid_math(x):
    """ 使用math.exp编写的sigmoid函数 """
    return 1/(1 + math.exp(-x))


def sigmoid_numpy(x):
    """ 使用numpy.exp编写的sigmoid函数 """
    return 1/(1 + np.exp(-x))


def sigmoid_derivative(x):
    """ 求sigmoid对x的导数 """
    s = sigmoid_numpy(x)
    return s * (1 - s)


def image2vector(image):
    """ 将图片向量化 
    param: image: a numpy array of shape (length, height, depth)
    return: a vector of shape (length*height*depth, 1)
    """
    return image.reshape(image.shape[0] * image.shape[1] * image.shape[2], 1)


def normalize_rows(x):
    """ 标准化矩阵的行 
    params: x: A numpy matrix of shape (n, m)
    return: x: The normalized (by row) numpy matrix
    """
    x_norm = np.linalg.norm(x, axis = 1, keepdims = True)
    x =  x / x_norm
    return x


def softmax(x):
    """ Calculates the softmax for each row of the input x 
    params: x: A numpy matrix of shape (n,m)
    return: s -- A numpy matrix equal to the softmax of x, of shape (n,m)
    """
    x_exp = np.exp(x)
    s = x_exp / np.sum(x_exp, axis = 1, keepdims = True)
    return s


def L1(y_hat, y):
    """ L1损失函数 
    params: y_hat: vector of size m (predicted labels)
    params: y: vector of size m (true labels)
    return: loss -- the value of the L1 loss function defined above
    """
    loss = np.sum(np.abs(y_hat - y))
    return loss


def L2(y_hat, y):
    """ L2损失函数 """
    loss = np.dot(y - y_hat, y - y_hat)
    return loss


if __name__ == "__main__":
    # print(sigmoid_math(3))
    # print(sigmoid_numpy(np.array([1, 2, 3])))
    # print(sigmoid_derivative(np.array([1, 2, 3])))
    # print(image2vector(np.array([[[ 0.67826139,  0.29380381],
    #     [ 0.90714982,  0.52835647],
    #     [ 0.4215251 ,  0.45017551]],

    #    [[ 0.92814219,  0.96677647],
    #     [ 0.85304703,  0.52351845],
    #     [ 0.19981397,  0.27417313]],

    #    [[ 0.60659855,  0.00533165],
    #     [ 0.10820313,  0.49978937],
    #     [ 0.34144279,  0.94630077]]])))
    # print(normalize_rows(np.array([
    # [0, 3, 4],
    # [1, 6, 4]])))
    # print(softmax(np.array([
    # [9, 2, 5, 0, 0],
    # [7, 5, 0, 0 ,0]])))
    # print(L1(np.array([.9, 0.2, 0.1, .4, .9]), np.array([1, 0, 0, 1, 1])))
    print(L2(np.array([.9, 0.2, 0.1, .4, .9]), np.array([1, 0, 0, 1, 1])))