#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel

import numpy as np


class PCA(object):
    '''
    data  m*n 矩阵
    '''

    def fit(self, data):
        data = data.T
        print(data)
        n, m = np.shape(data)
        # 矩阵列求平均
        mean = np.mean(data, axis=1)
        # 中心化
        avg = data - mean
        # 求协方差
        cov = (1 / m) * avg * avg.T
        # 求出协方差矩阵的特征值及对应的特征向量
        a, b = np.linalg.eig(cov)
        p = b.T
        return p[0, :] * avg


if __name__ == "__main__":
    data = [[1, 1], [1, 3], [2, 3], [4, 4], [2, 4]]

    # 数组转换为矩阵
    data = np.mat(data)
    x = data[:, 0]
    y = data[:, 1]
    arrayA = []
    arrayB = []
    for i in range(len(x)):
        arrayA.append(x[i])
        arrayB.append(y[i])
    # plt.scatter(arrayA, arrayB, marker='o')
    # plt.show()

    pca = PCA()
    print(pca.fit(data))
    # # # print(x)
    #
    # # 矩阵转置
    # x_T = x.T
    # # print(x_T)
    #
    # n, m = np.shape(x_T)
    # # print(n, m)
    #
    # # 矩阵的逆
    # # x_I = x.I
    # # print(x_I)
    #
    # # 矩阵行求平均
    # mean = np.mean(x_T, axis=1)
    # # print(mean)
    #
    # # 矩阵列求平均
    # # mean = np.mean(x_T, axis=0)
    #
    # # 零均值化
    # avg = x_T - mean
    # print(avg)
    #
    # C = (1 / m) * avg * avg.T
    #
    # a, b = np.linalg.eig(C)
    #
    # # print(a)
    # # print(b)
    #
    # # 获取 b 矩阵的第一列
    # # column1 = b[:, 0]
    #
    # p = b.T
    # print(p)
    #
    # print(p[0, :])
    # # print(C)
    # # print(p.T)
    # #
    # # print(p * C)
    #
    # pcpT = p * C * p.T
    #
    # # print(pcpT)
    #
    # print(p[0, :] * avg)
