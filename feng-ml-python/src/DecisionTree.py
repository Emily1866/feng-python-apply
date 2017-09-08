#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import numpy as np


class InformationGain(object):
    # 计算香农熵
    def calcShannonEnt(self, data):
        m, n = np.shape(data)
        labelCounts = {}
        for i in range(m):
            currentLabel = data[i][-1]
            if currentLabel not in labelCounts:
                labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
        shannonEnt = 0.0
        for key in labelCounts:
            prob = labelCounts[key] / m
            shannonEnt -= prob * np.log2(prob)
        return shannonEnt

    def splitData(self, data, axis, value):
        retData = []
        m, n = np.shape(data)
        for i in range(m):
            if data[i][axis] == value:
                reducedFeatVec = np.delete(data[i], axis, axis=0)
                retData.append(reducedFeatVec)
        return np.array(retData)

    def chooseBestFeatureToSplit(self, data):
        m, n = np.shape(data)
        # 特征个数
        numFeatures = n - 1
        baseEntropy = self.calcShannonEnt(data)
        bestInfoGain = 0.0
        bestFeature = -1
        for i in range(numFeatures):
            featureValues = [data[j][i] for j in range(m)]
            uniqueValues = set(featureValues)
            newEntropy = 0.0
            for value in uniqueValues:
                subData = self.splitData(data, i, value)
                prob = len(subData) / m
                newEntropy += prob * self.calcShannonEnt(subData)
            infoGain = baseEntropy - newEntropy
            if infoGain > bestInfoGain:
                bestInfoGain = infoGain
                bestFeature = i
        return bestFeature


class DecisionTree(object):
    def majorityCnt(self, classList):
        classCount = {}
        for i in range(len(classList)):
            if classList[i] not in classCount.keys():
                classCount[classList[i]] = 0
            classCount[classList[i]] += 1
        return max(classCount)

    def buildTree(self, data, features):
        classification = data[:, -1]
        uniqueValues = set(classification)
        if len(uniqueValues) == 1:
            return classification[0]
        if len(data[0]) == 1:
            return self.majorityCnt(classification)

        infomatinoGain = InformationGain()
        bestFeature = infomatinoGain.chooseBestFeatureToSplit(data)
        bestFeatureLabel = features[bestFeature]
        decisionTree = {bestFeatureLabel: {}}
        featureValues = set(data[:, bestFeature])
        tmpFeatures = np.delete(features, bestFeature, axis=0)
        for value in featureValues:
            subData = infomatinoGain.splitData(data, bestFeature, value)
            decisionTree[bestFeatureLabel][value] = self.buildTree(subData, tmpFeatures)
        return decisionTree


if __name__ == '__main__':
    features = ['L', 'F', 'H']
    arr = [[-1, -1, 0, 0],
           [-1, 1, 1, 1],
           [1, 0, 1, 1],
           [0, 0, 1, 1],
           [1, 0, 1, 1],
           [0, 1, 0, 1],
           [0, -1, 0, 0],
           [1, 0, 0, 1],
           [0, -1, 0, 1],
           [-1, -1, 1, 0]]
    features = ['no surfaceing', 'flippers']
    arr = [[1, 1, 1],
           [1, 1, 1],
           [1, 0, 0],
           [0, 1, 0],
           [0, 1, 0]]
    data = np.array(arr)

    decisionTree = DecisionTree()
    tree = decisionTree.buildTree(data, features)
    print(tree)
