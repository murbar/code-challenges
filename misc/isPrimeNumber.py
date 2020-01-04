import math


def isPrime(number):
    boundary = math.floor(math.sqrt(number))
    for i in range(2, boundary+1):
        if number % i == 0:
            return False

    return number >= 2


def isPrime2(number):
    # here we avoid using any external functions
    # i * i <= number equivalent to i <= sqrt(num)

    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1

    # excludes 0 and 1
    return number >= 2


def isPrime3(number):
    # using sieve of Eratosthenes
    # faster, but using memory to store potentially large bit vector
    if number < 2:
        return False

    vector = [True] * (number + 1)
    p = 2
    while p * p <= number:
        if vector[p]:
            for i in range(p * p, number + 1, p):
                vector[i] = False
        p += 1

    return vector[-1]


assert isPrime(0) == False
assert isPrime(1) == False
assert isPrime(2) == True
assert isPrime(3) == True
assert isPrime(7) == True
assert isPrime(9) == False
assert isPrime(435375373415465733) == False
assert isPrime(87178291199) == True

assert isPrime2(0) == False
assert isPrime2(1) == False
assert isPrime2(2) == True
assert isPrime2(3) == True
assert isPrime2(7) == True
assert isPrime2(9) == False
assert isPrime2(435375373415465733) == False
assert isPrime2(87178291199) == True

assert isPrime3(0) == False
assert isPrime3(1) == False
assert isPrime3(2) == True
assert isPrime3(3) == True
assert isPrime3(7) == True
assert isPrime3(9) == False
# will crash - too much memory!
# assert isPrime3(435375373415465733) == False
# assert isPrime3(87178291199) == True
