from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
from scipy.spatial import KDTree

if __name__ == '__main__':
    # file = '/Users/dianping/Downloads/iris.csv'
    # df = pd.read_csv(file, header=None)
    # # print(df.head(10)
    #
    # y = df.loc[0:99, 5].values
    # Y = np.where(y == 'Iris-setosa', 0, 1)
    # X = df.iloc[0:100, [1, 2]].values

    """
    神经网络算法预测数据
    """
    # clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    # clf.fit(X, Y)
    # l = clf.predict([[5.9, 4.05], [5.5, 1.4]])
    # print(l)
    # array = [[1, 9, 3], [4, 2, 6], [7, 4, 9], [1, 1, 1]]
    #
    # kd_tree = KDTree(array)
    # print(kd_tree.node)

    sentenct = '<doc id="18" url="https://zh.wikipedia.org/wiki?curid=18" title="哲学">'
