import numpy as np



class KNN(object):
    def __init__(self, n_neighbors):
        self.n_neighbors = n_neighbors
        pass

    def predict(self, x, y, neighbors):
        ranks = []
        for i in range[len(neighbors)]:
            c = x - neighbors[i]
            ranks.append(np.inner(c, c))
            pass


if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = b - a
    print(np.inner(c, c))
