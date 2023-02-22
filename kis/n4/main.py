def main(n):
    if n == 0:
        return 0.07
    elif n == 1:
        return 0.96
    else:
        return main(n - 1) ** 2 - 3 * main(n - 2) ** 3


def main2(n):
    return 0.07 if n == 0 else 0.96 if n == 1 else main(
        n - 1) ** 2 - 3 * main(n - 2) ** 3


def main3(n):
    return 0.07 if n == 0 else 0.96 if n == 1 else main(
        n - 1) ** 2 - 3 * main(n - 2) ** 3


print(main(9))
print(main2(9))
print(main3(9))
