#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
from src.InformationGain import InformationGain
import numpy as np


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
