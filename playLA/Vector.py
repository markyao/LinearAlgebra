from ._global import is_zero, is_equal
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

    def normalize(self):
        """返回向量的单位向量"""
        if is_zero(self.norm()):
            raise ZeroDivisionError("向量模不能为零")
        return Vector(self._values) / self.norm()

    def dot(self, other):
        """返回两个向量点乘"""
        assert len(self) == len(other), \
            "向量长度需要相等"
        return sum(a * b for a, b in zip(self, other))

    def underlying_list(self):
        """返回vector底层列表"""
        return self._values[:]

    def __add__(self, other):
        """向量加法"""
        assert len(self) == len(other), \
            "向量长度需要相等"
        return Vector([a + b for a, b in zip(self, other)])

    def __mul__(self, k):
        """向量的数量乘"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        """返回向量的数量除法 self / k"""
        return (1 / k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __eq__(self, other):
        other_list = other.underlying_list()
        if len(other_list) != len(self._values):
            return False
        return all(is_equal(x, y) for x, y in zip(self._values, other_list))

    def __neq(self, other):
        return not (self == other)

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
