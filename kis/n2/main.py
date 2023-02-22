import math


def main(z: int):
    if z < 30:
        return 60 * z + math.atan(z) ** 4 + 82 * z ** 6
    elif z < 117:
        return 23 * z ** 7
    else:
        return 2 * z ** 9


def main3(z: int):
    return (60 * z + math.atan(z) ** 4 + 82 * z ** 6) if (z < 30) else (
        23 * z ** 7 if (z < 117) else 2 * z ** 9)


print(main(75))

print(main3(75))
