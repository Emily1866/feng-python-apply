#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: lionel
import gensim


class MySentence(object):
    def __init__(self, dirname):
        self.dirname = dirname
        pass

    def __iter__(self):
        file = open(self.dirname, encoding='utf-8')
        for line in file.readlines():
            yield line.split(' ')
            pass
        pass


if __name__ == '__main__':
    sentences = MySentence('/Users/lionel/Desktop/3.csv')
    # sentence = LineSentence('/Users/lionel/Desktop/3.csv')
    # model = gensim.models.Word2Vec(sentences, min_count=100, size=200)
    # model.save("/Users/lionel/Desktop/dish_word2vec_model")
    # model.save_word2vec_format('/Users/lionel/Desktop/dish_word2vec_model1', binary=False)
    model = gensim.models.Word2Vec.load('/Users/lionel/Desktop/dish_word2vec_model')
    # model.wv.save_word2vec_format("/tmp/dish_word2vec_model.csv", binary=False)
    # print(model.wv['牛肉'])
    print(model.most_similar("牛肉"))
