import numpy as np


class OneHot:
    uniques = []

    def encoder(self, X):
        self.uniques = np.unique(X)
        Y = np.zeros((len(X), len(self.uniques)))
        j = 0
        for u in self.uniques:
            for i in range(len(X)):
                if X[i] == u:
                    Y[i][j] = 1
            j = j + 1
        return Y

    def decoder(self, Y):
        Z = np.zeros(len(Y))
        if len(self.uniques) != len(Y[0]):
            print("Columns must be the same size.")
            return
        else:
            for i in range(len(Y)):
                m = max(Y[i])
                for j in range(len(Y[i])):
                    if Y[i][j] == m:
                        Z[i] = self.uniques[j]
            return Z
