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


def is_delta_valid(a, b, p):
    return (4 * a**3 + 27 * b**2) % p != 0


def calculate_f(a, b, x, p):
    return int((x ** 3 + a * x + b)) % p


def check_legendre(f, p):
    base = (p - 1) // 2  # use // operator to divide big integers
    mod = pow(f, base, p)
    return mod == 1

def calculate_y(f, p):
    powing = (p + 1) // 4
    y = pow(f, powing, p)
    return y

def test_equality(y, f, p, x, a, b):
    y_squared = pow(y, 2, p)
    f_test = (pow(x, 3) + a * x + b) % p
    return y_squared == f_test


def draw_parameters(random_prime):
    # draw a and b point
    a = random.randrange(2, random_prime-1)
    b = random.randrange(2, random_prime-1)

    # check if delta % p is different than 0
    if not is_delta_valid(a, b, random_prime):
        return draw_parameters()

    # draw x parameter
    x = random.randrange(2, random_prime-1)
    
    # calculate f
    f = calculate_f(a, b, x, random_prime)

    # check Legendre Symbol
    if not check_legendre(f, random_prime):
        return draw_parameters(random_prime)

    y = calculate_y(f, random_prime)
    # check equality
    if not test_equality(y, f, random_prime, x, a, b):
        return draw_parameters(random_prime)

    return {'a': a, 'b': b, 'x': x, 'y': y}

def main():
    # draw random prime number with given bit length
    random_prime = draw_prime_number()

    # draw eliptic curve parameters
    parameters = draw_parameters(random_prime)
    
    # print the results
    print(parameters['a'], "a")
    print(parameters['b'], "b")
    print(parameters['x'], "x")
    print(parameters['y'], "y")

# execute program
main()

