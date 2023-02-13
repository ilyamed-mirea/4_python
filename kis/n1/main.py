import math


def main1(x, z):
    lefttop = (2 * (math.acos(z) ** 6)) + \
              (30 * (math.cos(27 * (x ** 2) + 22 * (x ** 3)) ** 2))
    leftbottom = 43 * (math.cos(z - 1 - (9 * (z ** 3))) ** 2) - (40 * (x ** 4))
    left = math.sqrt(lefttop / leftbottom)
    right = (math.log((z ** 2) - z - (12 * (x ** 3)),
                      math.e) ** 6) + (x ** 2)
    return left - right


def main3(x, z):
    left = math.sqrt(
        (
                (2 * pow(math.acos(z), 6))
                + (30 * pow(math.cos(27 * pow(x, 2) + 22 * pow(x, 3)), 2))
        )
        / (43 * pow(math.cos(z - 1 - (9 * pow(z, 3))), 2) - (40 * pow(x, 4)))
    )
    right = (pow(math.log(pow(z, 2) - z - (12 * pow(x, 3)),
                          math.e), 6) + pow(x, 2))
    return left - right


def main2(x, z):
    lefttop = (2 * pow(math.acos(z), 6)) + \
              (30 * pow(math.cos(27 * pow(x, 2) + (22 * pow(x, 3))), 2))
    leftbottom = 43 * pow(math.cos(z - 1 - (9 * pow(z, 3))), 2) - (
            40 * pow(x, 4))
    left = lefttop / leftbottom
    left = math.sqrt(left)
    right = pow(math.log(pow(z, 2) - z - (12 * pow(x, 3)),
                         math.e), 6) + pow(x, 2)
    return left - right


def main666(x, z):
    acos_z = math.acos(z)
    pow_acos_z = pow(acos_z, 6)
    two_pow_acos_z = 2 * pow_acos_z
    x_squared = pow(x, 2)
    x_cubed = pow(x, 3)
    twenty_seven_x_squared = 27 * x_squared
    twenty_two_x_cubed = 22 * x_cubed
    cos_27_x_squared_22_x_cubed = math.cos(
        twenty_seven_x_squared + twenty_two_x_cubed)
    pow_cos_27_x_squared_22_x_cubed = pow(cos_27_x_squared_22_x_cubed, 2)
    thirty_pow_cos_27_x_squared_22_x_cubed \
        = 30 * pow_cos_27_x_squared_22_x_cubed
    z_minus_1 = z - 1
    pow_z = pow(z, 3)
    nine_pow_z = 9 * pow_z
    z_minus_1_minus_9_pow_z = z_minus_1 - nine_pow_z
    cos_z_minus_1_minus_9_pow_z = math.cos(z_minus_1_minus_9_pow_z)
    pow_cos_z_minus_1_minus_9_pow_z = pow(cos_z_minus_1_minus_9_pow_z, 2)
    forty_pow_x_4 = 40 * pow(x, 4)
    ft_pow_cos_z_minus_1_minus_9_pow_z_minus_40_pow_x_4 \
        = 43 * pow_cos_z_minus_1_minus_9_pow_z - forty_pow_x_4
    left_numerator = two_pow_acos_z + thirty_pow_cos_27_x_squared_22_x_cubed
    left_denominator = ft_pow_cos_z_minus_1_minus_9_pow_z_minus_40_pow_x_4
    left = math.sqrt(left_numerator / left_denominator)
    pow_z_minus_z_minus_12_pow_x_3 = z ** 2 - z - (12 * x_cubed)
    log_pow_z_minus_z_minus_12_pow_x_3 = math.log(
        pow_z_minus_z_minus_12_pow_x_3, math.e)
    pow_log_pow_z_minus_z_minus_12_pow_x_3 = pow(
        log_pow_z_minus_z_minus_12_pow_x_3, 6)
    right = pow_log_pow_z_minus_z_minus_12_pow_x_3 + x ** 2
    return math.sqrt(left_numerator / left_denominator) \
        - pow_log_pow_z_minus_z_minus_12_pow_x_3 - x ** 2


def arccos(x):
    return math.acos(x)


def cos(x):
    return math.cos(x)


def log(x, base):
    return math.log(x, base)


def sqrt(x):
    return x ** 0.5


def pow(x, y):
    return x ** y


def main(x, z):
    left = sqrt(
        (
                (2 * pow(arccos(z), 6))
                + (30 * pow(cos(27 * pow(x, 2) + 22 * pow(x, 3)), 2))
        )
        / (43 * pow(cos(z - 1 - (9 * pow(z, 3))), 2) - (40 * pow(x, 4)))
    )
    right = (pow(log(pow(z, 2) - z - (12 * pow(x, 3)),
                     math.e), 6) + pow(x, 2))
    return left - right


print(main(0.15, -0.22))  # = -7.23e+00
print(main(0.11, -0.99))  # 6.45e+00
print(main(-0.94, -0.99))  # = -2.12e+02
