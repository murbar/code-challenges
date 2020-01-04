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
