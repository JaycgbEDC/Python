import numpy as np
import matplotlib.pyplot as plt
import sklearn
from testCases import *
from planar_utils import plot_decision_boundary, sigmoid, load_extra_datasets, load_planar_dataset


X, Y = load_planar_dataset()


def layer_sizes(X, Y):
    """ 
    params: 
    X: input dataset of shape (input size, number of examples)
    Y: labels of shape (output size, number of examples)
    returns:
    n_x: the size of the input layer
    n_h: the size of the hidden layer
    n_y: the size of the output layer
    """
    n_x = X.shape[0]
    n_h = 4
    n_y = Y.shape[0]
    return n_x, n_h, n_y


def initialize_parameters(n_x, n_h, n_y):
    """  
    params:
    n_x: size of the input layer
    n_h: size of the hidden layer
    n_y: size of the output layer
    returns:
    params: python dictionary containing your parameters:
                    W1 -- weight matrix of shape (n_h, n_x)
                    b1 -- bias vector of shape (n_h, 1)
                    W2 -- weight matrix of shape (n_y, n_h)
                    b2 -- bias vector of shape (n_y, 1)
    """
    np.random.seed(2)  # we set up a seed so that your output matches ours although the initialization is random.
    W1 = np.random.randn(n_h, n_x) * 0.01
    b1 = np.zeros((n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.01
    b2 = np.zeros((n_y, 1))
    parameters = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}
    return parameters


def forward_propagation(X, parameters):
    """  
    params:
    X: input data of size (n_x, m)
    parameters: python dictionary containing your parameters (output of initialization function)
    returns:
    A2: The sigmoid output of the second activation
    cache: a dictionary containing "Z1", "A1", "Z2" and "A2"
    """
    Z1 = np.dot(parameters['W1'], X) + parameters['b1']
    A1 = np.tanh(Z1)
    Z2 = np.dot(parameters['W2'], A1) + parameters['b2']
    A2 = sigmoid(Z2)

    assert A2.shape == (1, X.shape[1]), "the size of A2 error!"
    cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
    return A2, cache


def compute_cost(A2, Y, parameters):
    """  Computes the cross-entropy cost
    params:
    A2: The sigmoid output of the second activation, of shape (1, number of examples)
    Y: "true" labels vector of shape (1, number of examples)
    returns:
    cost -- cross-entropy cost
    """
    m = Y.shape[1]
    cost = -1 / m * np.sum(Y * np.log(A2) + (1 - Y) * np.log(1 - A2))
    cost = np.squeeze(cost)
    return cost


def backward_propagation(parameters, cache, X, Y):
    """ Implement the backward propagation 
    params:
    parameters: python dictionary containing our parameters 
    cache: a dictionary containing "Z1", "A1", "Z2" and "A2".
    X: input data of shape (2, number of examples)
    Y: "true" labels vector of shape (1, number of examples)
    returns:
    grads: python dictionary containing your gradients with respect to different parameters
    """
    m = Y.shape[1]
    dZ2 = cache['A2'] - Y
    dW2 = 1 / m * np.dot(dZ2, cache['A1'].T)
    db2 = 1 / m * np.sum(dZ2, axis = 1, keepdims = True)
    dZ1 = np.dot(parameters['W2'].T, dZ2) * (1 - np.power(cache['A1'], 2))
    dW1 = 1 / m * np.dot(dZ1, X.T)
    db1 = 1 / m * np.sum(dZ1, axis = 1, keepdims = True)
    grads = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}
    return grads


def update_parameters(parameters, grads, learning_rate = 1.2):
    """
    Updates parameters using the gradient descent update rule given above
    params:
    parameters: python dictionary containing your parameters 
    grads: python dictionary containing your gradients 
    returns:
    parameters: python dictionary containing your updated parameters 
    """
    W1 = parameters['W1'] - learning_rate * grads['dW1']
    b1 = parameters['b1'] - learning_rate * grads['db1']
    W2 = parameters['W2'] - learning_rate * grads['dW2']
    b2 = parameters['b2'] - learning_rate * grads['db2']
    parameters = {"W1": W1, "b1": b1, "W2": W2, "b2": b2}
    return parameters


def nn_model(X, Y, n_h, num_iterations = 10000, print_cost=False):
    """  
    params:
    X: dataset of shape (2, number of examples)
    Y: labels of shape (1, number of examples)
    n_h: size of the hidden layer
    num_iterations: Number of iterations in gradient descent loop
    print_cost: if True, print the cost every 1000 iterations
    returns:
    parameters: parameters learnt by the model. They can then be used to predict.
    """
    np.random.seed(3)
    n_x, n_y = layer_sizes(X, Y)[0], layer_sizes(X, Y)[2]
    parameters = initialize_parameters(n_x, n_h, n_y)
    W1, b1, W2, b2 = parameters['W1'], parameters['b1'], parameters['W2'], parameters['b2']
    for i in range(num_iterations):
        A2, cache = forward_propagation(X, parameters)
        cost = compute_cost(A2, Y, parameters)
        grads = backward_propagation(parameters, cache, X, Y)
        parameters = update_parameters(parameters, grads)
        if print_cost and i % 1000 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))
    return parameters


def predict(parameters, X):
    """ Using the learned parameters, predicts a class for each example in X
    params:
    parameters: python dictionary containing your parameters 
    X: input data of size (n_x, m)
    returns
    predictions: vector of predictions of our model (red: 0 / blue: 1) 
    """
    A2, cache = forward_propagation(X, parameters)
    predictions = np.round(A2)
    return predictions


parameters = nn_model(X, Y, n_h = 4, num_iterations = 10000, print_cost=True)
predictions = predict(parameters, X)
print ('Accuracy: %d' % float((np.dot(Y,predictions.T) + np.dot(1-Y,1-predictions.T))/float(Y.size)*100) + '%')
plot_decision_boundary(lambda x: predict(parameters, x.T), X, Y)
plt.title("Decision Boundary for hidden layer size " + str(4))
plt.show()