from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == '__main__':
    mat = Matrix([[1, 2], [3, 4]])
    print(mat)
    print("matrix.shape = {}".format(mat.shape()))
    print("matrix.size = {}".format(mat.size()))
    print("len(matrix) = {}".format(len(mat)))
    print("matrix[1][1] = {}".format(mat[1, 1]))

    print("matrix.row_vector(0) = {}".format(mat.row_vector(0)))
    print("matrix.col_vector(0) = {}".format(mat.col_vector(0)))

    mat2 = Matrix([[2, 1], [1, 1]])
    print("matrix.add: {}".format(mat + mat2))
    print("matrix.sub: {}".format(mat - mat2))
    print("matrix.scalar: {}".format(mat * 2))
    print("zero_2_3:{}".format(Matrix.zero(2, 3)))
    print(mat.dot(mat2))

    vec = Vector([1, 2])
    print(mat.dot(vec))
