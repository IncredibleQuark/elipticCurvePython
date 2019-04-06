import math
import random
import gmpy2


def draw_prime():
    primes = []
    r = 4*random.getrandbits(32) + 3
    print(r)
    # ran = random.randint(3*2**256 + 4, 2**256 * 10)
    # print(ran)
    #
    # test = ran / 4 == 3
    #
    # if not test:
    #     draw_prime()
    #     return
    #
    # print(test)

    # r = random.randint(4*2**256, 2**256*10)
    # print(2**256)
    #
    if not is_prime(r):
        draw_prime()
        return
    # for n in range(4*2**256+4, 2**256*2):
    #     if is_prime(n):
    #         primes.append(n)
    #
    # print (primes)
    # return ran
    # return random.choice(primes)
    return r


def is_prime(n):

    if n == 1:
        return False

    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    max_divisor = int(math.floor(math.sqrt(n)))
    print(max_divisor)
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True


random_prime = draw_prime()

print(random_prime, "drawn prime number")


def calculate_b(a, x, y):
    # b = y^2 - (x^3 + ax)
    return y**2 - (x**3 + a * x)


def is_b_valid(b, a, p):
    return (4 * a**3 + 27 * b**2) % p != 0


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


# result = generate_curve()

# print(result)
