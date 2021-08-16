import math


class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """返回一个dim维度的向量"""
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e ** 2 for e in self))

    def __add__(self, other):
        """向量加法"""
        assert len(self) == len(other), \
            "向量长度比较相等"
        return Vector([a + b for a, b in zip(self, other)])

    def __mul__(self, k):
        """向量的数量乘"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return self * k

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __sub__(self, other):
        """向量减法"""
        assert len(self) == len(other), \
            "向量长度比较相等"
        return Vector([a - b for a, b in zip(self, other)])

    def __getitem__(self, index):
        """返回向量索引index所有对应的元素值"""
        return self._values[index]

    def __len__(self):
        """返回向量的长度：有多少元素"""
        return len(self._values)

    def __iter__(self):
        """返回对象的迭代器"""
        return self._values.__iter__()

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
