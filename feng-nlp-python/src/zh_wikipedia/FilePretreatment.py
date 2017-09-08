#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import re


def pre_process(input_file, output_file):
    multi_version = re.compile('-\{.*?(zh-hans|zh-cn):([^;]*?)(;.*?)?\}-')
    punctuation = re.compile(u"[-~!@#$%^&*()_+`=\[\]\\\{\}\"|;':,./<>?·！@#￥%……&*（）——+【】、；‘：“”，。、《》？「『」』]")
    with open(output_file, 'w') as outfile:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile.readline():
                line = multi_version.sub(u'\2', line)
                line = punctuation.sub('', line)
                outfile.write(line)


if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print('Usage: python script.py input_file output_file')
    #     sys.exit()
    # inputfile, outputfile = sys.argv[1], sys.argv[2]
    # pre_process(inputfile, outputfile)

    pass


