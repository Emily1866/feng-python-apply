#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel

# out = open('/tmp/spu_similarty.csv', 'w', encoding='utf-8')
# with open('/Users/lionel/Desktop/data/recommendDish/spu_similarty.csv', 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         words = line.strip().split("\t")
#         key = words[0]
#         for i in range(1, len(words)):
#             dish, sim = words[i].split(":")
#             out.write(key + '\t' + dish + "\t" + sim + '\n')
# out.close()

from urllib import request

out = open('/tmp/2.csv', 'w', encoding='utf-8')

with open("/tmp/need_match_name_v1.txt", 'r', encoding='utf-8') as file:
    for line in file.readlines():
        fields = line.strip().split("\t")
        if len(fields) != 7:
            continue
        shopId = fields[0]
        picId = fields[1]
        for i in range(2, len(fields)):
            dishName = request.quote(fields[i])
            url = 'http://10.69.69.209:4080/invoke.json?app=poi-nlp-service&timestamp=1521546999&direct=false&version=1&token=&parameters%5B%5D=' + shopId + '&parameters%5B%5D=' + dishName + '&url=http%3A%2F%2Fservice.dianping.com%2Fcom.dianping.poi.nlp.service.RecommendDishService_1.0.0&method=getSimilarityDishes&parameterTypes%5B%5D=java.lang.Integer&parameterTypes%5B%5D=java.lang.String'
            with request.urlopen(url) as f:
                out.write(shopId + '\t' + picId + '\t' + fields[i] + '\t' + f.read().decode('utf-8') + '\n')
