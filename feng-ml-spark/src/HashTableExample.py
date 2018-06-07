#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel

import tensorflow as tf

# vocabulary_list = tf.constant(["emerson", "lake", "palmer"])
# table = tf.contrib.lookup.index_table_from_tensor(
#     mapping=vocabulary_list, num_oov_buckets=1, default_value=-1)
# features = tf.constant(["emerson", "lake", "and", "palmer"])
# ids = table.lookup(features)
sess = tf.InteractiveSession()
# tf.tables_initializer().run()
# print(ids.eval())

keys = tf.constant(['messi', 'henry', 'jiang'])
values = tf.constant([1, 2, 3])

table = tf.contrib.lookup.HashTable(
    tf.contrib.lookup.KeyValueTensorInitializer(keys, values), -1)

out = table.lookup(tf.constant(['j']))
table.init.run()
print(out.eval())
