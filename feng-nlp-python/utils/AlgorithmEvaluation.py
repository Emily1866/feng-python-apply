#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import sys


# 数据预处理
def data_preprocess(file):
    with open(file, 'r') as file:
        array = []
        for line in file.readlines():
            array.append(line.split(':')[0])
    return array


# list 的交集
def Intersection(array, array2):
    array = list((set(array).union(set(array2))) ^ (set(array) ^ set(array2)))
    return len(array)


if __name__ == '__main__':
    if len(sys.argv) < 5:
        sys.exit(1)
    t0, f0, t1, f1 = sys.argv[1:5]
    T0 = data_preprocess(t0)
    F0 = data_preprocess(f0)
    T1 = data_preprocess(t1)
    F1 = data_preprocess(f1)
    print(Intersection(T0, T1))
    print(Intersection(T0, F1))
    print(Intersection(F0, F1))
    print(Intersection(F0, T1))
