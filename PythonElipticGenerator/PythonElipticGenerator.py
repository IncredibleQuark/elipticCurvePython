import random
import os
from Crypto.Util import number


def draw_prime_number():
    pr = number.getPrime(256, os.urandom)
    if pr % 4 != 3:
        return draw_prime_number()
    return pr


random_prime = draw_prime_number()
print(random_prime, "selected random prime number")


def is_delta_valid(a, b, p):
    return (4 * a**3 + 27 * b**2) % p != 0


def check_f(a, b, x):
    f = x**3 + a * x + b
    return True


def draw_parameters():
    a = random.randrange(0, random_prime-1)
    b = random.randrange(0, random_prime-1)
    x = random.randrange(0, random_prime-1)

    if not is_delta_valid(a, b, random_prime) and not check_f(a, b, x):
        return draw_parameters()

    print(a, "a parameter")
    print(b, "b parameter")
    print(x, "x")

    return a, b, x


result = draw_parameters()

print(result)
