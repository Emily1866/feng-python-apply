#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def load_file(path):
    df = pd.read_csv(path, sep=':')
    train_X = df.iloc[:, 0:10].values
    train_Y = df.iloc[:, 15].values
    return train_X, train_Y


if __name__ == "__main__":
    train_path = '/Users/lionel/Desktop/data/recommendDish/dish/dish_feature.csv'
    test_path = '/Users/lionel/Desktop/data/recommendDish/dish/dish_test.csv'
    train_X, train_Y = load_file(train_path)
    test_X, test_Y = load_file(test_path)
    # clf = tree.DecisionTreeClassifier()
    clf = RandomForestClassifier(n_estimators=10)
    X = np.array(train_X)
    Y = np.array(train_Y)
    clf = clf.fit(X, Y)
    t_x = np.array(test_X)
    t_y = np.array(test_Y)
    y = (clf.predict(t_x))
    num = 0
    for i in range(len(t_y)):
        if t_y[i] == y[i]:
            num += 1
    print(num / len(t_y))
