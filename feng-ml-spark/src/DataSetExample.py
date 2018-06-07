#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: lionel

import tensorflow as tf
import itertools


def gen():
    for i in itertools.count(1):
        yield (i, [1] * i)


if __name__ == '__main__':
    dataset = tf.data.Dataset.from_tensors(tf.constant([['jiang', 'feng'], ['messi', 'henry']]))
    print(dataset.output_shapes)
    print(dataset.output_types)

    dataset2 = tf.data.Dataset.from_tensor_slices(tf.constant([['jiang', 'feng'], ['messi', 'henry']]))
    print(dataset.output_shapes)
    print(dataset.output_types)

    dataset3 = tf.data.Dataset.from_generator(gen, (tf.int64, tf.int64), (tf.TensorShape([]), tf.TensorShape([None])))

    dataset4 = tf.data.Dataset.range(100).map(
        lambda x: x + tf.random_uniform([], -10, 10, tf.int64))
    print(dataset4.output_shapes)
    print(dataset4.output_types)

    iterator = dataset4.make_one_shot_iterator()
    next_element = iterator.get_next()
    with tf.Session() as sess:
        for i in range(100):
            try:
                print(sess.run(next_element))
            except tf.errors.OutOfRangeError:
                break
