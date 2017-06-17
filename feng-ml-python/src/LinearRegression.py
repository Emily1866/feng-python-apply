#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn import linear_model
import matplotlib.pyplot as plt

import numpy as np

if __name__ == '__main__':
    array = []
    with open('../resources/lg.txt', 'r') as file:
        for line in file.readlines():
            array.append(np.array(line.strip().split("\t")).astype(np.float))
    tmp = np.array(array)
    x = tmp[0:, 0:2]
    y = tmp[0:, 2:3]
    lr = linear_model.LinearRegression()
    lr.fit(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, 'b.')
    y = lr.coef_ * x + lr.intercept_
    plt.plot(x, y, 'r-')
    plt.legend()
    plt.show()
    x = np.array([1.0, 1.2])
    print(lr.predict(x))
