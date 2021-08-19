import matplotlib.pyplot as plt

if __name__ == '__main__':
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(5, 5))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y)
    plt.show()
