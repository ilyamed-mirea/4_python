import math


def calc(k, i, j):
    return 81 * k ** 3 - 56 * math.log(k, math.e) ** 7 - 83 * (
            38 * i ** 3 + 1 + j) ** 2


def main(m, a, n):
    res = 0
    for j in range(1, n + 1):
        for i in range(1, a + 1):
            for k in range(1, m + 1):
                res += calc(k, i, j)
    return res


print(main(4, 6, 2))
print(main(2, 3, 8))
