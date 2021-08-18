from playLA.Matrix import Matrix

if __name__ == '__main__':
    mat = Matrix([[1, 2], [3, 4]])
    print(mat)
    print("matrix.shape = {}".format(mat.shape()))
    print("matrix.size = {}".format(mat.size()))
    print("len(matrix) = {}".format(len(mat)))
    print("matrix[1][1] = {}".format(mat[1, 1]))

    print("matrix.row_vector(0) = {}".format(mat.row_vector(0)))
    print("matrix.col_vector(0) = {}".format(mat.col_vector(0)))
