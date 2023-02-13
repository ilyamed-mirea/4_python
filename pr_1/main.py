# n1.1
# 1) оператор космического корабля <=> - используется для сравнения двух объектов
# 2) существует модуль "antigravity". Если вы выполните import antigravity, ваш веб-браузер откроет комикс из XKCD "Python Antigravity" (он откроет комикс в новом окне).
# 3) Для тех, кто любит языки программирования с различным синтаксисом, существует режим "Benevolent Dictator for Life" (BDFL).
# 4) В модуле functools есть функция cmp_to_key. Эта функция позволяет использовать функцию сравнения в качестве ключа для сортировки списков, словарей и т.д. в Python.

# n1.2 - 42 in 10 different ways
42
0b101010  # (binary)
0o52  # (octal)
0x2A  # (hexadecimal)
42.0  # (floating point)
42 + 0j  # (complex number)
int(42)  # (casting as integer)
42 * 1  # (multiplication)
42 / 1  # (division)
42 // 1  # (floor division)

# n1.3
# диапазон значений int ограничен только объемом памяти, доступной в системе
# Диапазон представимых чисел в формате float составляет приблизительно ±10^308 с точностью от 15 до 17 десятичных знаков.

# n1.4
# функция divmod. Эта функция возвращает купон и остаток от операции деления в виде кортежа.

# n1.5
# a = 10
# while a != 0:
#     a -= 0.1
# значение a никогда не будет равным 0 из-за неточности представления чисел с плавающей точкой

# n1.6
# z = 1
# z <<= 40
# 2 ** z # ** возвращают int и работает за O(Log(n))
# pow(2, z) # pow возвращает float и работает за O(n)
# print("done")
# потому что 2 в степени z слишком большое число и вызывает OverflowError для int

# n1.7
# i = 0
# while i < 10:
#     print(i)
#     ++i
# потому что в питоне нет оператора ++i

# n1.8
(True * 2 + False) * -True
# (1*2+0) * (-1) = -2

# n1.9
x = 5
1 < x < 10
# True потому что 10 > 5 и 5 > 1
x = 5
1 < (x < 10)


# False потому что x < 10 = True и True > 1 = False


# ----------------------------


# n2
# def = 3 # SyntaxError: invalid syntax
# 3 = x # SyntaxError: cannot assign to literal
# print(abcdsbcsdb) # NameError: name abcdsbcsdb is not defined
# test = "test # SyntaxError: unterminated string literal
# "test" - 5.5 # TypeError: unsupported operand type(s) for -: 'str' and 'float'
# def ttt():
#     print("test") # IndentationError: expected an indented block
#         print("test2")
#    print("test3") # IndentationError: unindent does not match any outer indentation level

# import math
# math.sqrt(-1) # math error
#
# import sys
# sys.float_info.max * 2345 # OverflowError: math range error


# ----------------------------


# n3.1
# *12 = 4x+
def multiply_by_12(x):
    y = x + x  # *2
    z = y + y  # *4
    d = z + z  # *8
    b = d + d  # *16
    return b - z


# print(multiply_by_12(3))

# n3.2
# Умножение на 16. Используйте 4 сложения.
def multiply_by_16(x):
    y = x + x  # *2
    z = y + y  # *4
    d = z + z  # *8
    b = d + d  # *16
    return b


# print(multiply_by_16(2))


# n3.3
def multiply_by_15(x):
    y = x + x  # *2
    z = y + y  # *4
    d = z + z  # *8
    return d - (x - d)  # *8 - (x - *8)


# print(multiply_by_15(3))

# n3.5
def fast_mul(a, b):
    temp_sum = 0
    while (a):
        if a & 1:
            temp_sum += b
        b << 1
        a >> 1
    return temp_sum


print(fast_mul(3, 6))


# n3.6
def fast_pow(base, e):
    res = 1
    while (e):
        if e % 2 != 0:
            res = fast_mul(res, base)
        base = fast_mul(base, base)
        e >> 1
    return res


print(fast_pow(3, 1))


# n3.7
def mul16(x, y):
    def mul_bits(x, y, bits):
        x &= (2 ** bits - 1)
        y &= (2 ** bits - 1)
        return x * y

    x_low = x & 0xff
    x_high = x >> 8
    y_low = y & 0xff
    y_high = y >> 8

    res_low = mul_bits(x_low, y_low, 8)
    res_mid = mul_bits(x_low, y_high, 8) + mul_bits(x_high, y_low, 8)
    res_high = mul_bits(x_high, y_high, 8)

    res = (res_high << 16) + (res_mid << 8) + res_low
    return res


# n3.8
def fast_mul_gen(y):
    res = 'def f(x):\n'
    res += '    r = 0\n'
    while y > 1:
        if y & 1:
            res += '    r += x\n'
        res += '    x += x\n'
        y >>= 1
    res += '    r += x\n'
    res += '    return r\n'
    return res
