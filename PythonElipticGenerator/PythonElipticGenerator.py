import random
import os
import math
from Crypto.Util import number

PRIME_NUMBER_SIZE = 256


def draw_prime_number():
    pr = number.getPrime(PRIME_NUMBER_SIZE, os.urandom)
    if pr % 4 != 3:
        return draw_prime_number()
    return pr


random_prime = draw_prime_number()
print(random_prime, "selected random prime number")


def is_delta_valid(a, b, p):
    return (4 * a**3 + 27 * b**2) % p != 0


def calculate_f(a, b, x):
    return int((x ** 3 + a * x + b)) % random_prime


def check_f(a, b, x):
    f = calculate_f(a, b, x)
    u = calculate_legendre(f, random_prime)
    return u == 1


def calculate_legendre(a, p):
    if a >= p or a < 0:
        return calculate_legendre(a % p, p)
    elif a == 0 or a == 1:
        return a
    elif a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a == p-1:
        if p % 4 == 1:
            return 1
        else:
            return -1
    else:
        if ((p-1)/2) % 2 == 0 or ((a-1)/2) % 2 == 0:
            return calculate_legendre(p, a)
        else:
            return (-1)*calculate_legendre(p, a)


def calculate_y(a, b, x):
    f = calculate_f(a, b, x) % random_prime
    # f = int((x ** 3 + a * x + b))
    po = int((random_prime + 1) / 4)
    y = pow(f, po, random_prime)

    print(f, 'sq')
    print(y, 'yyy')
    print(f == y**2)
    return y


def draw_parameters():
    a = random.randrange(0, random_prime-1)
    b = random.randrange(0, random_prime-1)
    x = random.randrange(0, random_prime-1)

    if not is_delta_valid(a, b, random_prime):
        return draw_parameters()

    if not check_f(a, b, x):
        return draw_parameters()

    print(a, "a parameter")
    print(b, "b parameter")
    print(x, "x")

    calculate_y(a, b, x)

    return a, b, x


result = draw_parameters()

print(result)
