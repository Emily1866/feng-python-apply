#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import nltk
import json

# nltk.download("punkt")


# from nltk.corpus import brown
#
# brown_tagged_sents = brown.tagged_sents(categories='news')
# train_num = int(len(brown_tagged_sents) * 0.9)
# x_train = brown_tagged_sents[0:train_num]
# x_test = brown_tagged_sents[train_num:]
# tagger = nltk.UnigramTagger(train=x_train)
# print(tagger.evaluate(x_test))  # 0.81

all_tagged_sents = []
with open('/Users/lionel/Desktop/data/nlp/人民日报.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        sent = line.split()
        tagged_sent = []
        for item in sent:
            pair = nltk.str2tuple(item)
            tagged_sent.append(pair)
        if len(tagged_sent) > 0:
            all_tagged_sents.append(tagged_sent)

train_size = int(len(all_tagged_sents) * 0.8)

x_train = all_tagged_sents[:train_size]
x_test = all_tagged_sents[train_size:]
tagger = nltk.UnigramTagger(train=x_train, backoff=nltk.DefaultTagger('n'))

tokens = nltk.word_tokenize(u'我 认为 不丹 的 被动 卷入 不 构成 此次 对峙 的 主要 因素。')
tagged = tagger.tag(tokens)
print(json.dumps(tagged, ensure_ascii=False))
print(tagger.evaluate(x_test))
