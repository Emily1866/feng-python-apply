import re
import urllib

import pymysql

# conn = pymysql.connect(host='127.0.0.1', port=3306, user='fengj', passwd='gogg897@!', db='Content',
#                        charset='utf8')
# cursor = conn.cursor()
# cursor.execute("truncate table Wikipedia_Paper")
# conn.commit()

import pandas as pd
import numpy as np
import urllib.request
import urllib.parse


def parse(file):
    df = pd.read_excel(file, sheetname='团单菜品与招牌菜', header=0)
    shopIds = np.array(df['门店ID'])
    dishs = np.array(df['招牌菜名称'])
    for i in range(len(dishs)):
        param = urllib.parse.urlencode(dishs[i])
        path = 'http://localhost:4080/invoke.json?validate=true&app=poi-nlp-service&timestamp=1500366765&direct=false&' \
               'token=undefined&parameters%5B%5D=%d&parameters%5B%5D=%7B%s%7D&' \
               'url=http%3A%2F%2Fservice.dianping.com%2Fcom.dianping.poi.nlp.service.PoiNlpService_1.0.0&' \
               'method=getDuplicatedDishByDish&parameterTypes%5B%5D=java.lang.Integer&parameterTypes%5B%5D=com.dianping.poi.nlp.dto.NLPDishDTO' % (
                   shopIds[i], dishs[i])
        req = urllib.request.urlopen(path)


if __name__ == "__main__":
    # with open('/tmp/1.csv', 'r') as file:
    #     sentence = ""
    #     url = ""
    #     category = ""
    #     for line in file.readlines():
    #         if line.startswith('<doc id'):
    #             relink = '<doc .* url="(.*)" title="(.*)">'
    #             cinfo = re.findall(relink, line.strip())
    #             if len(cinfo) != 1:
    #                 continue
    #             url = cinfo[0][0]
    #             category = cinfo[0][1]
    #             print(url, category)
    #             continue
    #         if not line.startswith('</doc>') and line is not None:
    #             sentence = sentence + line.strip()
    #         else:
    #             # try:
    #             cursor.execute('INSERT  INTO Wikipedia_Paper (category, url, text) VALUES (%s,%s,%s)',
    #                            (category, url, sentence))
    #             conn.commit()
    #             # except :
    #             #     print("error %s", (url))

    # path = "/Users/lionel/Desktop/data/recommendDish/录入推荐菜门店合作交易产品明细.xlsx"
    # parse(path)

    out = open('/tmp/1.csv', 'w')

    dish = urllib.parse.quote('{"dishName":"鸡肉"}')
    shopId = 69270665
    path = "http://10.72.203.168:4080/invoke.json?validate=true&app=poi-nlp-service&timestamp=1500366765&direct=false&token=undefined&parameters[]=%d&parameters[]=%s&url=http://service.dianping.com/com.dianping.poi.nlp.service.PoiNlpService_1.0.0&method=getDuplicatedDishByDish&parameterTypes[]=java.lang.Integer&parameterTypes[]=com.dianping.poi.nlp.dto.NLPDishDTO" % (
        shopId, dish)
    print(path)

    with urllib.request.urlopen(path) as f:
        result = f.read().decode('utf-8')
        print(re.findall('([\u4e00-\u9fa5]+)', result))
