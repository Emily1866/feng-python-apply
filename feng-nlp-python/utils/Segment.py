#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel

import jieba.posseg as pseg
import sys


class Segment(object):
    def parse(self, in_file, out_file):
        output_file = open(out_file, 'w')
        with open(in_file, 'r') as file:
            line = file.readline()
            i = 0
            for line in file.readlines():
                sentence = ""
                line = line.strip().split('\t')
                for word, flag in pseg.cut(line[1].strip()):
                    if flag == 'x':
                        continue
                    else:
                        sentence = sentence + word + " "
                output_file.write(sentence.strip() + "\n")
                i += 1
                if i % 100 == 0:
                    print('Handle lines %d' % i)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python script.py input_file out_file')
        sys.exit(1)
    in_file, out_file = sys.argv[1], sys.argv[2]
    segment = Segment()
    segment.parse(in_file, out_file)
