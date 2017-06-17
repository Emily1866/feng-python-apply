#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    X = np.linspace(0, 1, 1000)
    Y = -X * np.log2(X) - (1 - X) * np.log2(1 - X)
    plt.plot(X, Y)
    plt.show()
