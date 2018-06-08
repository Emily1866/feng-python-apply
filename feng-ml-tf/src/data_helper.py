#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import collections
import tensorflow as tf


def load_data(filename, sep=' ', sep1=',', isCharacter=False):
    label_list = []
    features_list = []
    with tf.gfile.GFile(filename, 'r') as f:
        for line in f.readlines():
            fields = line.strip().split(sep)
            if len(fields) != 2:
                continue
            label = fields[0]
            features = fields[1]
            label_list.append(label)
            if isCharacter:
                features_list.append(list(features))
            else:
                features_list.append(features.split(sep1))
    return label_list, features_list


def gen(filepath):
    with tf.gfile.GFile(filepath, 'r') as f:
        for line in f.readlines():
            fields = line.strip().split(' ')
            if len(fields) != 2:
                continue
            label = fields[0]
            features = fields[1]
            yield (label, features.split(','))


def build_word_dic(words_list, label_list, vocab_size=5000):
    word_dic = dict()
    word_dic['pad'] = 0
    word_dic['unk'] = 1
    all_words = []
    for words in words_list:
        all_words.extend(words)
    counter = collections.Counter(all_words).most_common(vocab_size)
    words, _ = list(zip(*counter))
    for word in words:
        word_dic[word] = len(word_dic)
    label_set = set(label_list)
    label_dic = dict()
    for label in label_set:
        label_dic[label] = len(label_dic)
    return words, word_dic, label_set, label_dic


def build_dic_hash_table(word_dic, label_dic):
    word_keys = tf.constant(list(word_dic.keys()))
    word_values = tf.constant(list(word_dic.values()))
    word_table = tf.contrib.lookup.HashTable(
        tf.contrib.lookup.KeyValueTensorInitializer(word_keys, word_values), word_dic['unk'])
    label_keys = tf.constant(list(label_dic.keys()))
    label_values = tf.constant(list(label_dic.values()))
    label_table = tf.contrib.lookup.HashTable(
        tf.contrib.lookup.KeyValueTensorInitializer(label_keys, label_values), -1)
    return word_table, label_table


def train_input_fn(label_list, features_list, shuffle_size, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices((label_list, features_list))
    dataset = dataset.shuffle(shuffle_size).repeat().batch(batch_size)
    return dataset


def build_table_from_text_file(filepath):
    return tf.contrib.lookup.HashTable(
        tf.contrib.lookup.TextFileInitializer(filepath, tf.string, 0, tf.int64, 1, delimiter=" "), -1)


if __name__ == '__main__':
    # label_list, features_list = load_data('/tmp/1.csv')
    # words, word_dic, labels, label_dic = build_word_dic(features_list, label_list)
    # word_table, label_table = build_dic_hash_table(word_dic, label_dic)
    sess = tf.InteractiveSession()
    # word_out = word_table.lookup(tf.constant(list(word_dic.keys())))
    # label_out = label_table.lookup(tf.constant(list(label_dic.keys())))
    # tf.tables_initializer().run()
    # print(word_out.eval())
    # print(label_out.eval())

    table = build_table_from_text_file('/tmp/2.csv')
    out = table.lookup(tf.constant(['emerson']))
    table.init.run()

    print(out.eval())
