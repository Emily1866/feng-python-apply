import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        pass

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0)
                self.errors_.append(errors)
                pass
            pass
        pass

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
        pass

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
        pass


if __name__ == '__main__':
    file = '/Users/dianping/Downloads/iris.csv'
    df = pd.read_csv(file, header=None)
    # print(df.head(10)

    y = df.loc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    print(y)

    X = df.iloc[0:100, [0, 2]].values
    print(X)

    plt.scatter(X[:50, 0], X[0: 50, 1], color='red', marker='o', label='setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
    plt.xlabel('花瓣长度')
    plt.ylabel('花茎长度')
    ppn = Perceptron()
    ppn.fit(X, y)
    x = np.array([5, 0.9])
    print(ppn.predict(x))
    # print(ppn.errors_)
    # plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    # plt.xlabel('Epochs')
    # plt.ylabel('错误分类次数')
    plt.show()
