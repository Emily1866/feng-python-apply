# coding:utf-8

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer

onehot_encoder = DictVectorizer()
instances = [{'city': '北京'}, {'city': '天津'}, {'city': '上海'}]
print(onehot_encoder.fit_transform(instances).toarray())

corpus = [
    'UNC played Duke in basketball',
    'Duke lost the basketball game']
vectorizer = CountVectorizer()
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)
