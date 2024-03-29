from .Vector import Vector
from .Matrix import Matrix
from ._global import is_zero


class LinearSystem:

    def __init__(self, A, b=None):
        assert b is None or A.row_num() == len(b), \
            "矩阵A的行数需和向量b长度相等"
        self._m = A.row_num()
        self._n = A.col_num()

        if b is None:
            self.Ab = [A.row_vector(i) for i in range(self._m)]
        if isinstance(b, Vector):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                       for i in range(self._m)]
        if isinstance(b, Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list())
                       for i in range(self._m)]
        self.pivots = []

    def _max_row(self, index_i, index_j, m):
        best, r = self.Ab[index_i][index_j], index_i
        for i in range(index_i + 1, m):
            if self.Ab[i][index_j] > best:
                best, r = self.Ab[i][index_j], i
        return r

    def _forward(self):
        i, k = 0, 0
        while i < self._m and k < self._n:
            max_row = self._max_row(i, k, self._m)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                for j in range(i + 1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]
                self.pivots.append(k)
                i += 1

    def _backward(self):
        n = len(self.pivots)
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]

    def gauss_jordan_elimination(self):
        """如果有解返回 True 否则返回False"""
        self._forward()
        self._backward()

        for i in range(len(self.pivots), self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])


def inv(A):
    if A.row_num() != A.col_num():
        return None

    n = A.row_num()
    ls = LinearSystem(A, Matrix.identity(n))
    if not ls.gauss_jordan_elimination():
        return None

    inv = [[row[i] for i in range(n, 2 * n)] for row in ls.Ab]
    return Matrix(inv)


def rank(A):
    ls = LinearSystem(A)
    ls.gauss_jordan_elimination()

    zero = Vector.zero(A.col_num())
    return sum([row != zero for row in ls.Ab])
