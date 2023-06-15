from playLA.Vector import Vector
from playLA.GramSchmitProcess import gram_schmidt_process

if __name__ == '__main__':
    basis1 = [Vector([2, 1]), Vector([1, 1])]
    res1 = gram_schmidt_process(basis1)
    for row in res1:
        print(row)

    res1 = [row / row.norm() for row in res1]
    for row in res1:
        print(row)

    print(res1[0].dot(res1[1]))
    print()

    basis2 = [Vector([2, 3]), Vector([4, 5])]
    res2 = gram_schmidt_process(basis1)
    res2 = [row / row.norm() for row in res2]
    for row in res2:
        print(row)

    print(res2[0].dot(res2[1]))
    print()

    basis3 = [Vector([1, 0, 1]), Vector([3, 1, 1]), Vector([-1, -1, -1])]
    res3 = gram_schmidt_process(basis3)
    res3 = [row / row.norm() for row in res3]
    for row in res3:
        print(row)

    print(res3[0].dot(res3[1]))
    print(res3[0].dot(res3[2]))
    print(res3[1].dot(res3[2]))
    print()
