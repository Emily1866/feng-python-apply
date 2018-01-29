#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import re
from collections import Counter
import pandas as pd


def words(text):
    return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('/Users/lionel/Desktop/data/nlp/page/norvig.com', 'r').read()))


def probability(word):
    print("总词数:%d" % sum(WORDS.values()))
    return 1.0 * WORDS[word] / sum(WORDS.values())


def correction(word):
    return max(candidates(word), key=probability)


def candidates(word):
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def read_file(path):
    dishes = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            dishes.append(line.strip())
    return dishes


if __name__ == '__main__':
    # print(edits1("speling"))
    # print(correction("speling"))
    # file1 = open("/tmp/1.csv", 'w', encoding='utf-8')
    # data = pd.read_csv("/Users/lionel/Downloads/dish_statistic.csv", sep='\t')
    # data.iloc[:, 1] = data.iloc[:, 1] / 198387851
    # for item in data.values:
    #     file.write(str(item[0]) + ':' + str(item[1]) + '\n')

    # file = open("/tmp/1.csv", 'r', encoding='utf-8')
    # for line in file.readlines():
    #     print(line)
    # file = open('/Users/lionel/Downloads/1.csv', 'r', encoding='utf-8')
    # file.readline()
    # for line in file.readlines():
    #     if len(line.strip()) == 4:
    #         file1.write(line.strip() + "\n")

    dish2 = read_file("/Users/lionel/Desktop/len2.csv")
    dish3 = read_file("/Users/lionel/Desktop/len3.csv")
    file3 = open('/tmp/1.csv', 'w', encoding='utf-8')
    dish4 = read_file("/Users/lionel/Desktop/len4.csv")
    for item2 in dish2:
        for item3 in dish3:
            if item2 in item3:
                continue
            else:
                file3.write(item3 + "\n")
