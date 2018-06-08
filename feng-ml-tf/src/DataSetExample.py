#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: lionel

import tensorflow as tf

filepath = '/tmp/ner_data_test'

def gen():
    with tf.gfile.GFile(filepath, 'r') as f:
        lines = [line.strip().split(' ') for line in f]
        index = 0
        while True:
            label = lines[index][0]
            features = list(lines[index][1])
            yield (features, label)
            index += 1
            if index == len(lines):
                index = 0


if __name__ == '__main__':
    dataset = tf.data.Dataset.from_tensors(tf.constant([['jiang', 'feng'], ['messi', 'henry']]))
    print(dataset.output_shapes)
    print(dataset.output_types)

    dataset2 = tf.data.Dataset.from_tensor_slices(tf.constant([['jiang', 'feng'], ['messi', 'henry']]))
    print(dataset.output_shapes)
    print(dataset.output_types)

    dataset3 = tf.data.Dataset.from_generator(gen, (tf.string, tf.string),
                                              (tf.TensorShape([None]), tf.TensorShape([])))

    dataset4 = tf.data.Dataset.range(100).map(
        lambda x: x + tf.random_uniform([], -10, 10, tf.int64))
    print(dataset4.output_shapes)
    print(dataset4.output_types)

    iterator = dataset3.make_one_shot_iterator()
    next_element = iterator.get_next()
    with tf.Session() as sess:
        for i in range(6):
            try:
                # sess.run(next_element)
                print(sess.run(next_element))
            except tf.errors.OutOfRangeError:
                break
