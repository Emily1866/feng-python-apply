# encoding=utf-8
import numpy as np


def gradAscent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)  # 数据列表转换成矩阵
    labelMat = np.mat(classLabels).transpose()  # 类标签列表转换成矩阵
    m, n = np.shape(dataMatrix)  # 得到dataMatrix矩阵大小
    alpha = 0.001  # 每次上升的步长
    maxCycles = 500  # 迭代次数
    weights = np.ones((n, 1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)  # 计算假设函数h（列向量）
        error = (labelMat - h)  # 类标签和假设函数的误差
        weights = weights + alpha * dataMatrix.transpose() * error  # 对weights进行迭代更新
    return weights


def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('../resources/lr.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])  # 得到数据列表
        labelMat.append(int(lineArr[2]))  # 类标签
    return dataMat, labelMat


if __name__ == '__main__':
    data, lable = loadDataSet()
    weights = gradAscent(data, lable)
    print(weights)
