# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt


# sigmoid 函数
def sigmoid(X):
    return 1.0 / (1 + np.exp(-X))


# sigmoid 函数导数
def sigmoid_derivative(X):
    Y = sigmoid(X)
    return np.multiply(Y, 1 - Y)


def initialize_parameters(n_x):
    W = np.zeros((1, n_x))
    b = np.zeros((1, 1))
    parameters = {"W": W,
                  "b": b}
    return parameters


def forward_propagation(X, parameters):
    Z = np.dot(parameters["W"], X) + parameters["b"]
    A = sigmoid(Z)
    cache = {"Z": Z,
             "A": A}
    return cache


def compute_cost(A, Y):
    m = Y.shape[1]
    logprobs = np.multiply(np.log(A), Y) + np.multiply(np.log(1 - A), (1 - Y))
    cost = (-1 / m) * np.sum(logprobs)
    cost = np.squeeze(cost)

    return cost


def backward_propagation(cache, X, Y):
    m = X.shape[1]
    Y = Y.reshape((1, m))
    A = cache['A']
    dZ = A - Y
    dW = (1 / m) * np.dot(dZ, X.T)
    db = (1 / m) * np.sum(dZ, axis=1, keepdims=True)
    grads = {'dW': dW,
             'db': db}
    return grads


def update_parameters(parameters, grads, learning_rate=0.02):
    W = parameters['W']
    b = parameters['b']
    dW = grads['dW']
    db = grads['db']
    W -= learning_rate * dW
    b -= learning_rate * db
    parameters = {'W': W,
                  'b': b}
    return parameters


def lr_model(X, Y, num_iteration=20000, print_cost=False, seed=3):
    np.random.seed(seed)
    # m为样本数，n 为样本维度
    n_x, m = X.shape
    parameters = initialize_parameters(n_x)
    for i in range(num_iteration):
        cache = forward_propagation(X, parameters)
        cost = compute_cost(cache['A'], Y)
        # print(cost)

        grads = backward_propagation(cache, X, Y)
        parameters = update_parameters(parameters, grads)
        if print_cost and i % 1000 == 0:
            print("Cost after iteration %i: %s" % (i, str(cost)))
    return parameters


if __name__ == '__main__':
    # re = initialize_parameters(3)
    # print(re)
    #
    # A = np.ones((1, 4)) * 0.5
    # B = np.ones((1, 4)) * 0.6
    # print(A)
    # print(B)
    # print(compute_cost(A, B))
    X = np.array([[0.5, 0.5], [0.6, 0.8], [0.4, 0.6], [1.0, 1.4], [1.1, 1.3], [1.2, 1.5]])
    Y = np.array([[0], [0], [0], [1], [1], [1]])
    plt.scatter(X[:, 0], X[:, 1], c=Y, s=40)
    parameters = lr_model(X.T, Y.T, print_cost=True)
    w1 = parameters['W'][0][0]
    w2 = parameters['W'][0][1]
    b = parameters['b'][0][0]
    x = np.linspace(0, 2)
    y = -(w1 / w2) * x - b / w2
    plt.plot(x, y)
    plt.show()
