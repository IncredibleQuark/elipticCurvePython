import math
import random

def is_prime(n):

    if n == 1:
        return False

    if n == 2:
      return True

    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True




def draw_prime():
    primes = []

    for n in range(100, 210000):
        if (is_prime(n)):
            primes.append(n)

    print (primes)

    return random.choice(primes)


def calculate_b(a, x, y):
    # b = y^2 - (x^3 + ax)
    return y**2 - (x**3 + a * x)

def is_b_valid(b, a, p):
    return (4 * a**3 + 27 * b**2) % p != 0

random_prime = draw_prime()

print(random_prime, "drawn prime number")

def generate_curve():
    a = random.choice(range(1, random_prime))
    x = random.choice(range(1, random_prime))
    y = random.choice(range(1, random_prime))

    print(a, "a parameter")
    print(x, "x parameter")
    print(y, "y parameter")

    b = calculate_b(a, x, y)

    print(b, "b calulated")

    if not is_b_valid(b, a, random_prime):
        generate_curve()

    return a, x, b


result = generate_curve()

print(result)


def calculate_nwd(a,b):

    while b != 0:
        c = a % b
        a = b
        b = c

    return a

nwd = calculate_nwd(100, 30)
print(nwd)
            