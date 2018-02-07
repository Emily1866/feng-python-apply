#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel


import fasttext
from sklearn import metrics


def train():
    fasttext.supervised("/tmp/xinlang.train", "/tmp/xinlang.model", label_prefix="__label__", lr=1, dim=200,
                        word_ngrams=2, bucket=10000000, epoch=20)


def evaluate():
    classifier = fasttext.load_model("/tmp/xinlang.model.bin", label_prefix="__label__")
    labels_right = []
    texts = []
    with open('/tmp/xinlang.test', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            fields = line.strip().split('\t')
            labels_right.append(fields[1].replace("__label__", ""))
            texts.append(fields[0])
    labels_predict = [e[0] for e in classifier.predict(texts)]
    print(metrics.classification_report(labels_right, labels_predict))


if __name__ == '__main__':
    # train()
    evaluate()
