#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

import numpy as np
from sklearn.naive_bayes import GaussianNB


# 根据文件路径加载数据
def load_data(file_name):
    file = open(file_name)
    data = []
    for line in file.readlines():
        tmpline = line.split(' ')
        tmp = []
        for x in tmpline:
            tmp.append(float(x))
        data.append(tmp)
    return data


# 数据分为训练数据 train_set 和测试数据 test_set
def split_data(data, split_ratio):
    train_size = int(len(data) * split_ratio)
    train_set = []
    test_set = list(data)
    while len(train_set) < train_size:
        index = random.randrange(len(test_set))
        train_set.append(test_set.pop(index))
    return [train_set, test_set]


# 数据分为属性集 x 和结果集 y
def targetAndData(set):
    x = [attribute[0:-1] for attribute in set]
    y = [target[-1] for target in set]
    return [x, y]


# 计算预测准确率
def accuracy(test_res, origin_res):
    num = 0
    for i in range(len(test_res)):
        if test_res.flat[i] == origin_res.flat[i]:
            num += 1
    return num / float(len(test_res)) * 100


if __name__ == '__main__':
    train_set, test_set = split_data(load_data('/tmp/test1'), 0.8)
    print(train_set)
    print(test_set)
    train_x, train_y = targetAndData(train_set)
    test_x, test_y = targetAndData(test_set)
    gnb = GaussianNB()
    y_pred = gnb.fit(train_x, train_y)
    res = gnb.predict(test_x)
    print('Accuracy is {0}%'.format(accuracy(res, np.array(test_y))))
