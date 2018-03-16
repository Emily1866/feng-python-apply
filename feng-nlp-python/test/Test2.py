#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel

out = open('/tmp/spu_similarty.csv', 'w', encoding='utf-8')
with open('/Users/lionel/Desktop/data/recommendDish/spu_similarty.csv', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        words = line.strip().split("\t")
        key = words[0]
        for i in range(1, len(words)):
            dish, sim = words[i].split(":")
            out.write(key + '\t' + dish + "\t" + sim + '\n')
out.close()
