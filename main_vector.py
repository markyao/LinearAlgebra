from playLA.Vector import Vector

if __name__ == '__main__':
    vec = Vector([5, 2])
    print("vec = {}".format(vec))
    print("len({} = {})".format(vec, len(vec)))
    print("vec = {}, vec[0] = {}, vec[1] = {}".format(vec, vec[0], vec[1]))

    vec2 = Vector([1, 3])
    print("vec2 = {}".format(vec2))
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero = Vector.zero(2)
    print(zero)
    print("{} + {} = {}".format(vec, zero, vec + zero))

    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(zero, zero.norm()))

    print("normalize {} = {}".format(vec, vec.normalize()))
    print(vec.normalize().norm())

    try:
        zero.normalize()
    except ZeroDivisionError:
        print("cannot normalize zero vector{}".format(zero))

    print(vec.dot(vec2))
