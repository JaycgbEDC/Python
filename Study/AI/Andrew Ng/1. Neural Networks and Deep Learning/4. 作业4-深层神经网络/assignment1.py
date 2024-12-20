import numpy as np
import h5py
import matplotlib.pyplot as plt
from testCases_v2 import *
from dnn_utils_v2 import sigmoid, sigmoid_backward, relu, relu_backward


def initialize_parameters(n_x, n_h, n_y):
    """  
    params:
    n_x: size of the input layer
    n_h: size of the hidden layer
    n_y: size of the output layer
    
    returns:
    parameters: python dictionary containing your parameters:
                    W1 -- weight matrix of shape (n_h, n_x)
                    b1 -- bias vector of shape (n_h, 1)
                    W2 -- weight matrix of shape (n_y, n_h)
                    b2 -- bias vector of shape (n_y, 1)
    """
    np.random.seed(1)
    W1 = np.random.randn(n_h, n_x) * 0.01
    b1 = np.zeros((n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.01
    b2 = np.zeros((n_y, 1))

    assert(W1.shape == (n_h, n_x))
    assert(b1.shape == (n_h, 1))
    assert(W2.shape == (n_y, n_h))
    assert(b2.shape == (n_y, 1))

    parameters = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}
    return parameters


def initialize_parameters_deep(layer_dims):
    """  
    params:
    ayer_dims: python array (list) containing the dimensions of each layer in our network
    returns:
    parameters: python dictionary containing your parameters "W1", "b1", ..., "WL", "bL":
                    Wl -- weight matrix of shape (layer_dims[l], layer_dims[l-1])
                    bl -- bias vector of shape (layer_dims[l], 1)
    """
    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)
    for l in range(1, L):
        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l - 1]) * 0.01
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
    return parameters


def linear_forward(A, W, b):
    """ Implement the linear part of a layer's forward propagation 
    params:
    A: activations from previous layer (or input data): (size of previous layer, number of examples)
    W: weights matrix: numpy array of shape (size of current layer, size of previous layer)
    b: bias vector, numpy array of shape (size of the current layer, 1)
    returns:
    Z: the input of the activation function, also called pre-activation parameter 
    cache: a python dictionary containing "A", "W" and "b" ; stored for computing the backward pass efficiently
    """
    Z = np.dot(W, A) + b
    cache = (A, W, b)
    return Z, cache


def linear_activation_forward(A_prev, W, b, activation):
    """ Implement the forward propagation for the LINEAR->ACTIVATION layer
    params:
    A_prev: activations from previous layer (or input data): (size of previous layer, number of examples)
    W: weights matrix: numpy array of shape (size of current layer, size of previous layer)
    b: bias vector, numpy array of shape (size of the current layer, 1)
    activation: the activation to be used in this layer, stored as a text string: "sigmoid" or "relu"
    returns:
    A: the output of the activation function, also called the post-activation value 
    cache: a python dictionary containing "linear_cache" and "activation_cache";
             stored for computing the backward pass efficiently 
    """
    if activation == "sigmoid":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = sigmoid(Z)
    elif activation == "relu":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = relu(Z)
    cache = (linear_cache, activation_cache)
    return A, cache


def L_model_forward(X, parameters):
    """ Implement forward propagation for the [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID computation 
    params:
    X: data, numpy array of shape (input size, number of examples)
    parameters: output of initialize_parameters_deep()   
    returns:
    AL: last post-activation value
    caches: list of caches containing:
                every cache of linear_relu_forward() (there are L-1 of them, indexed from 0 to L-2)
                the cache of linear_sigmoid_forward() (there is one, indexed L-1) 
    """
    caches = []
    A = X
    L = len(parameters) // 2
    for l in range(1, L):
        A_prev = A
        A, cache = linear_activation_forward(A_prev, parameters['W' + str(l)], parameters['b' + str(l)], "relu")
        caches.append(cache)
    AL, cache = linear_activation_forward(A, parameters['W' + str(L)], parameters['b' + str(L)], "sigmoid")
    caches.append(cache)
    return AL, caches


def compute_cost(AL, Y):
    """ Implement the cost function defined by equation (7).
    params:
    AL: probability vector corresponding to your label predictions, shape (1, number of examples)
    Y: true "label" vector (for example: containing 0 if non-cat, 1 if cat), shape (1, number of examples)
    returns:
    cost: cross-entropy cost 
    """
    m = Y.shape[1]
    cost = - 1 / m * np.sum(Y * np.log(AL) + (1 - Y) * np.log(1 - AL), axis = 1, keepdims = True)
    cost = np.squeeze(cost)
    return cost


def linear_backward(dZ, cache):
    """ Implement the linear portion of backward propagation for a single layer (layer l)
    params:
    dZ: Gradient of the cost with respect to the linear output (of current layer l)
    cache: tuple of values (A_prev, W, b) coming from the forward propagation in the current layer
    returns:
    dA_prev: Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev
    dW: Gradient of the cost with respect to W (current layer l), same shape as W
    db: Gradient of the cost with respect to b (current layer l), same shape as b 
    """
    A_prev, W, b = cache
    m = A_prev.shape[1]
    dW = 1 / m * np.dot(dZ, A_prev.T)
    db = 1 / m * np.sum(dZ, axis = 1, keepdims = True)
    dA_prev = np.dot(W.T, dZ)
    return dA_prev, dW, db


def linear_activation_backward(dA, cache, activation):
    """ Implement the backward propagation for the LINEAR->ACTIVATION layer.
    params:
    dA: post-activation gradient for current layer l 
    cache: tuple of values (linear_cache, activation_cache) we store for computing backward propagation efficiently
    activation: the activation to be used in this layer, stored as a text string: "sigmoid" or "relu"
    returns:
    dA_prev: Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev
    dW: Gradient of the cost with respect to W (current layer l), same shape as W
    db: Gradient of the cost with respect to b (current layer l), same shape as b 
    """
    linear_cache, activation_cache = cache
    if activation == "relu":
        dZ = relu_backward(dA, activation_cache)
    elif activation == "sigmoid":
        dZ = sigmoid_backward(dA, activation_cache)
    dA_prev, dW, db = linear_backward(dZ, linear_cache)
    return dA_prev, dW, db


def L_model_backward(AL, Y, caches):
    """ Implement the backward propagation for the [LINEAR->RELU] * (L-1) -> LINEAR -> SIGMOID group
    params:
    AL: probability vector, output of the forward propagation (L_model_forward())
    Y: true "label" vector (containing 0 if non-cat, 1 if cat)
    caches: list of caches containing:
                every cache of linear_activation_forward() with "relu" (it's caches[l], for l in range(L-1) i.e l = 0...L-2)
                the cache of linear_activation_forward() with "sigmoid" (it's caches[L-1])
    returns:
    grads: A dictionary with the gradients
             grads["dA" + str(l)] = ...
             grads["dW" + str(l)] = ...
             grads["db" + str(l)] = ... 
    """
    grads = {}
    L = len(caches)
    m = Y.shape[1]
    Y = Y.reshape(AL.shape)
    dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
    current_cache = caches[L-1]
    grads["dA" + str(L)], grads["dW" + str(L)], grads["db" + str(L)] = linear_activation_backward(dAL, current_cache, activation = "sigmoid")
    for l in range(L - 1)[::-1]:
        current_cache = caches[l]
        grads["dA" + str(l + 1)], grads["dW" + str(l + 1)], grads["db" + str(l + 1)] = linear_activation_backward(grads["dA" + str(l+2)], current_cache, activation = "relu")
    return grads


def update_parameters(parameters, grads, learning_rate):
    """ Update parameters using gradient descent
    params:
    parameters: python dictionary containing your parameters 
    grads: python dictionary containing your gradients, output of L_model_backward
    returns:
    parameters: python dictionary containing your updated parameters 
                  parameters["W" + str(l)] = ... 
                  parameters["b" + str(l)] = ... 
    """
    L = len(parameters) // 2
    for l in range(L):
        parameters['W' + str(l + 1)] = parameters['W' + str(l + 1)] - learning_rate * grads["dW" + str(l + 1)]
        parameters['b' + str(l + 1)] = parameters['b' + str(l + 1)] - learning_rate * grads["db" + str(l + 1)]
    return parameters