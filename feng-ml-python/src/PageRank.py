#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import numpy as np


class PageRank(object):
    def __init__(self, P, V, X):
        self.damping_factor = 0.85
        self.P = P
        self.V = V
        self.X = X

    def page_rank(self):
        n = len(self.V)
        avg = np.ones([n, n]) / n
        A = self.damping_factor * self.P + (1 - self.damping_factor) * avg
        x = self.X
        R = A.dot(x)
        while True:
            if x.all() == R.all():
                return R
            else:
                x = R
                R = A * x


if __name__ == '__main__':
    data = [[0, 1 / float(2), 1, 0], [1 / 3.0, 0, 0, 1 / 2.0], [1 / 3.0, 0, 0, 1 / 2.0], [1 / 3.0, 1 / 2.0, 0, 0]]
    P = np.array(data)
    V = ['a', 'b', 'c', 'd']
    x = np.array([1 / 4, 1 / 4, 1 / 4, 1 / 4])
    pr = PageRank(P, V, x)
    print(pr.page_rank())
