import gensim


class MySentence(object):
    def __init__(self, dirname):
        self.dirname = dirname
        pass

    def __iter__(self):
        file = open(self.dirname, encoding='utf-8')
        for line in file.readlines():
            yield line.split('\t')
            pass
        pass


if __name__ == '__main__':
    sentences = MySentence('/Users/dianping/Desktop/dish_word2vec_corpus.csv')
    model = gensim.models.Word2Vec(sentences, min_count=100, size=200)
    model.save("/Users/dianping/Desktop/model/dish_word2vec_model")
    # model.wv.save_word2vec_format("/tmp/dish_word2vec_model.csv", binary=False)
    print(model.wv['红烧'])
