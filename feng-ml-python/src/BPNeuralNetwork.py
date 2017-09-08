import numpy as np
import pandas as pd


class BPNeuralNetWork(object):
    def __init__(self, input_n, hidden_n, output_n):
        self.input_n = input_n
        self.hidden_n = hidden_n
        self.output_n = output_n
        self.input_cells = np.ones(self.input_n, dtype=float)
        self.hidden_cells = np.ones(self.hidden_n, dtype=float)
        self.output_cells = np.ones(self.output_n, dtype=float)
        self.input_weights = np.random.rand(input_n, hidden_n)
        self.output_weights = np.random.rand(hidden_n, output_n)
        pass

    def predict(self, X):
        mathUtils = MathUtils()
        for i in range(self.input_n):
            self.input_cells[i] = X[i]
        for j in range(self.hidden_n):
            total = 0.0
            for i in range(self.input_n):
                total += self.input_cells[i] * self.input_weights[i][j]
            self.hidden_cells[j] = mathUtils.sigmod(total)
        for k in range(self.output_n):
            total = 0.0
            for j in range(self.hidden_n):
                total += self.hidden_cells[j] * self.output_weights[j][k]
            self.output_cells[k] = mathUtils.sigmod(total)
        return self.output_cells

    def back_propagation(self, x, y, learn):
        mathUtils = MathUtils()
        self.predict(x)

        # 输出层误差
        output_delta = np.zeros(self.output_n)
        for k in range(self.output_n):
            error = y[k] - self.output_cells[k]
            output_delta[k] = mathUtils.sigmoid_derivative(self.output_cells[k]) * error

        # 隐含层误差
        hidden_delta = np.zeros(self.hidden_n)
        for j in range(self.hidden_n):
            error = 0.0
            for k in range(self.output_n):
                error += output_delta[k] * self.output_weights[j][k]
            hidden_delta[j] = mathUtils.sigmoid_derivative(self.hidden_cells[j]) * error

        # 更新输出层权值
        for k in range(self.output_n):
            for j in range(self.hidden_n):
                self.output_weights[j][k] += learn * output_delta[k] * self.hidden_cells[k]

        # 更新隐含层权值
        for j in range(self.hidden_n):
            for i in range(self.input_n):
                self.input_weights[i][j] += learn * hidden_delta[j] * self.input_cells[i]
        error = 0.0
        for k in range(self.output_n):
            error += 0.5 * (y[k] - self.output_cells[k]) ** 2
        return error

    def fit(self, X, Y, limit=100000, learn=0.05):
        for i in range(limit):
            error = 0.0
            for i in range(len(X)):
                x = X[i]
                y = Y[i]
                error += self.back_propagation(x, y, learn)
                # print(error)


if __name__ == '__main__':
    file = '/Users/dianping/Downloads/iris.csv'
    df = pd.read_csv(file, header=None)
    # print(df.head(10)

    y = df.loc[0:99, 5].values
    Y = np.where(y == 'Iris-setosa', 0, 1)
    tmp_Y = []
    for ele in Y:
        tmp_Y1 = []
        tmp_Y1.append(ele)
        tmp_Y.append(tmp_Y1)
    Y = tmp_Y
    X = df.iloc[0:100, [0, 1, 2]].values
    bPNeuralNetWork = BPNeuralNetWork(3, 2, 1)
    bPNeuralNetWork.fit(X, Y)
    x = np.array([1.0, 5.6, 1.5])
    x1 = np.array([1.0, 5.1, 4.0])
    print(bPNeuralNetWork.predict(x))
    print(bPNeuralNetWork.predict(x1))
    # print(X)
    # print(Y)
    # print(len(X))
    # print(len(Y))
    # print([1.0] * 10)
