#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel


import jieba.posseg as pseg

out = open('/tmp/12.csv', 'w', encoding='utf-8')
with open('/tmp/11.csv', 'r', encoding='utf-8') as f:
    for line in f:
        line = f.readline()
        fields = line.split('\t')
        if len(fields) != 3:
            continue
        content = fields[2].split('!')[1]
        words = pseg.cut(content)
        for word, flag in words:
            if flag == 'a':
                out.write(word + '\n')
out.close()
