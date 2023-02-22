from math import ceil


def main(x, z):
    n = len(z)
    x.insert(0, 0)
    z.insert(0, 0)
    res = 0
    for i in range(1, n + 1):
        left = x[ceil(i / 3)] ** 3
        right = 74 * z[n + 1 - ceil(i / 4)] ** 2
        res += (left + 1 + right) ** 7
    return res


print(main([0.59, -0.91, 0.45, -0.64, 0.29],
           [-0.58, 0.54, 0.33, 0.31, 0.35]))
