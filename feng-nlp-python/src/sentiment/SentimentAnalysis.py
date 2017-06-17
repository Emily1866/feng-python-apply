#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import re
from collections import defaultdict

import jieba


def loadWords(file):
    stopwords = []
    with open(file, encoding='utf-8') as file:
        for line in file.readlines():
            reobj = re.compile(r'\d.')
            if reobj.match(line):
                continue
            stopwords.append(line.strip())
    return stopwords


def sentence2words(sentence, stopwords):
    words = []
    for word in jieba.cut(sentence):
        if word not in stopwords:
            words.append(word)
    return words


## 情感定位 ##
def classifyWords(wordDic, senfile, nofile, degreefile):
    senWords = loadWords(senfile)
    senDic = defaultdict()
    for word in senWords:
        tmp = word.strip().split(' ')
        senDic[tmp[0]] = tmp[1]
    noList = loadWords(nofile)
    degreeList = loadWords(degreefile)
    degreeDict = defaultdict()
    for degree in degreeList:
        tmp = degree.strip().split('')
        degreeDict[tmp[0]] = tmp[1]
    senWord = defaultdict()
    notWord = defaultdict()
    degreeWord = defaultdict()


if __name__ == '__main__':
    sentence = '这是我喜欢的书本'
    # stopwords = loadWords('/Users/lionel/Desktop/knowledge/sentiment/data/dataset_616671/stopwords.csv')
    # words = sentence2words(sentence, stopwords)
    # print(words)

    # senList=loadWords('/Users/lionel/Desktop/knowledge/sentiment/data/degreeDict.csv')
    # print(senList)
