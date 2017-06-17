import math


class MathUtils(object):
    def __init__(self):
        pass

    def sigmod(self, x):
        return 1.0 / (1.0 + math.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def compute_distance(self, a, b):
        sum = 0.0
        for i in range(len(a)):
            sum += (a[i] - b[i]) * (a[i] - b[i])
        return sum


if __name__ == '__main__':
    mathUtiles = MathUtils()
    # print(mathUtiles.sigmod(0))
    a = [3, 2]
    b = [1, 2]
    print(mathUtiles.compute_distance(a, b))
