from playLA.Matrix import Matrix
from playLA.Vector import Vector


class LinearSystem:

    def __init__(self, A, b):
        assert A.row_num() == len(b), \
            "矩阵A的行数需和向量b长度相等"
        self._m = A.row_num()
        self._n = A.col_num()
        assert self._m == self._n

        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                   for i in range(self._m)]

    def _max_row(self, i, n):
        best, r = self.Ab[i][i], i
        for j in range(i + 1, n):
            if self.Ab[j][i] > best:
                best, r = self.Ab[j][i], j
        return r

    def _forward(self):
        n = self._m
        for i in range(n):
            max_row = self._max_row(i, n)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            self.Ab[i] = self.Ab[i] / self.Ab[i][i]
            for j in range(i + 1, n):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    def _backward(self):
        n = self._m
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    def gauss_jordan_elimination(self):
        self._forward()
        self._backward()

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])
