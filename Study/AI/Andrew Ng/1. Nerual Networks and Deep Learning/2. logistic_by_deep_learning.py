import numpy as np
import matplotlib.pyplot as plt
import h5py  # 处理存储为H5文件格式的数据集
import scipy
from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset


train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
def test():
    """ draw the picture in train_datasets """
    index = 5
    plt.imshow(train_set_x_orig[index])
    print ("y = " + str(train_set_y[:, index]) + ", it's a '" + classes[np.squeeze(train_set_y[:, index])].decode("utf-8") +  "' picture.")
    plt.show()

    """ find something """
    m_train = train_set_x_orig.shape[0]  # 训练集示例数量
    m_test = test_set_x_orig.shape[0]  # 测试集示例数量
    num_px = train_set_x_orig.shape[1]  # 训练图像的高度=训练图像的宽度
    print(m_train, m_test, num_px, train_set_x_orig.shape, train_set_y.shape, test_set_x_orig.shape, test_set_y.shape)


def pretreatment():
    """ reshape the size"""
    train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
    test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T
    train_set_x = train_set_x_flatten / 255
    test_set_x = test_set_x_flatten / 255
    return train_set_x, test_set_x


def sigmoid(z):
    """ Compute the sigmoid of z
    param: z: A scalar or numpy array of any size.
    return: sigmoid(z) 
    """
    return 1 / (1 + np.exp(-z))


def initialize_with_zeros(dim):
    """ This function creates a vector of zeros of shape (dim, 1) for w and initializes b to 0 
    param: dim: size of the w vector we want
    returns:
    w: initialized vector of shape (dim, 1)
    b: initialized scalar (corresponds to the bias)
    """
    w = np.zeros((dim, 1))
    b = 0
    assert w.shape == (dim, 1), "the size of w error!"
    assert isinstance(b, float) or isinstance(b, int), "the type of b error!"
    return w, b


def propagate(w, b, X, Y):
    """ Implement the cost function and its gradient for the propagation 
    params:
    w: weights, a numpy array of size (num_px * num_px * 3, 1)
    b: bias, a scalar
    X: data of size (num_px * num_px * 3, number of examples)
    Y: true "label" vector (containing 0 if non-cat, 1 if cat) of size (1, number of examples)
    returns:
    cost: negative log-likelihood cost for logistic regression
    dw: gradient of the loss with respect to w, thus same shape as w
    db: gradient of the loss with respect to b, thus same shape as b
    """
    m = X.shape[1]
    # forward propagation
    Z = np.dot(w.T, X) + b
    A = sigmoid(Z)
    cost = -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))

    # backward propagation
    dw = 1 / m * np.dot(X, (A - Y).T)
    db = 1 / m * np.sum(A - Y)

    assert dw.shape == w.shape, "the size of dw error!"
    assert db.dtype == float, "the type of db not float!"

    grads = {"dw": dw, "db": db}
    return grads, cost


def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost = False):
    """ This function optimizes w and b by running a gradient descent algorithm 
    params:
    w: weights, a numpy array of size (num_px * num_px * 3, 1)
    b: bias, a scalar
    X: data of shape (num_px * num_px * 3, number of examples)
    Y: true "label" vector (containing 0 if non-cat, 1 if cat), of shape (1, number of examples)
    num_iterations: number of iterations of the optimization loop
    learning_rate: learning rate of the gradient descent update rule
    print_cost: rue to print the loss every 100 steps
    returns:
    params: dictionary containing the weights w and bias b
    grads: dictionary containing the gradients of the weights and bias with respect to the cost function
    costs: list of all the costs computed during the optimization, this will be used to plot the learning curve
    """
    costs = []
    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)
        dw, db = grads["dw"], grads["db"]
        w = w - learning_rate * dw
        b = b - learning_rate * db
        if i % 100 == 0:
            costs.append(cost)
        if print_cost and i % 100 == 0:
            print(f"Cost after iteration {i}: {cost}")
    params = {"w": w, "b": b}
    grads = {"dw": dw, "db": db}
    return params, grads, costs 


def predict(w, b, X):
    """ Predict whether the label is 0 or 1 using learned logistic regression parameters (w, b) 
    params:
    w: weights, a numpy array of size (num_px * num_px * 3, 1)
    b: bias, a scalar
    X: data of size (num_px * num_px * 3, number of examples)
    returns:
    Y_prediction: a numpy array (vector) containing all predictions (0/1) for the examples in X
    """
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    Z = np.dot(w.T, X) + b
    A = sigmoid(Z)
    for i in range(A.shape[1]):
        if A[0, i] <= 0.5:
            Y_prediction[0, i] = 0
        else:
            Y_prediction[0, i] = 1
    
    assert Y_prediction.shape == (1, m), "the size of Y_predition error!"
    return Y_prediction


def model(X_train, Y_train, X_test, Y_test, num_iterations = 2000, learning_rate = 0.5, print_cost = False):
    """ Builds the logistic regression model 
    params:
    X_train: training set represented by a numpy array of shape (num_px * num_px * 3, m_train)
    Y_train: training labels represented by a numpy array (vector) of shape (1, m_train)
    X_test: test set represented by a numpy array of shape (num_px * num_px * 3, m_test)
    Y_test: test labels represented by a numpy array (vector) of shape (1, m_test)
    num_iterations: hyperparameter representing the number of iterations to optimize the parameters
    learning_rate: hyperparameter representing the learning rate used in the update rule of optimize()
    print_cost: Set to true to print the cost every 100 iterations
    returns:
    d: dictionary containing information about the model
    """
    w, b = initialize_with_zeros(X_train.shape[0])
    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)
    w, b = parameters["w"], parameters["b"]
    Y_prediction_train = predict(w, b, X_train)
    Y_prediction_test = predict(w, b, X_test)

    print(f"train accuracy: {100 - np.mean(np.abs(Y_prediction_train - Y_train) * 100)} %")
    print(f"test accuracy: {100 - np.mean(np.abs(Y_prediction_test - Y_test) * 100)} %")

    d = {
        "costs": costs,
        "Y_prediction_test": Y_prediction_test, 
        "Y_prediction_train" : Y_prediction_train, 
        "w" : w, 
        "b" : b,
        "learning_rate" : learning_rate,
        "num_iterations": num_iterations
    }
    return d


def draw_image(models, learning_rates):
    """ draw the picture of loss function """
    for i in learning_rates:
        plt.plot(np.squeeze(models[str(i)]["costs"]), label = str(models[str(i)]["learning_rate"]))
    plt.xlabel("iterations (per hundreds)")
    plt.ylabel("cost")
    legend = plt.legend(loc='upper center', shadow=True)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')
    plt.show()


if __name__ == "__main__":
    # test()
    train_set_x, test_set_x = pretreatment()
    learning_rates = [0.01, 0.001, 0.0001]
    models = {}
    for i in learning_rates:
        print("learning rate is: " + str(i))
        models[str(i)] = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations = 1500, learning_rate = i, print_cost = False)
        print('\n' + "-------------------------------------------------------" + '\n')
    draw_image(models, learning_rates)