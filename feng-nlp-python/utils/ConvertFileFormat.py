#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# Author: lionel


import sys

import chardet


def judge_file_format(file_path):
    with open(file_path, 'rb') as file:
        for line in file.readlines():
            return chardet.detect(line)['encoding']


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(1)
    inputFile, outputFile = sys.argv[1:3]

    output = open(outputFile, 'w')

    if judge_file_format(inputFile) == 'utf-8':
        with open(inputFile, encoding='utf-8') as file:
            for line in file.readlines():
                output.write(line)

    elif judge_file_format(inputFile) == 'ascii':
        output = open(outputFile, 'w')
        with open(inputFile, encoding='utf-8') as file:
            for line in file.readlines():
                output.write(line.encode('utf-8').decode('unicode-escape'))
    output.close()
