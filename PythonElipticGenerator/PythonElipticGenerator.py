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

    for n in range(1000, 2100):
        if (is_prime(n)):
            primes.append(n)

    print (primes)

    return random.choice(primes)

random_prime = draw_prime()

print(random_prime)