#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import math


# 根据文件路径加载数据
def load_data(file_name):
    data = []
    with open(file_name) as file:
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


# 根据结果分类
def separate_by_class(data):
    y = {}
    for i in range(len(data)):
        vector = data[i]
        if vector[-1] not in y:
            y[vector[-1]] = []
        y[vector[-1]].append(vector)
    return y


# 计算平均值
def average(numbers):
    return sum(numbers) / float(len(numbers))


# 计算样本方差
def stdev(numbers):
    avg = average(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)


# 计算每个属性的平均值和样本方差
def summarize(data):
    summaries = [(average(attribute), stdev(attribute)) for attribute in zip(*data)]
    del summaries[-1]
    return summaries


def summaries_by_class(data):
    y = separate_by_class(data)
    summaries = {}
    for classValue, instances in y.items():
        summaries[classValue] = summarize(instances)
    return summaries


# 计算高斯分布
def calculate_Probability(x, avg, stdev):
    exponent = math.exp((-1) * (math.pow(x - avg, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


# 计算输入向量的贝叶斯概率
def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            avg, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculate_Probability(x, avg, stdev)
    return probabilities


# 找到最大的值
def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel


def getPredictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions


# 计算预测正确率
def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


if __name__ == '__main__':
    data = load_data("/tmp/pima-indians-diabetes.txt")
    trainSet, testSet = split_data(data, 0.8)
    summaries = summaries_by_class(trainSet)
    print(
        'split {0} rows data into {1} rows trainData and {2} rows testData'.format(len(data), len(trainSet),
                                                                                   len(testSet)))
    predictions = getPredictions(summaries, testSet)
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy:{0}%'.format(accuracy))
