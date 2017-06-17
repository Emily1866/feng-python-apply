#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba.posseg as pseg

from gensim.models import Doc2Vec

if __name__ == '__main__':
    # check and process input arguments
    # if len(sys.argv) < 3:
    #     sys.exit(1)
    # file, word = sys.argv[1:3]


    model = Doc2Vec.load('../data/out1')

    test_data = '价格便宜，味道也不错啊，服务态度也很好，尤其是那个鸳鸯雪豆腐特别好吃'
    test_cut_raw = []
    item = pseg.cut(test_data)
    for k in list(item):
        test_cut_raw.append(k.word)
    print(test_cut_raw)
    inferred_vector = model.infer_vector(test_cut_raw)
    sims = model.docvecs.most_similar([inferred_vector], topn=1)
    print(sims)
    # sims是一个tuples,(index_of_document, similarity)

    # docvecs = Doc2Vec.load('../data/out2').docvecs
    #
    # print(docvecs.most_similar(1))
